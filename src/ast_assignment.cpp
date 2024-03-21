#include "ast_assignment.hpp"
#include "../include/Arrays/ast_array_index.hpp"

std::string Assignment::getIdentifier() const {
    return target_variable_->getIdentifier();
}

int Assignment::getSize() const {
    return target_variable_->getSize();
}

Node* Assignment::getValToAssign() const {
    return value_to_assign_;
}

void Assignment::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = target_variable_->fetchVariable(context);
    Variable target_specs = context.getVariableSpecs(getIdentifier());
    
    Specifier type = target_specs.type;
    int memory_cells_allocated = SpecifierSize[type];
    
    context.setOperationType(type);
    
    value_to_assign_->EmitRISC(stream, srcReg, context);

    // initialising bcs switch was nagging
    ArrayIndex* array_index_;
    int tmpReg = 0;
    switch(target_specs.var_type){

        case ProgramVarType::_unique:

            switch (target_specs.type_scope) {

                case VarScope::_local:
                    stream << context.getStoreInstruction(type) << " " << context.getRegisterName(srcReg) << ", " << 
                        context.getVariableSpecs(target_variable_->getIdentifier()).sp_offset << "(s0)" << std::endl;
                    break;

                case VarScope::_global:
                    tmpReg = context.allocateRegister(Specifier::_int);
                    stream << "lui " << context.getRegisterName(tmpReg) << ", %hi(" << getIdentifier() << ")" << std::endl;
                    stream << context.getStoreInstruction(type) << " " <<  context.getRegisterName(srcReg) 
                        << ", %lo(" << getIdentifier() << ")(" << context.getRegisterName(tmpReg) << ")" << std::endl;
                    context.freeUpRegister(tmpReg);
                    break;
            }
           
            break;

        case ProgramVarType::_array:
            array_index_ = dynamic_cast<ArrayIndex* >(target_variable_);
            tmpReg = context.allocateRegister(Specifier::_int);
            std::cerr << "assigned list" << std::endl;
            array_index_->computeIndex(stream, tmpReg, context);
            stream << context.getStoreInstruction(type) << " " << context.getRegisterName(srcReg) << ", 0(" 
                        << context.getRegisterName(tmpReg) << ")" << std::endl;
            context.freeUpRegister(tmpReg);
            break;

        default: std::runtime_error("Type not recognised in Assignment.cpp");
    }

    // housekeeping, spill computed value to memory
    target_specs.reg = -1;
    context.freeUpRegister(srcReg);
    context.updateVariableSpecs(target_variable_->getIdentifier(), target_specs);
}

void Assignment::Print(std::ostream &stream) const {
    stream << target_variable_->getIdentifier() << " = ";
    value_to_assign_->Print(stream);
    stream << ";" << std::endl;
}
