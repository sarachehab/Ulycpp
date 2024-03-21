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
        // bool isArray = declaration->isArray();

        int memory_offset, srcReg, number_elements = 1;

        Assignment* assignment_ = dynamic_cast<Assignment*>(declaration);

        switch (declaration->defineVarType()) {

            case ProgramVarType::_unique:

                memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
                if (assignment_ == nullptr) {
                    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, declaration->getVarScope(), ProgramVarType::_unique, -1);
                } else {
                    srcReg = context.allocateRegister(type);
                    context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, declaration->getVarScope(), ProgramVarType::_unique, srcReg);
                    declaration->EmitRISC(stream, destReg, context);
                }
                break;
                
            case ProgramVarType::_array:
                number_elements = declaration->getSize();

                if (number_elements == -1) { // assume initializer list exists
                    number_elements = assignment_->getSize();
                }

                memory_offset = context.increaseCurrentStackSize(number_elements*memory_cells_allocated);

                if (assignment_ == nullptr) {
                    context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, declaration->getVarScope(), ProgramVarType::_array, -1);
                } else {
                    std::runtime_error("Initialiser list not implement in Declaration.cpp");
                }
                break;

            default: std::runtime_error("VarType not recognised in Declaration.cpp");
        }
    }
}


void Declaration::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_list_->Print(stream);
    stream << ";" << std::endl;
}
