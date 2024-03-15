#include "../../include/Functions/ast_parameter.hpp"

void Parameter::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = declaration_specifier_->getType();
    int memory_cells_allocated = SpecifierSize[type];
    int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);

    std::string identifier = init_declarator_list_->getIdentifier();

    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, -1);
    stream << "sw " << context.getRegisterName(destReg) << ", " << -memory_offset << "(sp)" << std::endl;

}


void Parameter::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_list_->Print(stream);
}


void ParametersList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int argReg = 10;
    for (auto parameter : nodes_){
        parameter->EmitRISC(stream, argReg++, context);
        if (argReg > 17) {
            std::runtime_error("Have not implemented functions taking more than 7 arguments. Check ast_parameters.cpp");
        }
    }
}

void ParametersList::Print(std::ostream& stream) const {
    for (auto parameter : nodes_){
        parameter->Print(stream);
        stream << ", "; // todo: fix this, currenyly printing , for last parameter
    }
}

