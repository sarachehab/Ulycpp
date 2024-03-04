#ifndef AST_PARAMETER_HPP
#define AST_PARAMETER_HPP

#include "ast_node.hpp"
#include "ast_declaration.hpp"

class Parameter : public Declaration {

public:
    using Declaration::Declaration;
    ~Parameter() {}

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


class ParametersList : public NodeList {

public:
    using NodeList::NodeList;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
