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
	: external_declaration 					{ $$ = new NodeList($1); }
	| translation_unit external_declaration { $1->PushBack($2); $$ = $1; }
	;

external_declaration
	: function_definition 	{ $$ = new InternalFunction($1); }
	| declaration			{ $$ = new ExternalDeclaration($1); }
	;

function_definition
	: declaration_specifiers declarator compound_statement { $$ = new FunctionDefinition($1, $2, $3); }
	;

declaration_specifiers
	: type_specifier { $$ = $1; }
	;

type_specifier
	: INT 		{ $$ = new TypeSpecifier(Specifier::_int); }
	| FLOAT		{ $$ = new TypeSpecifier(Specifier::_float); }
	| DOUBLE	{ $$ = new TypeSpecifier(Specifier::_double); }
	;

init_declarator_list
	: init_declarator 							{ $$ = new NodeList($1); }
	| init_declarator_list ',' init_declarator 	{ $1->PushBack($3); $$ = $1; }
	;

init_declarator
	: declarator 					{ $$ = $1; }
	| declarator '=' initializer 	{ $$ = new Assignment($1, $3); }
	;

declarator
	: direct_declarator { $$ = $1; }
	;

direct_declarator
	: IDENTIFIER 								{ $$ = new Identifier($1); }
	| direct_declarator '(' ')' 				{ $$ = new FunctionDeclarator($1); }
	| direct_declarator '(' parameter_list ')'	{ $$ = new FunctionDeclarator($1, $3); }
	;


parameter_list
	: parameter_declaration						{ $$ = new ParametersList($1); }
	| parameter_list ',' parameter_declaration	{ $1->PushBack($3); $$ = $1; }
	;

parameter_declaration
	: declaration_specifiers declarator			{ $$ = new Parameter($1, $2); }
	;


initializer
	: assignment_expression { $$ = $1; }
	;

statement
	: jump_statement 		{ $$ = $1; }
	| expression_statement 	{ $$ = $1; }
	| selection_statement	{ $$ = $1; }
	| compound_statement	{ $$ = $1; }
	| iteration_statement	{ $$ = $1; }
	| labeled_statement		{ $$ = $1; }
	;

declaration
	: declaration_specifiers init_declarator_list ';' { $$ = new Declaration($1, $2); }
	;

declaration_list
	: declaration					{ $$ = new NodeList($1); }
	| declaration_list declaration 	{ $1->PushBack($2); $$ = $1; }
	;

compound_statement
	: '{' statement_list '}' 					{ $$ = new CompoundStatement($2); }
	| '{' declaration_list statement_list '}'	{ $$ = new CompoundStatement($2); $$->PushBack($3); }
	| '{' declaration_list '}'					{ $$ = new CompoundStatement($2); }
	| '{' '}'									{ $$ = new CompoundStatement(nullptr); }
	;

statement_list
	: statement 				{ $$ = new NodeList($1); }
	| statement_list statement 	{ $1->PushBack($2); $$ = $1; }
	;

expression_statement
	: ';'			 { $$ = new EmptyNode(); }
	| expression ';' { $$ = $1; }
	;

jump_statement
	: RETURN ';' 			{ $$ = new ReturnStatement(nullptr); }
	| RETURN expression ';' { std::cerr << "PARSER: defined return with expr" << std::endl; $$ = new ReturnStatement($2); }
	| CONTINUE ';'			{ $$ = new ContinueStatement(); }
	| BREAK ';'				{ $$ = new BreakStatement(); }
	;

primary_expression
	: INT_CONSTANT 			{ $$ = new IntConstant($1); }
	| FLOAT_CONSTANT		{ std::cerr << "declaring immediate float " << std::endl; $$ = new FloatConstant($1); }
	| IDENTIFIER			{ $$ = new VariableIdentifier($1); }
	| '(' expression ')'	{ $$ = $2; }
	;

postfix_expression
	: primary_expression										{ $$ = $1; }
	| postfix_expression '(' ')' 								{ std::cerr << "PARSER: function called here" << std::endl; $$ = new FunctionCall($1); }
	| postfix_expression '(' argument_expression_list ')'		{ $$ = new FunctionCall($1, $3); }
	| postfix_expression INC_OP									{ $$ = new RightIncrement($1); }
	| postfix_expression DEC_OP									{ $$ = new RightDecrement($1); }
	;

argument_expression_list
	: assignment_expression	{ $$ = new ArgumentList($1); }
	| argument_expression_list ',' assignment_expression { $1->PushBack($3); $$ = $1; }

	;

unary_expression
	: postfix_expression
	| '+' cast_expression 		{ $$ = $2; }
	| '-' cast_expression		{ $$ = new Negate($2); }
	| '~' cast_expression		{ $$ = new OneComplement($2); }
	| INC_OP unary_expression	{ $$ = new LeftIncrement($2); }
	| DEC_OP unary_expression	{ $$ = new LeftDecrement($2); }
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
	| equality_expression EQ_OP relational_expression { $$ = new Equal($1, $3); }
	| equality_expression NE_OP relational_expression { $$ = new NotEqual($1, $3); }
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
	| logical_and_expression AND_OP inclusive_or_expression { $$ = new LogicalAnd($1, $3); }
	;

logical_or_expression
	: logical_and_expression
	| logical_or_expression OR_OP logical_and_expression { $$ = new LogicalOr($1, $3); }
	;

conditional_expression
	: logical_or_expression												{ $$ = $1; }
	| logical_or_expression '?' expression ':' conditional_expression	{ $$ = new IfElseStatement($1, $3, $5); }
	;

assignment_expression
	: conditional_expression
	| unary_expression '=' assignment_expression 			{ $$ = new Assignment($1, $3); }
	| unary_expression MUL_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new Multiplication($1, $3)); }
	| unary_expression DIV_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new Division($1, $3)); }
	| unary_expression MOD_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new Modulus($1, $3)); }
	| unary_expression ADD_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new Addition($1, $3)); }
	| unary_expression SUB_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new Substraction($1, $3)); }
	| unary_expression LEFT_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new LeftShift($1, $3)); }
	| unary_expression RIGHT_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new RightShift($1, $3)); }
	| unary_expression AND_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new And($1, $3)); }
	| unary_expression XOR_ASSIGN assignment_expression 	{ $$ = new Assignment($1, new ExclusiveOr($1, $3)); }
	| unary_expression OR_ASSIGN assignment_expression 		{ $$ = new Assignment($1, new InclusiveOr($1, $3)); }
	;

expression
	: assignment_expression								{ $$ = $1; }
	;

constant_expression
	: conditional_expression
	;

selection_statement
	: IF '(' expression ')' statement					{ $$ = new IfStatement($3, $5); }
	| IF '(' expression ')' statement ELSE statement	{ $$ = new IfElseStatement($3, $5, $7); }
	| SWITCH '(' expression ')' statement				{ /*$$ = new Switch($3, $5);*/ }
	;

iteration_statement
	: WHILE '(' expression ')' statement												{ $$ = new WhileLoop($3, $5); }
	| DO statement WHILE '(' expression ')' ';'											{ $$ = new DoWhileLoop($5, $2); }
	| FOR '(' expression_statement expression_statement ')' statement 					{ $$ = new ForLoop($3, $4, $6); }
	| FOR '(' expression_statement expression_statement expression ')' statement		{ $$ = new ForLoop($3, $4, $5, $7); }
	;

labeled_statement
	: CASE constant_expression ':' statement	{ /*$$ = new Case($2, $4);*/ }
	| DEFAULT ':' statement						{ /*$$ = new Default($3);*/ }
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
