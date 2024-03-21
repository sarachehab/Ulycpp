#ifndef AST_HPP
#define AST_HPP

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>

#include "ast_node.hpp"
#include "context.hpp"

#include "ast_type_specifier.hpp"
#include "ast_identifier.hpp"
#include "ast_constant.hpp"

#include "Functions/ast_function_definition.hpp"
#include "Functions/ast_return_statement.hpp"
#include "Functions/ast_function_declarator.hpp"
#include "Functions/ast_parameter.hpp"
#include "Functions/ast_function_call.hpp"
#include "Functions/ast_argument.hpp"
#include "Functions/ast_function_declaration.hpp"

#include "Operations/ast_binary_operation.hpp"
#include "Operations/ast_unary_operation.hpp"
#include "Operations/ast_arithmetic_operation.hpp"
#include "Operations/ast_logical_operation.hpp"
#include "Operations/ast_bitwise_operation.hpp"
#include "Operations/ast_comparaison.hpp"
#include "Operations/ast_increment.hpp"

#include "ast_declaration.hpp"
#include "ast_assignment.hpp"

#include "ast_sizeof.hpp"

#include "ControlFlows/ast_conditional_statement.hpp"
#include "ControlFlows/ast_loop.hpp"
#include "ControlFlows/ast_transfer_control.hpp"
#include "ControlFlows/ast_switch.hpp"

#include "ast_compound_statement.hpp"
#include "ast_char.hpp"

extern Node *ParseAST(std::string file_name);

#endif
