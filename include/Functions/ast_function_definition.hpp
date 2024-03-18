#ifndef AST_FUNCTION_DEFINITION_HPP
#define AST_FUNCTION_DEFINITION_HPP

#include "../ast_node.hpp"

class FunctionDefinition : public Node
{
private:
    Node *declaration_specifier_;
    Node *declarator_;
    Node *compound_statement_;

public:
    FunctionDefinition(Node *declaration_specifier, Node *declarator, Node *compound_statement) : declaration_specifier_(declaration_specifier), declarator_(declarator), compound_statement_(compound_statement){};
    ~FunctionDefinition()
    {
        delete declaration_specifier_;
        delete declarator_;
        delete compound_statement_;
    };
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
