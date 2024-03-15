#include "../../include/Operations/ast_increment.hpp"


void LeftIncrement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = value_->fetchVariable(stream, context);
    Variable variable_specs = context.getVariableSpecs(value_->getIdentifier());

    value_->EmitRISC(stream, srcReg, context);

    stream <<"addi " << context.getRegisterName(srcReg) << ", "
        << context.getRegisterName(srcReg) << ", 1" << std::endl;
    stream << "mv " << context.getRegisterName(destReg) << ", " << context.getRegisterName(srcReg) << std::endl;
    stream << "sw " << context.getRegisterName(srcReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;

    context.freeUpRegister(srcReg);
}

void LeftIncrement::Print(std::ostream &stream) const {
    stream << "(";
    stream << "++";
    value_->Print(stream);
    stream << ")";
}


void LeftDecrement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = value_->fetchVariable(stream, context);
    Variable variable_specs = context.getVariableSpecs(value_->getIdentifier());

    value_->EmitRISC(stream, srcReg, context);
    stream <<"addi " << context.getRegisterName(srcReg) << ", "
        << context.getRegisterName(srcReg) << ", -1" << std::endl;
    stream << "mv " << context.getRegisterName(destReg) << ", " << context.getRegisterName(srcReg) << std::endl;
    stream << "sw " << context.getRegisterName(srcReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;

    context.freeUpRegister(srcReg);
}

void LeftDecrement::Print(std::ostream &stream) const {
    stream << "(";
    stream << "--";
    value_->Print(stream);
    stream << ")";
}


void RightIncrement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = value_->fetchVariable(stream, context);
    Variable variable_specs = context.getVariableSpecs(value_->getIdentifier());

    value_->EmitRISC(stream, srcReg, context);

    stream << "mv " << context.getRegisterName(destReg) << ", " << context.getRegisterName(srcReg) << std::endl;
    stream <<"addi " << context.getRegisterName(srcReg) << ", "
        << context.getRegisterName(srcReg) << ", 1" << std::endl;
    stream << "sw " << context.getRegisterName(srcReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;

    context.freeUpRegister(srcReg);
}

void RightIncrement::Print(std::ostream &stream) const {
    stream << "(";
    value_->Print(stream);
    stream << "++";
    stream << ")";
}


void RightDecrement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = value_->fetchVariable(stream, context);
    Variable variable_specs = context.getVariableSpecs(value_->getIdentifier());

    value_->EmitRISC(stream, srcReg, context);

    stream << "mv " << context.getRegisterName(destReg) << ", " << context.getRegisterName(srcReg) << std::endl;
    stream << "addi " << context.getRegisterName(srcReg) << ", "
        << context.getRegisterName(srcReg) << ", -1" << std::endl;
    stream << "sw " << context.getRegisterName(srcReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;

    context.freeUpRegister(srcReg);
}

void RightDecrement::Print(std::ostream &stream) const {
    stream << "(";
    value_->Print(stream);
    stream << "--";
    stream << ")";
}
