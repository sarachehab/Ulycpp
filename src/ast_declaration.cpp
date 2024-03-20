#include "ast_declaration.hpp"
#include "ast_assignment.hpp"

Specifier Declaration::getType(Context& context) const {
    return declaration_specifier_->getType(context);
}

ExternalDeclarationType Declaration::getExternalType() const {
    auto desired_declaration = init_declarator_list_->getNodes();
    return desired_declaration[0]->getExternalType();
}

std::string Declaration::getIdentifier() const {
    auto desired_declaration = init_declarator_list_->getNodes();
    return desired_declaration[0]->getIdentifier();
}


void Declaration::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = declaration_specifier_->getType(context);
    int memory_cells_allocated = SpecifierSize[type];

    for (auto declaration : init_declarator_list_->getNodes()) {
        std::string identifier = declaration->getIdentifier();
        bool isArray = declaration->isArray();

        int number_elements = 1;

        if (isArray){
            number_elements = declaration->getSize();

            // if size not defined, assume size of array is size of initializer
            if (number_elements == -1) {
                number_elements = 1; // TODO: Fix this
            }
        }

        // adjust stack
        int memory_offset = context.increaseCurrentStackSize(number_elements*memory_cells_allocated);

        Assignment* assignment_ = dynamic_cast<Assignment*>(declaration);
        if (assignment_ == nullptr){
            context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, -1);
        } else {
            
            if (isArray){
                int init_list_size = assignment_->getSize();
                for (int i = 0; i < init_list_size; i++){
                    int srcReg = context.allocateRegister(type);
                    context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset+i*memory_cells_allocated, type, srcReg);
                    // TODO: complete
                }
            }
            else {
                int srcReg = context.allocateRegister(type);
                context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, srcReg);
                declaration->EmitRISC(stream, destReg, context);
            }
        }
    }
}


void Declaration::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_list_->Print(stream);
    stream << ";" << std::endl;
}
