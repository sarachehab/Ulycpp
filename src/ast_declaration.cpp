#include "ast.hpp"


void Declaration::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    enum Specifier type = declaration_specifier_->getType(); // todo: implement in type_specifier
    int memory_cells_allocated = SpecifierSize[type];
    std::string identifier = init_declarator_->getIdentifier(); // todo: implement function in Identifier

    // adjust stack
    int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
    stream << "sub sp, sp, " << memory_cells_allocated << std::endl;

    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, destReg);
}


void Declaration::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_->Print(stream);
    stream << ";" << std::endl;
}
