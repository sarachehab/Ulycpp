#ifndef AST_COMPARAISON_HPP
#define AST_COMPARAISON_HPP

#include "../ast_node.hpp"
#include "ast_binary_operation.hpp"


class Comparaison : public BinaryOperation {
public:
    using BinaryOperation::BinaryOperation;
    ~Comparaison(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction(Specifier type) const override = 0;

    Specifier getType(Context& context) const override;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
};

class EqualCheck : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~EqualCheck(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction(Specifier type) const override = 0;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
};


class CompositeComparaison : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~CompositeComparaison(){}

    virtual std::string getOperation() const override = 0;
    virtual std::string getInstruction(Specifier type) const override = 0;

    void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
};


class LessThan : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~LessThan(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class LessThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    ~LessThanEqual(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class GreaterThan : public Comparaison {
public:
    using Comparaison::Comparaison;
    ~GreaterThan(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class GreaterThanEqual : public CompositeComparaison {
public:
    using CompositeComparaison::CompositeComparaison;
    ~GreaterThanEqual(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class Equal : public EqualCheck {
public:
    using EqualCheck::EqualCheck;
    ~Equal(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};


class NotEqual : public EqualCheck {
public:
    using EqualCheck::EqualCheck;
    ~NotEqual(){}
    std::string getOperation() const override;
    std::string getInstruction(Specifier type) const override;
};

#endif
