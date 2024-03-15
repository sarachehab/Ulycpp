#include "../../include/Functions/ast_function_definition.hpp"

void FunctionDefinition::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    // TODO: these are just examples ones, make sure you understand the concept of directives and correct them.
    // Emit assembler directives.
    stream << ".text" << std::endl;
    stream << ".globl " << declarator_->getIdentifier() << std::endl;

    int stack_size = 1024; // todo: review this

    context.enterFunction();

    stream << declarator_->getIdentifier() << ":" << std::endl;

    // header of the function
    stream << "addi " << "sp, " << "sp " << -stack_size << std::endl;
    stream << "sw " << "ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "sw " << "s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "addi " << "s0, " << "sp, " << stack_size << std::endl;

    declarator_->EmitRISC(stream, destReg, context);

    if (compound_statement_ != nullptr){
        // todo: potentially fix this, saving automatically into register a0
        compound_statement_->EmitRISC(stream, destReg, context);
    }

    stream << context.getFunctionEndLabel() << ":" << std::endl;
    stream << "ret" << std::endl;
    context.exitFunction();

    // footer of the function
    stream << "lw " << "ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "lw " << "s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "addi " << "sp, " << "sp " << stack_size << std::endl;
    stream << "jr " << "ra" << std::endl;

}

void FunctionDefinition::Print(std::ostream &stream) const {
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
