#ifndef ARRAY_INITIALIZER_HPP
#define ARRAY_INITIALIZER_HPP

#include "../ast_node.hpp"

class ArrayList : public NodeList {
public:
    using NodeList::NodeList;
    ~ ArrayList(){}

    int getSize() const override;
    Node* getElement(int index) const override;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif