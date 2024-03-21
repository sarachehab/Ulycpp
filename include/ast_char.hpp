#ifndef AST_CHAR_HPP
#define AST_CHAR_HPP

#include "ast_node.hpp"

class Character : public Node {
private:
    std::string name_;
    int value_;

public:
    Character(std::string* name)
        : name_(*name), value_(0)
    { delete name; }
    ~Character(){}

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};

#endif