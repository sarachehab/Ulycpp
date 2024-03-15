#include "../../include/ControlFlows/ast_transfer_control.hpp"
#include "../../include/ast_node.hpp"

void BreakStatement::EmitRISC(std::ostream &stream, int destReg, Context& context) const {
    stream << "j " << context.getEndLabel() << std::endl;
}

void BreakStatement::Print(std::ostream &stream) const {
    stream << "break;" << std::endl;;
}

void ContinueStatement::EmitRISC(std::ostream &stream, int destReg, Context& context) const {
    stream << "j " << context.getStartLabel() << std::endl;
}


void ContinueStatement::Print(std::ostream &stream) const {
    stream << "continue;" << std::endl;
}
