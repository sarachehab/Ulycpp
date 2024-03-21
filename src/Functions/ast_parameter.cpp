#include "../../include/Functions/ast_parameter.hpp"

Specifier Parameter::getType(Context& context) const {
    return declaration_specifier_->getType(context);
}

void Parameter::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = getType(context);
    int memory_cells_allocated = SpecifierSize[type];
    int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);

    std::string identifier = init_declarator_list_->getIdentifier();

    context.addVariable(identifier, memory_cells_allocated, -memory_offset, type, -1);
    stream << context.getStoreInstruction(type) << " " << context.getRegisterName(destReg) << ", " << -memory_offset << "(s0)" << std::endl;

}


void Parameter::Print(std::ostream &stream) const {
    declaration_specifier_->Print(stream);
    stream << " ";
    init_declarator_list_->Print(stream);
}

// TODO: modify to support floats, argReg hardcoded
void ParametersList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int argRegInt = 10, argRegFloat = 42;
    
    for (auto parameter : nodes_){

        // choose argument register in function of type
        switch (parameter->getType(context)){
            case Specifier::_int:
            case Specifier::_unsigned:
            case Specifier::_char:
                parameter->EmitRISC(stream, argRegInt++, context);
                break;
            case Specifier::_float:
            case Specifier::_double:
                parameter->EmitRISC(stream, argRegFloat++, context);
                break;
            default: throw std::runtime_error("unrecognised type in ParametersList");
        }

        if (argRegInt > 17 && argRegFloat > 57) {
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

