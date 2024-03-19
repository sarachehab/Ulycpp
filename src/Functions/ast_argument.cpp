#include "../../include/Functions/ast_argument.hpp"

void ArgumentList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int reg = 10;
    for (auto arg : nodes_){
        arg->EmitRISC(stream, reg++, context);
    }
}

void ArgumentList::Print(std::ostream& stream) const {
    for (auto arg : nodes_){
        arg->Print(stream);
        stream << ", ";
    }
}
