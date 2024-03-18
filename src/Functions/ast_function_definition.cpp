#include "../../include/Functions/ast_function_definition.hpp"

void FunctionDefinition::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    // TODO: these are just examples ones, make sure you understand the concept of directives and correct them.
    // Emit assembler directives.

    stream << ".text" << std::endl;
    stream << ".globl " << declarator_->getIdentifier() << std::endl;

    Specifier return_type = declaration_specifier_->getType(context);
    context.enterFunction(return_type);

    declarator_->EmitRISC(stream, destReg, context);

    int returnReg;
    switch (return_type){
        case Specifier::_int:
            returnReg = 10;
            break;
        case Specifier::_float:
        case Specifier::_double:
            returnReg = 42;
            break;
        default: throw std::runtime_error("Type not recognised in FunctionDefintion");
    }

    if (compound_statement_ != nullptr){
        // todo: potentially fix this, saving automatically into register a0
        compound_statement_->EmitRISC(stream, returnReg, context);
    }
    
    stream << context.getFunctionEndLabel() << ":" << std::endl;
    stream << "ret" << std::endl;
    context.exitFunction();
}

void FunctionDefinition::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";

    declarator_->Print(stream);
    stream << " {" << std::endl;

    if (compound_statement_ != nullptr)
    {
        compound_statement_->Print(stream);
    }
    stream << "}" << std::endl;
}
