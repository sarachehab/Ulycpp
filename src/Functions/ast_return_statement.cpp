#include "../../include/Functions/ast_return_statement.hpp"

void ReturnStatement::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    context.setOperationType(context.getReturnType());
    
    if (expression_ != nullptr) {
        expression_->EmitRISC(stream, destReg, context);
    }

    stream << "j " << context.getFunctionEndLabel() << std::endl;
}

void ReturnStatement::Print(std::ostream &stream) const
{
    stream << "return";
    if (expression_ != nullptr)
    {
        stream << " ";
        expression_->Print(stream);
    }
    stream << ";" << std::endl;
}
