#ifndef AST_ADDITION_HPP
#define AST_ADDITION_HPP

#include "ast_node.hpp"
#include <map>
#include <vector>
#include <string>


class Addition : public Node
{
private:
    Node *left_;
    Node *right_;

public:
    Addition(Node *left, Node *right) : left_(left), right_(right){};
    ~Addition(){
        delete left_;
        delete right_;
    };
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


#endif
