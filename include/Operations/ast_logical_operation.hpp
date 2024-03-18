#ifndef AST_LOGICAL_OPERATION_HPP
#define AST_LOGICAL_OPERATION_HPP

#include "../ast_node.hpp"
#include "ast_binary_operation.hpp"
#include "ast_unary_operation.hpp"

class LogicalOperation : public BinaryOperation {

public:
    using BinaryOperation::BinaryOperation;
    ~LogicalOperation(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction(Specifier type) const override = 0;

    Specifier getType(Context& context) const override;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class Negate : public UnaryOperation {
public:
    using UnaryOperation::UnaryOperation;
    ~Negate(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class LogicalAnd : public LogicalOperation {
public:
    using LogicalOperation::LogicalOperation;
    ~LogicalAnd(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class LogicalOr : public LogicalOperation {
public:
    using LogicalOperation::LogicalOperation;
    ~LogicalOr(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


#endif
