#ifndef AST_DECLARATION_DEFINITION_HPP
#define AST_DECLARATION_DEFINITION_HPP

#include "ast_node.hpp"

class Declaration : public Node {

protected:
    Node* declaration_specifier_;
    Node* init_declarator_list_;

public:
    Declaration () {
        std::runtime_error("Should not have called Declaration's default initializer (check ast_declaration.hpp)"); // there to define parameters later
    }
    Declaration (Node* declaration_specifier, Node* init_declarator_list)
        : declaration_specifier_(declaration_specifier)
        , init_declarator_list_(init_declarator_list)
    {}
    ~ Declaration() {
        delete declaration_specifier_;
        delete init_declarator_list_;
    }

    Specifier getType(Context& context) const override;
    std::string getIdentifier() const override;

    ExternalDeclarationType getExternalType() const override;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    virtual void Print(std::ostream &stream) const override;
};

#endif
