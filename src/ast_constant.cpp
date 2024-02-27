#include "ast_constant.hpp"

void IntConstant::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    stream << "li " << context.getRegisterName(destReg) << ", " << value_ << std::endl;
}

void IntConstant::Print(std::ostream &stream) const
{
    stream << value_;
}
