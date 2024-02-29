#ifndef AST_DECLARATION_DEFINITION_HPP
#define AST_DECLARATION_DEFINTION_HPP

#include "ast_node.hpp"

class Declaration : public Node {

private:
    Node* declaration_specifier_;
    Node* init_declarator_;

public:
    Declaration (Node* declaration_specifier, Node* init_declarator)
        : declaration_specifier_(declaration_specifier)
        , init_declarator_(init_declarator)
    {}
    ~ Declaration() {
        delete declaration_specifier_;
        delete init_declarator_;
    }

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    virtual void Print(std::ostream &stream) const override;
};

#endif
