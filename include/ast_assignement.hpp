#ifndef AST_ASSIGNEMENT_HPP
#define AST_ASSIGNEMENT_HPP

#include "ast_node.hpp"

class Assignement : public Node {
private:
    Node* assigned_variable_;
    Node* value_to_assign_;
    bool declaration_;

public:
    Assignement(Node* assigned_variable, Node* value_to_assign, bool declaration)
        : assigned_variable_(assigned_variable)
        , value_to_assign_(value_to_assign)
        , declaration_(declaration)
    {}
    ~ Assignement () {
        delete assigned_variable_;
        delete value_to_assign_;
    }

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    virtual void Print(std::ostream &stream) const override;
};

#endif
