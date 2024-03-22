#ifndef AST_POINTER_HPP
#define AST_POINTER_HPP

#include "../ast_node.hpp"

class Pointer : public Node {
protected:
    Node* address_;

public:
    Pointer(Node* address) 
        : address_(address) 
    {}

    ~Pointer() {
        delete address_;
    }

    std::string getIdentifier() const override;

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};


class PointerDereference : public Pointer {

public:
    using Pointer::Pointer;

    ~PointerDereference() {}

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
};

#endif