#ifndef AST_SWITCH_HPP
#define AST_SWITCH_HPP

#include "../ast_node.hpp"

inline int case_number = 0;

class Switch : public Node {
protected:
    Node* condition_;
    Node* body_;

public: 
    Switch(Node* condition, Node* body)
        : condition_(condition)
        , body_(body)
    {}

    ~Switch() {
        delete condition_;
        delete body_;
    }

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

class Case : public Node {
protected:
    Node* condition_;
    Node* body_true_;
    std::string jump_label_;

public:
    Case(Node* condition, Node* body_true)
        : condition_(condition)
        , body_true_(body_true)
    {
        jump_label_ = "case_number" + std::to_string(case_number++);
    }
    Case(Node* body_true)
        : condition_(nullptr)
        , body_true_(body_true)
    {
        jump_label_ = "case_number" + std::to_string(case_number++);
    }

    ~Case() {
        delete condition_;
        delete body_true_;
    }

    virtual void EmitCondition(std::ostream &stream, int destReg, Context& context) const override;
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    virtual void Print(std::ostream &stream) const override;
};

class Default : public Case {
public:
    using Case::Case;
    ~Default() {}

    void EmitCondition(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

#endif