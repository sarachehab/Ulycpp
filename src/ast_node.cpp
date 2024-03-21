#include "ast_node.hpp"

Node::~Node(){
    for (auto branch : branches_){
        delete branch;
    }
}

Specifier Node::getType(Context& context) const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getType should not have been called (ast_node)");
}

std::string Node::getIdentifier() const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getIdentifier should not have been called (ast_node)");
}

void Node::PushBack(Node* item) {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("PushBack should not have been called (ast_node)");
}

int Node::fetchVariable(Context &context) const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("fetchVariable should not have been called (ast_node)");
}

std::vector<Node *> Node::getNodes() const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getNodes should not have been called (ast_node)");
}

std::string Node::getNodeType() const {
    return "Node";
}

std::vector<Node *> NodeList::getNodes() const {
        return nodes_;
    }


void NodeList::PushBack(Node *item){
    nodes_.push_back(item);
}

void NodeList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    for (auto node : nodes_) {
        if (node == nullptr){
            continue;
        }
        node->EmitRISC(stream, destReg, context);
    }
}

void NodeList::Print(std::ostream &stream) const {
    for (auto node : nodes_){
        if (node == nullptr){
            continue;
        }
        node->Print(stream);
    }
}

std::string NodeList::getNodeType() const {
    return "NodeList";
}

void NodeList::EmitCondition(std::ostream &stream, int destReg, Context &context) const {
    for (auto node : nodes_) {
        if (node == nullptr){
            continue;
        }
        node->EmitCondition(stream, destReg, context);
    }
}

void Node::EmitCondition(std::ostream &stream, int destReg, Context &context) const {}