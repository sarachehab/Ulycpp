#ifndef  FUNCTION_CALL_HPP
#define  FUNCTION_CALL_HPP

#include "../ast_node.hpp"

class FunctionCall : public Node
{
protected:
    Node* function_name_;
    Node* arguments_;

public:
    FunctionCall(Node* function_name)
        : function_name_(function_name) 
        , arguments_(nullptr)
    {}
    FunctionCall(Node* function_name, Node* arguments)
        : function_name_(function_name)
        , arguments_(arguments)
    {}

    ~FunctionCall() {
        delete function_name_;
        delete arguments_;
    }


    std::string getIdentifier() const override;
    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
