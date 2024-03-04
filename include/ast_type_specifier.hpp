#ifndef AST_TYPE_SPECIFIER
#define AST_TYPE_SPECIFIER

#include "ast_node.hpp"
class TypeSpecifier : public Node
{
private:
    std::string type_;

public:
    TypeSpecifier(std::string type) : type_(type){};
    ~TypeSpecifier(){};

    Specifier getType() const override;
    void EmitRISC(std::ostream &stream,  int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
