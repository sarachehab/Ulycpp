#include "../../include/Functions/ast_function_definition.hpp"

void FunctionDefinition::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    // TODO: these are just examples ones, make sure you understand the concept of directives and correct them.
    // Emit assembler directives.

    std::string function_identifier = declarator_->getIdentifier();

    stream << ".text" << std::endl;
    stream << ".globl " << function_identifier << std::endl;

    Specifier return_type = declaration_specifier_->getType(context);
    context.enterFunction(function_identifier, return_type);

    stream << function_identifier << ":" << std::endl;

    int stack_size = 1024; // todo: review this, count number of declarations
    stream << "addi sp, sp, " << -stack_size << std::endl;
    stream << "sw ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "sw s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "addi s0, sp, " << stack_size << std::endl;

    declarator_->EmitRISC(stream, destReg, context);

    int flowReg, returnReg;
    switch (return_type){
        case Specifier::_int:
        case Specifier::_unsigned:
        case Specifier::_char:
            flowReg = 15;
            returnReg = 10;
            break;
        case Specifier::_float:
        case Specifier::_double:
            flowReg = 47;
            returnReg = 42;
            break;
        default: throw std::runtime_error("Type not recognised in FunctionDefintion");
    }

    if (compound_statement_ != nullptr){
        // todo: potentially fix this, saving automatically into register a0
        compound_statement_->EmitRISC(stream, flowReg, context);
    }

    stream << context.getFunctionEndLabel() << ":" << std::endl;

    // footer of the function
    stream << "lw ra, " << stack_size - 4 << "(sp)" << std::endl;
    stream << "lw s0, " << stack_size - 8 << "(sp)" << std::endl;
    stream << "addi sp, sp, " << stack_size << std::endl;
    stream << context.getMoveInstruction(return_type) << " " << context.getRegisterName(returnReg) << ", " << context.getRegisterName(flowReg) << std::endl;
    stream << "ret" << std::endl;

    stream << ".section .rodata" << std::endl;

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
