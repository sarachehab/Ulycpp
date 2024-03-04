// Adapted from: https://www.lysator.liu.se/c/ANSI-C-grammar-y.html

// TODO: you can either continue adding to this grammar file or
// rename parser_full.y to parser.y once you're happy with
// how this example works.

%code requires{
    #include "ast.hpp"

    extern Node *g_root;
    extern FILE *yyin;
    int yylex(void);
    void yyerror(const char *);
}

// Represents the value associated with any kind of AST node.
%union{
  Node         *node;
  NodeList     *nodes;
  int          number_int;
  double       number_float;
  std::string  *string;
  yytokentype  token;
}

%token IDENTIFIER INT_CONSTANT FLOAT_CONSTANT STRING_LITERAL
%token PTR_OP INC_OP DEC_OP LEFT_OP RIGHT_OP LE_OP GE_OP EQ_OP NE_OP AND_OP OR_OP
%token MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN ADD_ASSIGN SUB_ASSIGN LEFT_ASSIGN RIGHT_ASSIGN AND_ASSIGN XOR_ASSIGN OR_ASSIGN
%token TYPE_NAME TYPEDEF EXTERN STATIC AUTO REGISTER SIZEOF
%token CHAR SHORT INT LONG SIGNED UNSIGNED FLOAT DOUBLE CONST VOLATILE VOID
%token STRUCT UNION ENUM ELLIPSIS
%token CASE DEFAULT IF ELSE SWITCH WHILE DO FOR GOTO CONTINUE BREAK RETURN

%type <node> translation_unit external_declaration function_definition primary_expression postfix_expression argument_expression_list
%type <node> unary_expression cast_expression multiplicative_expression additive_expression shift_expression relational_expression
%type <node> equality_expression and_expression exclusive_or_expression inclusive_or_expression logical_and_expression logical_or_expression
%type <node> conditional_expression assignment_expression expression constant_expression declaration declaration_specifiers init_declarator_list
%type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
%type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
%type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
%type <node> compound_statement declaration_list expression_statement selection_statement iteration_statement jump_statement

%type <nodes> statement_list

%type <string> unary_operator assignment_operator storage_class_specifier

%type <number_int> INT_CONSTANT STRING_LITERAL
%type <number_float> FLOAT_CONSTANT
%type <string> IDENTIFIER


%start ROOT
%%

ROOT
    : translation_unit { g_root = $1; }

translation_unit
	: external_declaration { $$ = $1; }
	;

external_declaration
	: function_definition { $$ = $1; }
	;

function_definition
	: declaration_specifiers declarator compound_statement { $$ = new FunctionDefinition($1, $2, $3); }
	;

declaration_specifiers
	: type_specifier { $$ = $1; }
	;

type_specifier
	: INT { $$ = new TypeSpecifier("int"); }
	;

init_declarator_list
	: init_declarator 							{ $$ = new NodeList($1); }
	| init_declarator_list ',' init_declarator 	{ $1->PushBack($3); $$ = $1; }
	;

init_declarator
	: declarator 					{ $$ = $1; }
	| declarator '=' initializer 	{ $$ = new Assignement($1, $3); }
	;

declarator
	: direct_declarator { $$ = $1; }
	;

direct_declarator
	: IDENTIFIER 								{ $$ = new Identifier($1); }
	| direct_declarator '(' ')' 				{ $$ = new DirectDeclarator($1); }
	| direct_declarator '(' parameter_list ')'	{ $$ = new DirectDeclarator($1, $3); } // todo
	;


parameter_list
	: parameter_declaration						{ $$ = new ParametersList($1); }
	| parameter_list ',' parameter_declaration	{ $1->PushBack($3); $$ = $1; }
	;

parameter_declaration
	: declaration_specifiers declarator			{ $$ = new Parameter($1, $2); } //todo
	;


initializer
	: assignment_expression { $$ = $1; }
	;

statement
	: jump_statement 		{ $$ = $1; }
	| expression_statement 	{ $$ = $1; }
	;

declaration
	: declaration_specifiers init_declarator_list ';' { $$ = new Declaration($1, $2); }
	;

declaration_list
	: declaration					{ $$ = new NodeList($1); }
	| declaration_list declaration 	{ $1->PushBack($2); $$ = $1; }
	;

compound_statement
	: '{' statement_list '}' 					{ $$ = $2; }
	| '{' declaration_list statement_list '}'	{ $$ = new NodeList($2); $$->PushBack($3); }
	| '{' declaration_list '}'					{ $$ = $2; }
	| '{' '}'									{ $$ = nullptr; /*todo: review*/ }
	;

statement_list
	: statement 				{ $$ = new NodeList($1); }
	| statement_list statement 	{ $1->PushBack($2); $$ = $1; }
	;

expression_statement
	: ';'
	| expression ';' { $$ = $1; }
	;

jump_statement
	: RETURN ';' 			{ $$ = new ReturnStatement(nullptr); }
	| RETURN expression ';' { $$ = new ReturnStatement($2); }
	;

primary_expression
	: INT_CONSTANT 			{ $$ = new IntConstant($1); }
	| IDENTIFIER			{ $$ = new VariableIdentifier($1); }
	| '(' expression ')'	{ $$ = $2; }
	;

postfix_expression
	: primary_expression		{ $$ = $1; }
	;

argument_expression_list
	: assignment_expression
	;

unary_expression
	: postfix_expression
	| '+' cast_expression 	{ $$ = $2; }
	| '-' cast_expression	{ $$ = new Negate($2); }
	| '~' cast_expression	{ $$ = new OneComplement($2); }
	;

cast_expression
	: unary_expression
	;

multiplicative_expression
	: cast_expression
	| multiplicative_expression '*' cast_expression { $$ = new Multiplication($1, $3); }
	| multiplicative_expression '/' cast_expression { $$ = new Division($1, $3); }
	| multiplicative_expression '%' cast_expression { $$ = new Modulus($1, $3); }
	;

additive_expression
	: multiplicative_expression
	| additive_expression '+' multiplicative_expression { $$ = new Addition($1, $3); }
	| additive_expression '-' multiplicative_expression { $$ = new Substraction($1, $3); }
	;

shift_expression
	: additive_expression
	| shift_expression LEFT_OP additive_expression	{ $$ = new LeftShift($1, $3); }
	| shift_expression RIGHT_OP additive_expression	{ $$ = new RightShift($1, $3); }
	;

relational_expression
	: shift_expression
	| relational_expression '<' shift_expression 	{ $$ = new LessThan($1, $3); }
	| relational_expression '>' shift_expression 	{ $$ = new GreaterThan($1, $3); }
	| relational_expression LE_OP shift_expression 	{ $$ = new LessThanEqual($1, $3); }
	| relational_expression GE_OP shift_expression 	{ $$ = new GreaterThanEqual($1, $3); }
	;

equality_expression
	: relational_expression
	;

and_expression
	: equality_expression
	| and_expression '&' equality_expression { $$ = new And($1, $3); }
	;

exclusive_or_expression
	: and_expression
	| exclusive_or_expression '^' and_expression { $$ = new ExclusiveOr($1, $3); }
	;

inclusive_or_expression
	: exclusive_or_expression
	| inclusive_or_expression '|' exclusive_or_expression { $$ = new InclusiveOr($1, $3); }
	;

logical_and_expression
	: inclusive_or_expression
	;

logical_or_expression
	: logical_and_expression
	;

conditional_expression
	: logical_or_expression
	;

assignment_expression
	: conditional_expression
	| unary_expression '=' assignment_expression 			{ $$ = new Assignement($1, $3); }
	| unary_expression MUL_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new Multiplication($1, $3)); }
	| unary_expression DIV_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new Division($1, $3)); }
	| unary_expression MOD_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new Modulus($1, $3)); }
	| unary_expression ADD_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new Addition($1, $3)); }
	| unary_expression SUB_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new Substraction($1, $3)); }
	| unary_expression LEFT_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new LeftShift($1, $3)); }
	| unary_expression RIGHT_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new RightShift($1, $3)); }
	| unary_expression AND_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new And($1, $3)); }
	| unary_expression XOR_ASSIGN assignment_expression 	{ $$ = new Assignement($1, new ExclusiveOr($1, $3)); }
	| unary_expression OR_ASSIGN assignment_expression 		{ $$ = new Assignement($1, new InclusiveOr($1, $3)); }
	;

expression
	: assignment_expression
	;


%%

Node *g_root;

Node *ParseAST(std::string file_name)
{
  yyin = fopen(file_name.c_str(), "r");
  if(yyin == NULL){
    std::cerr << "Couldn't open input file: " << file_name << std::endl;
    exit(1);
  }
  g_root = nullptr;
  yyparse();
  return g_root;
}
