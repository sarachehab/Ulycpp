#include "ast_assignement.hpp"

void Assignement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    if (declaration_){
        throw std::runtime_error("Have not implemented declarations with assignements yet (ast_assignement)");
    } else {
        int srcReg = assigned_variable_->fetchVariable(context);
        value_to_assign_->EmitRISC(stream, srcReg, context);
    }
}

void Assignement::Print(std::ostream &stream) const {
    std::cout << "implement this" << std::endl;
}
