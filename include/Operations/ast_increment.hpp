#ifndef AST_INCREMENT_HPP
#define AST_INCREMENT_HPP

#include "../ast_node.hpp"

class Increment : public Node {

protected:
    Node* value_;

public:

    Increment(Node* value)
        : value_(value)
    {}

    ~Increment(){
        delete value_;
    }

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override = 0;
    virtual void Print(std::ostream &stream) const override = 0;
};


class RightIncrement : public Increment {
public:
    using Increment::Increment;
    ~RightIncrement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class RightDecrement : public Increment {
public:
    using Increment::Increment;
    ~RightDecrement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

class LeftIncrement : public Increment {
public:
    using Increment::Increment;
    ~LeftIncrement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

class LeftDecrement : public Increment {
public:
    using Increment::Increment;
    ~LeftDecrement(){}
    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

#endif