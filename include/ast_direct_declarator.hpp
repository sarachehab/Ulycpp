#ifndef AST_DIRECT_DECLARATOR_HPP
#define AST_DIRECT_DECLARATOR_HPP

#include "ast_node.hpp"
#include "ast_parameter.hpp"

class DirectDeclarator : public Node
{
private:
    Node *identifier_;
    Node *parameter_list_;

public:
    DirectDeclarator(Node *identifier)
        : identifier_(identifier)
        , parameter_list_(nullptr)
    {};
    DirectDeclarator(Node *identifier, Node *parameter_list_)
        : identifier_(identifier)
        , parameter_list_(parameter_list_)
    {};
    ~DirectDeclarator()
    {
        delete identifier_;
        delete parameter_list_;
    };

    std::string getIdentifier() const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
