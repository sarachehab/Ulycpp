#ifndef UNARY_OPERATION_HPP
#define UNARY_OPERATION_HPP

#include "../ast_node.hpp"

class UnaryOperation : public Node {

protected:
    Node* value_;

public:

    UnaryOperation(Node* value)
        : value_(value)
    {}

    ~UnaryOperation(){
        delete value_;
    }

    virtual std::string getOperation() const = 0;
    virtual std::string getInstruction(Specifier type) const = 0;

    Specifier getType(Context& context) const override;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
