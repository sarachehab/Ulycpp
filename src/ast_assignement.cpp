#include "ast_assignement.hpp"

void Assignement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = target_variable_->fetchVariable(stream, context);
    value_to_assign_->EmitRISC(stream, srcReg, context);
    stream << "sw " << context.getRegisterName(srcReg) << ", " << context.getVariableSpecs(target_variable_->getIdentifier()).sp_offset << "(sp)" << std::endl;
}

void Assignement::Print(std::ostream &stream) const {
    stream << target_variable_->getIdentifier() << " = ";
    value_to_assign_->Print(stream);
    stream << ";" << std::endl;
}
