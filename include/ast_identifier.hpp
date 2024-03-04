#ifndef AST_IDENTIFIER_HPP
#define AST_IDENTIFIER_HPP

#include "ast_node.hpp"
class Identifier : public Node {
protected:
    std::string identifier_;

public:
    Identifier(const std::string* identifier)
    : identifier_(*identifier)
    { delete identifier; };

    ~Identifier(){};

    std::string getIdentifier() const override;
    virtual int fetchVariable(std::ostream &stream, Context &context) const override;

    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

class VariableIdentifier : public Identifier {
public:
    using Identifier::Identifier;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
};

#endif
