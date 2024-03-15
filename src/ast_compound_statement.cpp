#include "ast_compound_statement.hpp"
#include "context.hpp"


void CompoundStatement::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    context.enterScope(context.getCurrentScopeSize());
    for (auto node : nodes_) {
        if (node == nullptr){
            continue;
        }
        node->EmitRISC(stream, destReg, context);
    }
    context.exitScope();
}
