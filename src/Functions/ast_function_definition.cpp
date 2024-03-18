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
    stream << "addi sp, sp, " << -stack_size << std::endl;
    stream << "sw ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "sw s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "sw t0, " << stack_size - 12 << "(sp)" << std::endl;
    stream << "sw t1, " << stack_size - 16 << "(sp)" << std::endl;
    stream << "sw t2, " << stack_size - 20 << "(sp)" << std::endl;
    stream << "sw t3, " << stack_size - 24 << "(sp)" << std::endl;
    stream << "sw t4, " << stack_size - 28 << "(sp)" << std::endl;
    stream << "sw t5, " << stack_size - 32 << "(sp)" << std::endl;
    stream << "sw t6, " << stack_size - 36 << "(sp)" << std::endl;
    stream << "addi s0, sp, " << stack_size << std::endl;

    declarator_->EmitRISC(stream, destReg, context);

    if (compound_statement_ != nullptr){
        // todo: potentially fix this, saving automatically into register a0
        compound_statement_->EmitRISC(stream, 15, context);
    }

    stream << context.getFunctionEndLabel() << ":" << std::endl;
    context.exitFunction();

    // footer of the function
    stream << "lw ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "lw s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "lw t0, " << stack_size - 12 << "(sp)" << std::endl;
    stream << "lw t1, " << stack_size - 16 << "(sp)" << std::endl;
    stream << "lw t2, " << stack_size - 20 << "(sp)" << std::endl;
    stream << "lw t3, " << stack_size - 24 << "(sp)" << std::endl;
    stream << "lw t4, " << stack_size - 28 << "(sp)" << std::endl;
    stream << "lw t5, " << stack_size - 32 << "(sp)" << std::endl;
    stream << "lw t6, " << stack_size - 36 << "(sp)" << std::endl;
    stream << "addi sp, sp, " << stack_size << std::endl;
    stream << "mv " << context.getRegisterName(10) << ", " << context.getRegisterName(15) << std::endl;
    stream << "ret" << std::endl;

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
