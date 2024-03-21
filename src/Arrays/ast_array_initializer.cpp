#include "../../include/Arrays/ast_array_initializer.hpp"

int ArrayList::getSize() const {
    int size = 0;
    for (auto element : nodes_){
        size += 1;
    }
    return size;
}

Node* ArrayList::getElement(int index) const {
    return nodes_[index];
}

void ArrayList::EmitRISC(std::ostream &stream, int destReg, Context &context) const {}

void ArrayList::Print(std::ostream &stream) const {
    stream << "{";
    for (auto element : nodes_){
        element->Print(stream);
        stream << ", ";
    }
    stream << "}";
}