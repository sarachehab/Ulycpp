#ifndef AST_COMPOUND_STATEMENT_HPP
#define AST_COMPOUND_STATEMENT_HPP

#include "ast_node.hpp"

class CompoundStatement : public NodeList {

public:
    using NodeList::NodeList;
    ~CompoundStatement(){}

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
};


#endif
