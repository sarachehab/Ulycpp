#ifndef AST_CONSTANT_HPP
#define AST_CONSTANT_HPP

#include "ast_node.hpp"

class Constant : public Node {
private:
    int value_;
    Specifier type_;

public:
    Constant(){}
    ~Constant(){}

    virtual Specifier getType(Context &context) const override = 0;
    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const override = 0;
    void Print(std::ostream &stream) const override;
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
};

class FloatConstant : public Constant {
private:
    double value_;

public:
    FloatConstant(double value) 
        : value_(value)
    {}
    ~FloatConstant(){}

    Specifier getType(Context &context) const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
};

#endif
