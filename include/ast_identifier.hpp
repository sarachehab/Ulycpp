#ifndef AST_IDENTIFIER_HPP
#define AST_IDENTIFIER_HPP

#include "ast_node.hpp"

class Identifier : public Node
{
private:
    std::string identifier_;
    bool fetch_;

public:
    Identifier(const std::string* identifier, bool fetch)
    : identifier_(*identifier)
    , fetch_(fetch)
    { delete identifier; };

    ~Identifier(){};

    std::string getIdentifier() const override;
    int fetchVariable(Context &context) const override;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
