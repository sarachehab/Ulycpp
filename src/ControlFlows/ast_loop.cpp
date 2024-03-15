#include "../../include/ControlFlows/ast_loop.hpp"

void Loop::EmitRISC(std::ostream &stream, int destReg, Context& context) const {

    // creating labels and adding them to stack for breaks and continues
    std::string start_label = context.createLabel("enter_while_statement");
    std::string end_label = context.createLabel("exit_while_statement");
    context.pushLabels(start_label, end_label);

    // assigning register for condition checking
    int conditionReg = context.allocateRegister(stream);

    // defining new scope for loop
    context.enterScope(context.getCurrentScopeSize());

    EmitLoop(stream, destReg, conditionReg, context);

    // housekeeping
    context.freeUpRegister(conditionReg);
    context.exitScope();
    context.popLabels();

}

void WhileLoop::EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const {

    // retrieving start and end label from stack
    std::string start_label = context.getStartLabel();
    std::string end_label = context.getEndLabel();
    
    // re-evaluate condition eavery time we enter the loop
    stream << start_label << ":" << std::endl;
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "beqz " << context.getRegisterName(conditionReg) << ", " << end_label << std::endl;

    // while loop statement
    body_true_->EmitRISC(stream, destReg, context);

    stream << "j " << start_label << std::endl;

    // exit conditional
    stream << end_label << ":" << std::endl;
}

void WhileLoop::Print(std::ostream &stream) const {
    stream << "while (";
    condition_->Print(stream);
    stream << ") {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;
}

void DoWhileLoop::EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const { // TODO; Verify this

    // retrieving start and end label from stack
    std::string start_label = context.getStartLabel();
    std::string end_label = context.getEndLabel();
    
    stream << start_label << ":" << std::endl;

    // do while loop statement
    body_true_->EmitRISC(stream, destReg, context);

    // re-evaluate condition eavery time before we exit the loop
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "bnez " << context.getRegisterName(conditionReg) << ", " << start_label << std::endl;

    stream << end_label << ":" << std::endl;
}

void DoWhileLoop::Print(std::ostream &stream) const {
    stream << "do {" << std::endl;
    body_true_->Print(stream);
    stream << std::endl << " } while (";
    condition_->Print(stream);
    stream << ");" << std::endl;
}

void ForLoop::EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const {

    // retrieving start and end label from stack
    std::string incrementer_label = context.getStartLabel();
    std::string end_label = context.getEndLabel();

    std::string start_label = context.createLabel("for_condition_check");
    
    int incrementReg = context.allocateRegister(stream);

    initializer_->EmitRISC(stream, incrementReg, context);
    stream << start_label << ":" << std::endl;

    // condition check
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "beqz " << context.getRegisterName(conditionReg) << ", " << end_label << std::endl;

    // enter loop body
    body_true_->EmitRISC(stream, destReg, context);
    stream << incrementer_label << ":" << std::endl;
    increment_->EmitRISC(stream, incrementReg, context);

    stream << "j " << start_label << std::endl;

    stream << end_label << ":" << std::endl;

    // housekeeping
    context.freeUpRegister(incrementReg);
}


void ForLoop::Print(std::ostream &stream) const {
    stream << "for (";
    condition_->Print(stream);
    stream << ") {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;
}
