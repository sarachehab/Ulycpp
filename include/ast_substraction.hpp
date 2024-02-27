#ifndef AST_SUBSTRACTION_HPP
#define AST_SUBSTRACTION_HPP

#include "ast_node.hpp"
#include <map>
#include <vector>
#include <string>


class Substraction : public Node
{
private:
    Node *left_;
    Node *right_;

public:
    Substraction(Node *left, Node *right) : left_(left), right_(right){};
    ~Substraction(){
        delete left_;
        delete right_;
    };
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


#endif
