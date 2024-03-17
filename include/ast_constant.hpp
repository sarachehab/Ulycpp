#ifndef AST_CONSTANT_HPP
#define AST_CONSTANT_HPP

#include "ast_node.hpp"

class Constant : public Node {

public:
    Constant(){}
    ~Constant(){}

    virtual Specifier getType(Context &context) const override = 0;
    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const override = 0;
    void Print(std::ostream &stream) const override = 0;
};

class IntConstant : public Constant {
private:
    int value_;

public:
    IntConstant(int value) 
        : value_(value)
    {}
    ~IntConstant(){}

    Specifier getType(Context &context) const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

class FloatConstant : public Constant {
private:
    float value_;

public:
    FloatConstant(float value) 
        : value_(value)
    {}
    ~FloatConstant(){}

    Specifier getType(Context &context) const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
