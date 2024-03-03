#include "ast.hpp"


void Declaration::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = declaration_specifier_->getType();
    int memory_cells_allocated = SpecifierSize[type];
    std::string identifier = init_declarator_->getIdentifier();

    // adjust stack
    int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
    // stream << "addi sp, sp, " << -memory_cells_allocated << std::endl;

    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, -1);
}


void Declaration::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_->Print(stream);
    stream << ";" << std::endl;
}
