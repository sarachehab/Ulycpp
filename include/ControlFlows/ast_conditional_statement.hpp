#ifndef AST_CONDITIONAL_STATEMENT_HPP
#define AST_CONDITIONAL_STATEMENT_HPP

#include "../ast_node.hpp"

class ConditionalStatement : public Node {

protected:
    Node* condition_;
    Node* body_true_;
    Node* body_false_;

public:

    ConditionalStatement(Node* condition, Node* body_true)
        : condition_(condition)
        , body_true_ (body_true)
        , body_false_ (nullptr)
    {}
    ConditionalStatement(Node* condition, Node* body_true, Node* body_false)
        : condition_(condition)
        , body_true_(body_true)
        , body_false_(body_false)
    {}

    ~ConditionalStatement() {
        delete condition_;
        delete body_true_;
        delete body_false_;
    }

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override = 0;
    virtual void Print(std::ostream &stream) const override = 0;
};


class IfStatement : public ConditionalStatement {
public:
    using ConditionalStatement::ConditionalStatement;
    ~IfStatement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class IfElseStatement : public ConditionalStatement {
public:
    using ConditionalStatement::ConditionalStatement;
    ~IfElseStatement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
