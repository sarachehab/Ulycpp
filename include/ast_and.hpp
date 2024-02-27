#ifndef AST_AND_HPP
#define AST_AND_HPP

#include "ast_node.hpp"
#include <map>
#include <vector>
#include <string>


class And : public Node
{
private:
    Node *left_;
    Node *right_;

public:
    And(Node *left, Node *right) : left_(left), right_(right){};
    ~And(){
        delete left_;
        delete right_;
    };
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


#endif
