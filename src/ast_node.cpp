#include "ast_node.hpp"

Node::~Node(){
    for (auto branch : branches_){
        delete branch;
    }
}

std::string Node::getNodeType() const {
    return "Node";
}

std::vector<Node *> NodeList::getNodes() const {
        return nodes_;
    }

ExternalDeclarationType Node::getExternalType() const {
    return ExternalDeclarationType::_global;
}

int Node::getCurrentIndex() const {
    return 0;
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


/* FUNCTIONS DEFINED HERE FOR THE SAKE OF SUBCLASSES */

bool Node::isArray() const { return false; }

int Node::getSize() const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getSize should not have been called (ast_node)");
}

int Node::getValue() const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getValue should not have been called (ast_node)");
}

Node* Node::getElement(int index) const {
    std::cerr << getNodeType() << std::endl;;
    throw std::runtime_error("getElement should not have been called (ast_node)");
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

VarScope Node::getVarScope() const { return VarScope::_local; }

ProgramVarType Node::defineVarType() const { return ProgramVarType::_unique; }