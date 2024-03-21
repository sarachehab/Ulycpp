#include "../../include/Functions/ast_function_declaration.hpp"
#include "../../include/ast_declaration.hpp"

void ExternalDeclaration::EmitRISC(std::ostream& stream, int destReg, Context& context) const {

    Declaration* global_declaration_;

    switch(declaration_->getExternalType()){

        case(ExternalDeclarationType::_functions):
            context.declareExternalFunction(declaration_->getIdentifier(), declaration_->getType(context));
            break;

        case(ExternalDeclarationType::_global):
           
            global_declaration_ = dynamic_cast<Declaration*>(declaration_);
            int size, align;

            switch (global_declaration_->defineVarType()){
                case ProgramVarType::_unique:
                    size = SpecifierSize[global_declaration_->getType(context)];
                    break;
                case ProgramVarType::_array:
                    std::cerr << "defining global array" << std::endl;
                    size = SpecifierSize[global_declaration_->getType(context)] * global_declaration_->getSize();
                    break;
                default: throw std::runtime_error("Unrecognized ProgramVarType in ExternalDeclaration");
            }

            stream << ".globl " << global_declaration_->getIdentifier() << std::endl;
            stream << ".section .sdata, \"aw\"" << std::endl;
            stream << ".align " << SpecifierAlign[global_declaration_->getType(context)] << std::endl;
            stream << ".size " << global_declaration_->getIdentifier() << ", " << size << std::endl;

            stream << global_declaration_->getIdentifier() << ":" << std::endl;
            stream << ".zero " << size << std::endl;

            context.addVariable(global_declaration_->getIdentifier(), size, 0, global_declaration_->getType(context), 
                    VarScope::_global, global_declaration_->defineVarType(), -1);
            break;

        default: throw std::runtime_error("Unrecognised type in ExternalDeclaration");
    }
}

void ExternalDeclaration::Print(std::ostream& stream) const {
    declaration_->Print(stream);
    stream << std::endl;
}

VarScope ExternalDeclaration::getVarScope() const { return VarScope::_global; }


void InternalFunction::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    declaration_->EmitRISC(stream, destReg, context);
}
