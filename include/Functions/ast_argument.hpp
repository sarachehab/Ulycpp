#ifndef AST_ARGUMENTS_HPP
#define AST_ARGUMENTS_HPP

#include "../ast_node.hpp"
#include "../ast_declaration.hpp"


class ArgumentList : public NodeList
{
public:
    using NodeList::NodeList;
    ~ArgumentList(){}

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
