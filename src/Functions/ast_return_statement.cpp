#include "../../include/Functions/ast_return_statement.hpp"

void ReturnStatement::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    std::cerr << "COMPILER: In return with expr" << std::endl;
    if (expression_ != nullptr)
    {
        // TODO: if return statement
        // TODO: if function call inside of function call + val saved: int x = getNum(y);
        std::cerr << "COMPILER: Printing return with expr" << std::endl;
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
