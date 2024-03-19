#ifndef ARRAY_DECLARATION_HPP
#define ARRAY_DECLARATION_HPP

#include "../ast_node.hpp"

class ArrayDeclaration : public Node {
private:
    Node* direct_declarator_;
    Node* constant_expression_;

public:
    ArrayDeclaration(Node* direct_declarator, Node* constant_expression)
        : direct_declarator_(direct_declarator)
        , constant_expression_(constant_expression)
    {}
    ArrayDeclaration(Node* direct_declarator)
        : direct_declarator_(direct_declarator)
        , constant_expression_(nullptr)
    {}

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};

#endif