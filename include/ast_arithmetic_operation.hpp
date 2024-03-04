#ifndef AST_ARITHMETIC_HPP
#define AST_ARITHMETIC_HPP

#include "ast_binary_operation.hpp"
#include "ast_unary_operation.hpp"
#include "ast_composite_comparaison.hpp"
#include "ast_comparaison.hpp"
#include "ast_logical_operation.hpp"

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

class LessThan : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class LessThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class GreaterThan : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class GreaterThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class Equal : public Comparaison {
public:
    using Comparaison::Comparaison;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class NotEqual : public Comparaison {
public:
    using Comparaison::Comparaison;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class LogicalAnd : public LogicalOperation {
public:
    using LogicalOperation::LogicalOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

class LogicalOr : public LogicalOperation {
public:
    using LogicalOperation::LogicalOperation;
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


#endif
