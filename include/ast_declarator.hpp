#ifndef DECLARATOR_HPP
#define DECLARATOR_HPP

#include "ast_node.hpp"

class Declarator : public Node {
public:
    std::string getIdentifier() const override = 0;
    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override = 0;
    void Print(std::ostream& stream) const override = 0;
};

#endif