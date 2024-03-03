#include "ast_identifier.hpp"

std::string Identifier::getIdentifier() const {
    return identifier_;
};

int Identifier::fetchVariable(std::ostream &stream, Context &context) const {
    throw std::runtime_error ("tried to fetchVariable in ast_identifier");
}


int VariableIdentifier::fetchVariable(std::ostream &stream, Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_);

    if (variable_specs.reg == -1) {
        int allocated_register = context.allocateRegister(stream);
        context.useRegister(allocated_register);
        variable_specs.reg = allocated_register;
    }

    context.updateVariableSpecs(identifier_, variable_specs);
    return variable_specs.reg;
}


void FunctionIdentifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    stream << identifier_;
}

void VariableIdentifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Variable variable_specs = context.getVariableSpecs(identifier_);

    if (variable_specs.reg != -1) {
        context.freeUpRegister(variable_specs.reg);
    }

    context.useRegister(destReg); // todo change load to vary in function of size
    stream << "lw " << context.getRegisterName(destReg) << ", " << variable_specs.sp_offset << "(sp)" << std::endl;
    variable_specs.reg = destReg;

    context.updateVariableSpecs(identifier_, variable_specs);

}

void Identifier::Print(std::ostream &stream) const {
    stream << identifier_;
}
