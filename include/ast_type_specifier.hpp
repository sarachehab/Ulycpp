#ifndef AST_TYPE_SPECIFIER
#define AST_TYPE_SPECIFIER

#include "ast_node.hpp"
class TypeSpecifier : public Node
{
private:
    Specifier type_;

public:
    TypeSpecifier(Specifier type) : type_(type){};
    ~TypeSpecifier(){};

    Specifier getType(Context& context) const override;
    void EmitRISC(std::ostream &stream,  int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
