#ifndef AST_HPP
#define AST_HPP

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>

#include "ast_direct_declarator.hpp"
#include "ast_function_definition.hpp"
#include "ast_identifier.hpp"
#include "ast_jump_statement.hpp"
#include "ast_node.hpp"
#include "ast_type_specifier.hpp"
#include "ast_constant.hpp"
#include "ast_context.hpp"

#include "ast_binary_operation.hpp"
#include "ast_unary_operation.hpp"
#include "ast_arithmetic_operation.hpp"

#include "ast_declaration.hpp"
#include "ast_assignement.hpp"

extern Node *ParseAST(std::string file_name);

#endif
