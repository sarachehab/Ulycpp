#ifndef BINARY_OPERATION_HPP
#define BINARY_OPERATION_HPP

#include "../ast_node.hpp"

class BinaryOperation : public Node {

protected:
    Node* left_;
    Node* right_;

public:

    BinaryOperation(Node* left, Node* right)
        : left_(left)
        , right_(right)
    {}

    ~BinaryOperation(){
        delete left_;
        delete right_;
    }

    virtual std::string getOperation() const = 0;
    virtual std::string getInstruction(Specifier type) const = 0;

    Specifier getType(Context& context) const;

    void HandlePointers(std::ostream& stream, Node* operand_, int destReg, int op1Reg, int op2Reg, Specifier type, Context& context) const;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


#endif
