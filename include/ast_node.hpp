#ifndef AST_NODE_HPP
#define AST_NODE_HPP

#include <iostream>
#include <vector>

#include "context.hpp"

class Node {
protected:
    std::vector<Node *> branches_;

public:
    Node(){};
    virtual ~Node();

    virtual Specifier getType(Context& context) const;

    virtual std::string getIdentifier() const;
    virtual void PushBack(Node* item);
    virtual int fetchVariable(Context &context) const;

    virtual std::string getNodeType() const;
    virtual std::vector<Node *> getNodes() const;

    virtual void EmitCondition(std::ostream &stream, int destReg, Context &context) const;

    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const = 0;
    virtual void Print(std::ostream &stream) const = 0;
};

// Represents a list of nodes.
class NodeList : public Node {
protected:
    std::vector<Node *> nodes_;

public:
    NodeList(Node *first_node) : nodes_({first_node}) {}

    ~NodeList() {
        for (auto node : nodes_) {
            delete node;
        }
    }

    std::string getNodeType() const override;

    std::vector<Node *> getNodes() const override;

    virtual void EmitCondition(std::ostream &stream, int destReg, Context &context) const;

    void PushBack(Node *item) override;
    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    virtual void Print(std::ostream &stream) const override;
};


class EmptyNode : public Node {
public:
    EmptyNode(){}
    ~EmptyNode(){}

    virtual void EmitRISC(std::ostream &stream, int destReg, Context &context) const override {}
    virtual void Print(std::ostream &stream) const override {}
};


#endif
