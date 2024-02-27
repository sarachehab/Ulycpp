#include "ast_jump_statement.hpp"

void ReturnStatement::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    if (expression_ != nullptr)
    {
        // TODO: if return statement
        // TODO: if function call inside of function call + val saved: int x = getNum(y);
        int regA0 = 10; // TODO: hard coded into a0
        expression_->EmitRISC(stream, regA0, context);
    }
    stream << "ret" << std::endl;
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
