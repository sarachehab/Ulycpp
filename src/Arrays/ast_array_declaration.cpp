#include "../../include/Arrays/ast_array_declaration.hpp"

bool ArrayDeclarator::isArray() const { return true; }

int ArrayDeclarator::getSize() const {
    if (constant_expression_ == nullptr){
        return -1;
    }
    return constant_expression_->getValue();
}

std::string ArrayDeclarator::getIdentifier() const {
    return direct_declarator_->getIdentifier();
}

void ArrayDeclarator::EmitRISC(std::ostream& stream, int destReg, Context& context) const {}

void ArrayDeclarator::Print(std::ostream& stream) const {
    stream << direct_declarator_->getIdentifier() << "[";
    if (constant_expression_ != nullptr){
        stream << constant_expression_->getValue();
    }
    stream << "]"; 
}

ProgramVarType ArrayDeclarator::defineVarType() const {
    return ProgramVarType::_array;
}