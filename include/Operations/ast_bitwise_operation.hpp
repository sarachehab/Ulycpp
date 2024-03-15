#ifndef AST_BITWISE_HPP
#define AST_BITWISE_HPP

#include "ast_binary_operation.hpp"
#include "ast_unary_operation.hpp"


class InclusiveOr : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~InclusiveOr(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class ExclusiveOr : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~ExclusiveOr(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class And : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~And(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class LeftShift : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~LeftShift(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class RightShift : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~RightShift(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class OneComplement : public UnaryOperation {
public:
    using UnaryOperation::UnaryOperation;
    ~OneComplement(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};




#endif