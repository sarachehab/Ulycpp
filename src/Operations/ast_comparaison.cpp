#include "../../include/Operations/ast_comparaison.hpp"


void Comparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int leftReg = context.allocateRegister(stream);
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister(stream);
    right_->EmitRISC(stream, rightReg, context);
    stream << "sub " << context.getRegisterName(destReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << getInstruction() << context.getRegisterName(destReg) << ", " << context.getRegisterName(destReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void Comparaison::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}


void CompositeComparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int leftReg = context.allocateRegister(stream);
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister(stream);
    right_->EmitRISC(stream, rightReg, context);
    int tmpReg = context.allocateRegister(stream);
    stream << getInstruction() << context.getRegisterName(tmpReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "sub " << context.getRegisterName(leftReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "seqz " << context.getRegisterName(leftReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    stream << "or " << context.getRegisterName(destReg) << ", " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void CompositeComparaison::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}


std::string LessThan::getInstruction()      const { return "slt "; }
std::string LessThan::getOperation()        const { return " < "; }

std::string LessThanEqual::getInstruction() const { return "slt "; }
std::string LessThanEqual::getOperation()   const { return " <= "; }

std::string GreaterThan::getInstruction()   const { return "sgt "; }
std::string GreaterThan::getOperation()     const { return " > "; }

std::string GreaterThanEqual::getInstruction()  const { return "sgt "; }
std::string GreaterThanEqual::getOperation()    const { return " >= "; }

std::string Equal::getInstruction()         const { return "seqz "; }
std::string Equal::getOperation()           const { return " == "; }

std::string NotEqual::getInstruction()      const { return "snez "; }
std::string NotEqual::getOperation()        const { return " != "; }