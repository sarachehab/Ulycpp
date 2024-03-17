#ifndef AST_FUNCTION_DECLARATION
#define AST_FUNCTION_DECLARATION

#include "../ast_node.hpp"

class ExternalDeclaration : public Node {
protected:
    Node* declaration_;
public:
    ExternalDeclaration(Node* declaration)
        : declaration_(declaration)
    {}
    ~ExternalDeclaration(){
        delete declaration_;
    }

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
    void Print(std::ostream& stream) const override;
    
};

class InternalFunction : public ExternalDeclaration {
public:
    using ExternalDeclaration::ExternalDeclaration;
    ~InternalFunction(){}

    void EmitRISC(std::ostream& stream, int destReg, Context& context) const override;
};


#endif