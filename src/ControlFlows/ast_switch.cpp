#include "../../include/ControlFlows/ast_switch.hpp"

void Switch::EmitRISC(std::ostream &stream, int destReg, Context& context) const {
    std::string end_switch_label = context.createLabel("end_switch"); 
    context.pushLabels("", end_switch_label);

    // checking conditions
    condition_->EmitRISC(stream, destReg, context);
    NodeList* cases = dynamic_cast<NodeList*>(body_);

    cases->EmitCondition(stream, destReg, context);
    
    // printing body
    if (cases != nullptr) {
        cases->EmitRISC(stream, destReg, context);
    }
    
    stream << end_switch_label << ":" << std::endl;
    context.popLabels();
}

void Switch::Print(std::ostream &stream) const {
    stream << "Switch(";
    condition_->Print(stream);
    stream << ") {";
    body_->Print(stream);
    stream << std::endl << " } " << std::endl;
}

void Case::EmitCondition(std::ostream &stream, int destReg, Context& context) const {
    int conditionReg = context.allocateRegister(Specifier::_int);
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "beq " << context.getRegisterName(conditionReg) << ", " << context.getRegisterName(destReg) << ", " << jump_label_ << std::endl;
    context.freeUpRegister(conditionReg);
}

void Default::EmitCondition(std::ostream &stream, int destReg, Context& context) const {
    stream << "j " << jump_label_ << std::endl;
}


void Case::EmitRISC(std::ostream &stream, int destReg, Context& context) const {
    stream << jump_label_ << ":" << std::endl;
    body_true_->EmitRISC(stream, destReg, context);
}

void Case::Print(std::ostream &stream) const {
    stream << "Case(";
    condition_->Print(stream);
    stream << ") {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;
}

void Default::Print(std::ostream &stream) const {
    stream << "Default: {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;  
}
