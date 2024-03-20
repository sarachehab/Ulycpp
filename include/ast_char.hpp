#ifndef AST_CHAR_HPP
#define AST_CHAR_HPP

#include "ast_node.hpp"

class Character : public Node {
private:
    int value_;

public:
    Character(int value)
        : value_(value)
    {}
    ~Character(){}

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};

#endif