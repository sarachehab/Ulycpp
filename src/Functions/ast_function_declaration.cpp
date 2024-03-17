#include "../../include/Functions/ast_function_declaration.hpp"

void ExternalDeclaration::EmitRISC(std::ostream& stream, int destReg, Context& context) const {}

void ExternalDeclaration::Print(std::ostream& stream) const {
    declaration_->Print(stream);
    stream << std::endl;
}

void InternalFunction::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    declaration_->EmitRISC(stream, destReg, context);
}
