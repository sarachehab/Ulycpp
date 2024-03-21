#include "../include/ast_sizeof.hpp"

void SizeOf::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    Specifier type = type_specifier_->getType(context);
    int size = SpecifierSize[type];
    stream << "li " << context.getRegisterName(destReg) << ", " << size << std::endl;
}

void SizeOf::Print(std::ostream &stream) const {
    stream << "sizeof(";
    type_specifier_->Print(stream);
    stream << ")";
}
