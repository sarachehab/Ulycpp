#include "ast_declaration.hpp"
#include "ast_assignment.hpp"


void Declaration::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = declaration_specifier_->getType(context);
    int memory_cells_allocated = SpecifierSize[type];

    for (auto declaration : init_declarator_list_->getNodes()) {
        std::string identifier = declaration->getIdentifier();

        // adjust stack
        int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
        // stream << "addi sp, sp, " << -memory_cells_allocated << std::endl;

        Assignment* assignment_ = dynamic_cast<Assignment*>(declaration);
        if (assignment_ == nullptr){
            context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, -1);
        } else {
            int srcReg = context.allocateRegister(type);
            context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, srcReg);
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
