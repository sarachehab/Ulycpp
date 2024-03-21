#ifndef SIZE_OF_HPP
#define SIZE_OF_HPP

#include "ast_node.hpp"

class SizeOf : public Node {
private:
    Node* type_specifier_;

public:
    SizeOf(Node* type_specifier)
        : type_specifier_(type_specifier)
    {}
    ~SizeOf() {
        delete type_specifier_;
    }

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};

#endif
