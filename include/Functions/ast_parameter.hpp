#ifndef AST_PARAMETER_HPP
#define AST_PARAMETER_HPP

#include "../ast_node.hpp"
#include "../ast_declaration.hpp"

class Parameter : public Declaration {

public:
    using Declaration::Declaration;
    ~Parameter() {}

    Specifier getType (Context& context) const;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


class ParametersList : public NodeList {

public:
    using NodeList::NodeList;
    ~ParametersList(){}

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
