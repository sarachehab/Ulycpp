#ifndef AST_COMPARAISON_HPP
#define AST_COMPARAISON_HPP

#include "../ast_node.hpp"
#include "ast_binary_operation.hpp"


class Comparaison : public BinaryOperation {

public:
    using BinaryOperation::BinaryOperation;
    ~Comparaison(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction() const override = 0;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class CompositeComparaison : public BinaryOperation {

public:
    using BinaryOperation::BinaryOperation;
    ~CompositeComparaison(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction() const override = 0;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    void Print(std::ostream &stream) const override;
};


class LessThan : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~LessThan(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class LessThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    ~LessThanEqual(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class GreaterThan : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~GreaterThan(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class GreaterThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    ~GreaterThanEqual(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class Equal : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~Equal(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};


class NotEqual : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~NotEqual(){}
    std::string getOperation() const override;
    std::string getInstruction() const override;
};

#endif
