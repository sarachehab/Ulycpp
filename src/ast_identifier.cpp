#include "ast_identifier.hpp"

std::string Identifier::getIdentifier() const {
    return identifier_;
};

Specifier Identifier::getType(Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_);
    return variable_specs.type;
}

int Identifier::fetchVariable(Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_);

    if (variable_specs.reg == -1) {
        Specifier type = variable_specs.type;
        int allocated_register = context.allocateRegister(type);
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

    // choose adequate load instruction
    std::string load_instruction;

    // TODO: Load from register file if variable already there
    stream << context.getLoadInstruction(variable_specs.type) << " " << context.getRegisterName(destReg) << ", " << variable_specs.sp_offset << "(s0)" << std::endl;
    variable_specs.reg = destReg; 

    context.updateVariableSpecs(identifier_, variable_specs);
}