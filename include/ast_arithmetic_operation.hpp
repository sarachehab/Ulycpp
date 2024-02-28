#ifndef AST_ARITHMETIC_HPP
#define AST_ARITHMETIC_HPP

#include "ast_binary_operation.hpp"
#include "ast_unary_operation.hpp"

class InclusiveOr : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class ExclusiveOr : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class And : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class LeftShift : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class RightShift : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Addition : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Substraction : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Multiplication : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Division : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Modulus : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class OneComplement : public UnaryOperation {
public:
    using UnaryOperation::UnaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class Negate : public UnaryOperation {
public:
    using UnaryOperation::UnaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

#endif
