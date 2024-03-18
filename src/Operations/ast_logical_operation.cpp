#include "../../include/Operations/ast_logical_operation.hpp"

Specifier LogicalOperation::getType(Context& context) const { return Specifier::_int; }

void LogicalOperation::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    int leftReg = context.allocateRegister(Specifier::_int);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(Specifier::_int);
    right_->EmitRISC(stream, rightReg, context);

    stream << "snez " << context.getRegisterName(leftReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    stream << "snez " << context.getRegisterName(rightReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << getInstruction(Specifier::_int) << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;

    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void LogicalOperation::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}


std::string Negate::getInstruction(Specifier type) const { return "neg "; }
std::string Negate::getOperation() const { return " - "; }

std::string LogicalOr::getInstruction(Specifier type) const { return "or "; }
std::string LogicalOr::getOperation() const { return " || "; }

std::string LogicalAnd::getInstruction(Specifier type) const { return "and "; }
std::string LogicalAnd::getOperation() const { return " && "; }
