#include "ast_function_definition.hpp"

void FunctionDefinition::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    // Emit assembler directives.
    // TODO: these are just examples ones, make sure you understand
    // the concept of directives and correct them.
    stream << ".text" << std::endl;
    stream << ".globl " << declarator_->getIdentifier() << std::endl;

    declarator_->EmitRISC(stream, destReg, context);

    if (compound_statement_ != nullptr){
        // todo: fix this, saving automatically into register r0
        compound_statement_->EmitRISC(stream, destReg, context);
    }
}

void FunctionDefinition::Print(std::ostream &stream) const
{
    declaration_specifiers_->Print(stream);
    stream << " ";

    declarator_->Print(stream);
    stream << " {" << std::endl;

    if (compound_statement_ != nullptr)
    {
        compound_statement_->Print(stream);
    }
    stream << "}" << std::endl;
}
