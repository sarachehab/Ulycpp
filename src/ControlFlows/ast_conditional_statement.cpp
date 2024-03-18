#include "../../include/ControlFlows/ast_conditional_statement.hpp"

void IfStatement::EmitRISC(std::ostream &stream, int destReg, Context& context) const {

    // creating labels
    std::string exit_label = context.createLabel("exit_conditional_statement");

    // evaluate condition
    int conditionReg = context.allocateRegister(Specifier::_int);
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "beqz " << context.getRegisterName(conditionReg) << ", " << exit_label << std::endl;
    context.freeUpRegister(conditionReg);

    // if branch statements
    context.enterScope(context.getCurrentScopeSize());
    body_true_->EmitRISC(stream, destReg, context);
    context.exitScope();

    // exit conditional
    stream << exit_label << ":" << std::endl;

}

void IfStatement::Print(std::ostream &stream) const {
    stream << "if (";
    condition_->Print(stream);
    stream << ") {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;
}


void IfElseStatement::EmitRISC(std::ostream &stream, int destReg, Context& context) const {

    // creating labels
    std::string else_label = context.createLabel("else_statement_jump");
    std::string exit_label = context.createLabel("exit_conditional_statement");

    // evaluate condition
    int conditionReg = context.allocateRegister(Specifier::_int);
    condition_->EmitRISC(stream, conditionReg, context);
    stream << "beqz " << context.getRegisterName(conditionReg) << ", " << else_label << std::endl;
    context.freeUpRegister(conditionReg);

    // if branch statements
    context.enterScope(context.getCurrentScopeSize());
    body_true_->EmitRISC(stream, destReg, context);
    context.exitScope();
    stream << "j " << exit_label << std::endl;

    // else branch statements
    stream << else_label << ":" << std::endl;
    context.enterScope(context.getCurrentScopeSize());
    body_false_->EmitRISC(stream, destReg, context);
    context.exitScope();

    // exit conditional statement
    stream << exit_label << ":" << std::endl;
}


void IfElseStatement::Print(std::ostream &stream) const {
    stream << "if (";
    condition_->Print(stream);
    stream << ") {";
    body_true_->Print(stream);
    stream << std::endl << " } " << std::endl;
    stream << "else {";
    body_false_->Print(stream);
    stream << std::endl << " } " << std::endl;
}
