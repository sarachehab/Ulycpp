#include "../../include/Functions/ast_function_call.hpp"

std::string FunctionCall::getIdentifier() const {
    return function_name_->getIdentifier();
}

Specifier FunctionCall::getType(Context& context) const {
    return context.getReturnType(getIdentifier());
}


void FunctionCall::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier return_type = getType(context);

    std::cerr << "In function call print" << std::endl;
    if (arguments_ != nullptr){
        arguments_->EmitRISC(stream, destReg, context);
    }

    int returnReg;
    switch(return_type){
        case Specifier::_int:
            returnReg = 10;
            break;
        case Specifier::_double:
        case Specifier::_float:
            returnReg = 42;
            break;
        default: throw std::runtime_error("Type not recognised in FunctionCall EmitRISC");
    }

    stream << "call " << function_name_->getIdentifier() << std::endl;
    context.FlushRegisters();
    stream << "nop " << std::endl;
    stream << context.getMoveInstruction(return_type) << " " << context.getRegisterName(destReg) << ", " << context.getRegisterName(returnReg) << std::endl;
    std::cerr << "COMPILER: Done function call print" << std::endl;
}


void FunctionCall::Print(std::ostream &stream) const {
    stream << function_name_->getIdentifier() << "(";
    if (arguments_ != nullptr){
        arguments_->Print(stream);
    }
    stream << ")";
}
