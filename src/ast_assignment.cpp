#include "ast_assignment.hpp"

std::string Assignment::getIdentifier() const {
    return target_variable_->getIdentifier();
}

void Assignment::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = target_variable_->fetchVariable(context);
    
    Specifier type = target_variable_->getType(context);
    int memory_cells_allocated = SpecifierSize[type];
    context.setOperationType(type);

    int i = target_variable_->getCurrentIndex();

    value_to_assign_->EmitRISC(stream, srcReg, context);
    stream << context.getStoreInstruction(type) << " " << context.getRegisterName(srcReg) << ", " << 
        i * memory_cells_allocated + context.getVariableSpecs(target_variable_->getIdentifier()).sp_offset 
            << "(s0)" << std::endl;
    // TODO: check previous line

    // housekeeping, spill computed value to memory
    Variable variable_specs = context.getVariableSpecs(target_variable_->getIdentifier());
    variable_specs.reg = -1;
    context.freeUpRegister(srcReg);
    context.updateVariableSpecs(target_variable_->getIdentifier(), variable_specs);
}

void Assignment::Print(std::ostream &stream) const {
    stream << target_variable_->getIdentifier() << " = ";
    value_to_assign_->Print(stream);
    stream << ";" << std::endl;
}
