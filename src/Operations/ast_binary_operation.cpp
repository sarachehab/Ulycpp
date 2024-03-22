#include "../../include/Operations/ast_binary_operation.hpp"
#include "../../include/ast_identifier.hpp"

Specifier BinaryOperation::getType(Context& context) const { return left_->getType(context); }

void BinaryOperation::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    Specifier type = context.getLastOperationType(); 

    int leftReg = context.allocateRegister(type);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(type);
    right_->EmitRISC(stream, rightReg, context);

    Identifier* proba;

    proba = dynamic_cast<Identifier*>(left_);
    if (proba != nullptr){
        HandlePointers(stream, left_, destReg, leftReg, rightReg, type, context);
    } else {
        proba = dynamic_cast<Identifier*>(right_);
        if (proba != nullptr){
            HandlePointers(stream, right_, destReg, rightReg, leftReg, type, context);
        } else { 
            stream << getInstruction(type) << " " << context.getRegisterName(destReg) << ", "
                << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
        }
    }

    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void BinaryOperation::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}


void BinaryOperation::HandlePointers(std::ostream& stream, Node* operand_, int destReg, int op1Reg, int op2Reg, Specifier type, Context& context) const {
    Variable variable_specs = context.getVariableSpecs(operand_->getIdentifier());
    ProgramVarType var_type = variable_specs.var_type;
    int memory_cells_allocated = SpecifierSize[variable_specs.pointing_to];

    switch(var_type) {
        case ProgramVarType::_pointer:
            stream << "slli " << context.getRegisterName(op2Reg) << ", " << context.getRegisterName(op2Reg) << ", 2" << std::endl;
            stream << getInstruction(type) << " " << context.getRegisterName(destReg) << ", "
                << context.getRegisterName(op1Reg) << ", " << context.getRegisterName(op2Reg) << std::endl;
            break;
        case ProgramVarType::_unique:
        case ProgramVarType::_array:
            stream << getInstruction(type) << " " << context.getRegisterName(destReg) << ", "
                << context.getRegisterName(op1Reg) << ", " << context.getRegisterName(op2Reg) << std::endl;
        default: break;
    }
}