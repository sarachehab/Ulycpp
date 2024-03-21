#ifndef ARRAY_INDEX_HPP
#define ARRAY_INDEX_HPP

#include "../ast_node.hpp"

class ArrayIndex : public Node
{
private:
    Node *identifier_;
    Node *index_;

public:
    ArrayIndex(Node *identifier, Node *index)
        : identifier_(identifier)
        , index_(index)
    {}
    ~ArrayIndex()
    {
        delete identifier_;
        delete index_;
    }

    int fetchVariable(Context &context) const override;

    void computeIndex(std::ostream& stream, int tmpReg, Context& context) const;

    Specifier getType(Context &context) const override;
    std::string getIdentifier() const override;

    void EmitRISC(std::ostream &stream, int destReg, Context &context) const override;
    void Print(std::ostream &stream) const override;
};


#endif