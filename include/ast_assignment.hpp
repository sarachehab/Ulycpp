#ifndef AST_ASSIGNMENT_HPP
#define AST_ASSIGNMENT_HPP

#include "ast_node.hpp"

class Assignment : public Node {
private:
    Node* target_variable_;
    Node* value_to_assign_;

public:
    Assignment(Node* target_variable, Node* value_to_assign)
        : target_variable_(target_variable)
        , value_to_assign_(value_to_assign)
    {}
    ~ Assignment () {
        delete target_variable_;
        delete value_to_assign_;
    }

    int getSize() const override;
    std::string getIdentifier() const override;
    
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    virtual void Print(std::ostream &stream) const override;
};

#endif
