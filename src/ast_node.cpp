#include "ast_node.hpp"

Node::~Node(){
    for (auto branch : branches_){
        delete branch;
    }
}

Specifier Node::getType() const {
    throw std::runtime_error("getType should not have been called (ast_node)");
}

std::string Node::getIdentifier() const {
    throw std::runtime_error("getIdentifier should not have been called (ast_node)");
}

void Node::PushBack(Node* item) {
    throw std::runtime_error("PushBack should not have been called (ast_node)");
}

int Node::fetchVariable(Context& context) const {
    throw std::runtime_error("fetchVariable should not have been called (ast_node)");
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
