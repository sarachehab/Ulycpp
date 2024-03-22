#include "ast_declaration.hpp"
#include "ast_assignment.hpp"
#include "Arrays/ast_array_initializer.hpp"

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
                    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, Specifier::_not_specified, declaration->getVarScope(), ProgramVarType::_unique, -1);
                } else {
                    srcReg = context.allocateRegister(type);
                    context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, Specifier::_not_specified, declaration->getVarScope(), ProgramVarType::_unique, srcReg);
                    declaration->EmitRISC(stream, destReg, context);
                }
                break;
                
            case ProgramVarType::_array:
                number_elements = declaration->getSize();
                memory_offset = context.increaseCurrentStackSize(number_elements*memory_cells_allocated);

                if (assignment_ != nullptr) {
                    Node* to_assign = assignment_->getValToAssign();
                    ArrayList* InitList = dynamic_cast<ArrayList*>(to_assign);

                    if (number_elements == -1){
                        number_elements = InitList->getSize();
                    }
                    
                    for (int i = 0; i < InitList->getSize(); i++){
                        srcReg = context.allocateRegister(type);
                        stream << "li " << context.getRegisterName(srcReg) << ", " << InitList->getElement(i) << std::endl;
                        stream << context.getStoreInstruction(type) << ", " << i*SpecifierSize[type] - memory_offset  << "(s0)" << std::endl;
                    }
                }

                context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, type, Specifier::_not_specified, declaration->getVarScope(), ProgramVarType::_array, -1);
                break;
            
            case ProgramVarType::_pointer:
                memory_cells_allocated = SpecifierSize[Specifier::_int];
                memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);

                if (assignment_ != nullptr) {
                    context.addVariable(identifier, memory_cells_allocated, -memory_offset, Specifier::_int, type, declaration->getVarScope(), ProgramVarType::_pointer, -1);
                } else {
                    std::cerr << "initialization of pointer not supported yet" << std::endl;
                    srcReg = context.allocateRegister(type);
                    context.addVariable(identifier, memory_cells_allocated*number_elements, -memory_offset, Specifier::_int, type, declaration->getVarScope(), ProgramVarType::_pointer, srcReg);
                    declaration->EmitRISC(stream, destReg, context);
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
