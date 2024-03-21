#ifndef ARRAY_DECLARATION_HPP
#define ARRAY_DECLARATION_HPP

#include "../ast_node.hpp"

class ArrayDeclarator : public Node {
private:
    Node* direct_declarator_;
    Node* constant_expression_;

public:
    ArrayDeclarator(Node* direct_declarator, Node* constant_expression)
        : direct_declarator_(direct_declarator)
        , constant_expression_(constant_expression)
    {}
    ArrayDeclarator(Node* direct_declarator)
        : direct_declarator_(direct_declarator)
        , constant_expression_(nullptr)
    {}

    ~ArrayDeclarator() {
        delete direct_declarator_;
        delete constant_expression_;
    }

    bool isArray() const override;
    int getSize() const override;
    std::string getIdentifier() const override;
    ProgramVarType defineVarType() const override;

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};

#endif