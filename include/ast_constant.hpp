#ifndef AST_CONSTANT_HPP
#define AST_CONSTANT_HPP

#include "ast_node.hpp"

class IntConstant : public Node
{
private:
    int value_;

public:
    IntConstant(int value) : value_(value) {}
    ~IntConstant(){}

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
