#ifndef AST_WHILE_LOOP_HPP
#define AST_WHILE_LOOP_HPP

#include "../ast_node.hpp"

class Loop : public Node {

protected:
    Node* condition_;
    Node* body_true_;
    Node* initializer_;
    Node* increment_;

public:

    Loop(Node* condition, Node* body_true)
        : condition_(condition)
        , body_true_(body_true)
        , initializer_(nullptr)
        , increment_(nullptr)
    {}

    Loop(Node* initializer, Node* condition, Node* body_true)
        : condition_(condition)
        , body_true_(body_true)
        , initializer_(initializer)
        , increment_(nullptr)
    {}

    Loop(Node* initializer, Node* condition, Node* increment, Node* body_true)
        : condition_(condition)
        , body_true_(body_true)
        , initializer_(initializer)
        , increment_(increment)
    {}

    ~Loop() {
        delete condition_;
        delete body_true_;
        delete initializer_;
        delete increment_;
    }

    virtual void EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const = 0;

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    virtual void Print(std::ostream &stream) const override = 0;
};


class ForLoop : public Loop {
public:
    using Loop::Loop;
    ~ForLoop(){}
    void EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class WhileLoop : public Loop {
public:
    using Loop::Loop;
    ~WhileLoop(){}
    void EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

class DoWhileLoop : public Loop {
public:
    using Loop::Loop;
    ~DoWhileLoop(){}
    void EmitLoop(std::ostream &stream, int destReg, int conditionReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
