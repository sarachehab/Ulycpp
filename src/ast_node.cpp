#include "ast_node.hpp"

Node::~Node(){
    for (auto branch : branches_){
        delete branch;
    }
}

Specifier Node::getType() const {
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

int Node::fetchVariable(std::ostream &stream, Context &context) const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("fetchVariable should not have been called (ast_node)");
}

std::string Node::getNodeType() const {
    return "Node";
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
