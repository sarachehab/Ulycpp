#ifndef AST_ARITHMETIC_HPP
#define AST_ARITHMETIC_HPP

#include "ast_binary_operation.hpp"


class Addition : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Addition(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class Substraction : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Substraction(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class Multiplication : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Multiplication(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class Division : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Division(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class Modulus : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Modulus(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


#endif