#include "ast_declaration.hpp"
#include "ast_assignement.hpp"


void Declaration::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = declaration_specifier_->getType();
    int memory_cells_allocated = SpecifierSize[type];

    for (auto declaration : init_declarator_list_->getNodes()) {
        std::string identifier = declaration->getIdentifier();

        // adjust stack
        int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
        // stream << "addi sp, sp, " << -memory_cells_allocated << std::endl;

        Assignement* assignement_ = dynamic_cast<Assignement*>(declaration);
        if (assignement_ == nullptr){
            context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, -1);
        } else {
            context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, destReg);
            declaration->EmitRISC(stream, destReg, context);
        }
    }
}


void Declaration::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_list_->Print(stream);
    stream << ";" << std::endl;
}
