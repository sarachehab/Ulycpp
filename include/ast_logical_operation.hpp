#ifndef AST_LOGICAL_OPERATION_HPP
#define AST_LOGICAL_OPERATION_HPP

#include "ast_node.hpp"
#include "ast_binary_operation.hpp"

class LogicalOperation : public BinaryOperation {

public:
    using BinaryOperation::BinaryOperation;

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction() const override = 0;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


#endif
