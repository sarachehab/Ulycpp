#ifndef AST_TRANSFER_CONTROL_HPP
#define AST_TRANSFER_CONTROL_HPP

#include "../ast_node.hpp"


class ControlFlow : public Node {
public:
    ControlFlow(){}
    ~ControlFlow() {}

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override = 0;
    virtual void Print(std::ostream &stream) const override = 0;
};

class BreakStatement : public ControlFlow {

public:

    using ControlFlow::ControlFlow;

    ~BreakStatement() {}

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    virtual void Print(std::ostream &stream) const override;
};

class ContinueStatement : public ControlFlow {

public:

    using ControlFlow::ControlFlow;

    ~ContinueStatement() {}

    virtual void EmitRISC(std::ostream &stream, int destReg, Context& context) const override;
    virtual void Print(std::ostream &stream) const override;
};

#endif
