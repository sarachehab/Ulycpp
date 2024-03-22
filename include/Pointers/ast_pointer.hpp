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

    int fetchVariable(Context &context) const override;

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

class AddressOf : public Node {
protected:
    Node* variable_;

public:
    AddressOf(Node* variable)
        : variable_(variable)
    {}
    ~AddressOf(){
        delete variable_;
    }

    int fetchVariable(Context &context) const override;

    std::string getIdentifier() const;

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
};

#endif