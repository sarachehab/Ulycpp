#ifndef  FUNCTION_CALL_HPP
#define  FUNCTION_CALL_HPP

#include "../ast_node.hpp"
#include <map>

class FunctionCall : public Node
{
protected:
    Node* function_name_;
    Node* arguments_;
    mutable std::map<int, Specifier> register_mapping_type;

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

    Specifier getType(Context& context) const override;
    std::string getIdentifier() const override;

    void createHeader(std::ostream& stream, Context& context) const;
    void createFooter(std::ostream& stream, Context& context) const;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
