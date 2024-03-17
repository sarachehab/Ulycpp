#include "../../include/Functions/ast_argument.hpp"

void ArgumentList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    for (auto arg : nodes_){
        int reg = 0;
        arg->EmitRISC(stream, reg++, context);
    }
}

void ArgumentList::Print(std::ostream& stream) const {
    for (auto arg : nodes_){
        arg->Print(stream);
        stream << ", ";
    }
}
