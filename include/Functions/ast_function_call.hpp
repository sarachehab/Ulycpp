#ifndef  FUNCTION_CALL_HPP
#define  FUNCTION_CALL_HPP

#include "ast_node.hpp"

class FunctionCall : public Node
{
protected:
    Node* identifier_;
    Node* arguments_;

public:
    FunctionCall(Node* identifier): identifier_(identifier) {delete identifier;}
    FunctionCall(Node* identifier, Node* arguments)
        : identifier_(identifier)
        , arguments_(arguments)
    {}

    ~FunctionCall() {
        delete identifier_;
        delete arguments_;
    }


    std::string getIdentifier() const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
