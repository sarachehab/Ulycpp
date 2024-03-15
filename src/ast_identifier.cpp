#include "ast_identifier.hpp"

std::string Identifier::getIdentifier() const {
    return identifier_;
};


int Identifier::fetchVariable(std::ostream &stream, Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_);

    if (variable_specs.reg == -1) {
        int allocated_register = context.allocateRegister(stream);
        variable_specs.reg = allocated_register;
    }

    context.updateVariableSpecs(identifier_, variable_specs);
    return variable_specs.reg;
}


void Identifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    stream << identifier_;
}


void Identifier::Print(std::ostream &stream) const {
    stream << identifier_;
}


void VariableIdentifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Variable variable_specs = context.getVariableSpecs(identifier_);

    // TODO: Load from register file if variable already there
    stream << "lw " << context.getRegisterName(destReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;
    variable_specs.reg = destReg; 

    context.updateVariableSpecs(identifier_, variable_specs);
}

