Script started on 2024-03-15 15:03:45+00:00 [TERM="xterm-256color" TTY="/dev/pts/1" COLUMNS="191" LINES="12"]
[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# git pull origin control_flowstatus[Kpull origin control_flow[3Pcheckout control_flowpull[Kbranch[2Ppull[1Pllbranch -D int[K[2Ppullcheckout main [8Pbranch[2Ppushcommit -m "all test cases pass for integers, implemented all functions"add .[K./test.sh compiler_tests/integer/[Kgit pull origin int[10P./test.shgit pull origin int[10P./test.shgit checkout intpull origin main [3Pcheckout main pull origin int[10P./test.sh[2Ptest.shgit pull origin int./test.sh compiler_tests[5Pgit pull origin int[K./test.sh compiler_tests/custom_simple_add/[24Pgit pull origin int[10Pstashpull origin int[7Pclean -fpull origin int[Kstatus[2Ppull./test.sh compiler_tests/custom_simple_add/git push[Kcommit -m "added slt sgt and others"push[K./test.sh compiler_tests/custom_simple_add/git pull[Kstatus[2Ppull origin int[7Pclean -fpull origin int[10Pstashpull origin int./test.sh compiler_tests/custom_simple_add/                                 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.99996568599818[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_call.cpp -o build/Functions/ast_function_call.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.999983286001225[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_call.cpp -o build/Functions/ast_function_call.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.999977254999976[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.999978092000674[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.99996879600076[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh git pull origin control_flowstatus[Kpull origin control_flow[3Pcheckout control_flowpull[Kcheckout control_flow[3@pull origin control_flowstatus[Kpull origin control_flow[18P./test.sh [K./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -o bin/c_compiler build/ast_assignment.o build/ast_compound_statement.o build/ast_constant.o build/ast_declaration.o build/ast_identifier.o build/ast_node.o build/ast_type_specifier.o build/cli.o build/compiler.o build/context.o build/ControlFlows/ast_conditional_statement.o build/ControlFlows/ast_loop.o build/ControlFlows/ast_transfer_control.o build/Functions/ast_function_declarator.o build/Functions/ast_function_definition.o build/Functions/ast_parameter.o build/Functions/ast_return_statement.o build/Operations/ast_arithmetic_operation.o build/Operations/ast_binary_operation.o build/Operations/ast_bitwise_operation.o build/Operations/ast_comparaison.o build/Operations/ast_increment.o build/Operations/ast_logical_operation.o build/Operations/ast_unary_operation.o build/parser.tab.o build/lexer.yy.o
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.99996667599771[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh 
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
^Cmake: *** [Makefile:23: build/ast_compound_statement.o] Interrupt
[0mTraceback (most recent call last):
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 511, in <module>
    main()
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 498, in main
    if not make(silent=args.short):
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 332, in make
    return_code, error_msg, _ = run_subprocess(
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 300, in run_subprocess
    subprocess.run(cmd, env=env, stdout=stdout, stderr=stderr, timeout=timeout, check=True)
  File "/usr/lib/python3.10/subprocess.py", line 505, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
  File "/usr/lib/python3.10/subprocess.py", line 1154, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "/usr/lib/python3.10/subprocess.py", line 2047, in _communicate
    self.wait(timeout=self._remaining_time(endtime))
  File "/usr/lib/python3.10/subprocess.py", line 1209, in wait
    return self._wait(timeout=timeout)
  File "/usr/lib/python3.10/subprocess.py", line 1953, in _wait
    time.sleep(delay)
KeyboardInterrupt

[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh git pull origin control_flowstatus[Kpull origin control_flow[3Pcheckout control_flowpull[Kbranch[2Ppull[1Pllbranch -D int[K[2Ppullcheckout main [8Pbranch[2Ppushcommit -m "all test cases pass for integers, implemented all functions"add .[K./test.sh compiler_tests/integer/[K compiler_tests/integer/        custom
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_declarator_list
      |                                                                                                                                  ^~~~~~~~~~~~~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_declaration
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -o bin/c_compiler build/ast_assignment.o build/ast_compound_statement.o build/ast_constant.o build/ast_declaration.o build/ast_identifier.o build/ast_node.o build/ast_type_specifier.o build/cli.o build/compiler.o build/context.o build/ControlFlows/ast_conditional_statement.o build/ControlFlows/ast_loop.o build/ControlFlows/ast_transfer_control.o build/Functions/ast_function_declarator.o build/Functions/ast_function_definition.o build/Functions/ast_parameter.o build/Functions/ast_return_statement.o build/Operations/ast_arithmetic_operation.o build/Operations/ast_binary_operation.o build/Operations/ast_bitwise_operation.o build/Operations/ast_comparaison.o build/Operations/ast_increment.o build/Operations/ast_logical_operation.o build/Operations/ast_unary_operation.o build/parser.tab.o build/lexer.yy.o
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.999981657001626[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# [K]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh compiler_tests/custom
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -o bin/c_compiler build/ast_assignment.o build/ast_compound_statement.o build/ast_constant.o build/ast_declaration.o build/ast_identifier.o build/ast_node.o build/ast_type_specifier.o build/cli.o build/compiler.o build/context.o build/ControlFlows/ast_conditional_statement.o build/ControlFlows/ast_loop.o build/ControlFlows/ast_transfer_control.o build/Functions/ast_function_declarator.o build/Functions/ast_function_definition.o build/Functions/ast_parameter.o build/Functions/ast_return_statement.o build/Operations/ast_arithmetic_operation.o build/Operations/ast_binary_operation.o build/Operations/ast_bitwise_operation.o build/Operations/ast_comparaison.o build/Operations/ast_increment.o build/Operations/ast_logical_operation.o build/Operations/ast_unary_operation.o build/parser.tab.o build/lexer.yy.o
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.999981685999956[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh compiler_tests/custom
[?2004l[32mCleaning project...[0m
[32mRunning make...[0m
make: Entering directory '/workspaces/langproc-2023-cw-Uly_Cpp'
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_assignment.cpp -o build/ast_assignment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_compound_statement.cpp -o build/ast_compound_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_constant.cpp -o build/ast_constant.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_declaration.cpp -o build/ast_declaration.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_identifier.cpp -o build/ast_identifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_node.cpp -o build/ast_node.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ast_type_specifier.cpp -o build/ast_type_specifier.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/cli.cpp -o build/cli.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/compiler.cpp -o build/compiler.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/context.cpp -o build/context.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_conditional_statement.cpp -o build/ControlFlows/ast_conditional_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_loop.cpp -o build/ControlFlows/ast_loop.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/ControlFlows/ast_transfer_control.cpp -o build/ControlFlows/ast_transfer_control.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_declarator.cpp -o build/Functions/ast_function_declarator.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_function_definition.cpp -o build/Functions/ast_function_definition.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_parameter.cpp -o build/Functions/ast_parameter.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Functions/ast_return_statement.cpp -o build/Functions/ast_return_statement.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_arithmetic_operation.cpp -o build/Operations/ast_arithmetic_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_binary_operation.cpp -o build/Operations/ast_binary_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_bitwise_operation.cpp -o build/Operations/ast_bitwise_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_comparaison.cpp -o build/Operations/ast_comparaison.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_increment.cpp -o build/Operations/ast_increment.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_logical_operation.cpp -o build/Operations/ast_logical_operation.o
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -MMD -MP -c src/Operations/ast_unary_operation.cpp -o build/Operations/ast_unary_operation.o
bison -v -d src/parser.y -o build/parser.tab.cpp
src/parser.y:38.45-60: warning: symbol 'struct_specifier' is used, but is not defined as a token and has no rules; did you mean 'enum_specifier'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
      |                                             enum_specifier
src/parser.y:38.62-84: warning: symbol 'struct_declaration_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                              struct_declarator_list
src/parser.y:38.86-103: warning: symbol 'struct_declaration' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
      |                                                                                      struct_declarator
src/parser.y:38.105-128: warning: symbol 'specifier_qualifier_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                                         identifier_list
src/parser.y:38.130-151: warning: symbol 'struct_declarator_list' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration_list'? [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
      |                                                                                                                                  struct_declaration_list
src/parser.y:39.14-30: warning: symbol 'struct_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declaration'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
      |              struct_declaration
src/parser.y:39.32-45: warning: symbol 'enum_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
      |                                struct_specifier
src/parser.y:39.47-61: warning: symbol 'enumerator_list' is used, but is not defined as a token and has no rules; did you mean 'enumerator'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
      |                                               enumerator
src/parser.y:39.63-72: warning: symbol 'enumerator' is used, but is not defined as a token and has no rules; did you mean 'enumerator_list'? [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
      |                                                               enumerator_list
src/parser.y:39.103-109: warning: symbol 'pointer' is used, but is not defined as a token and has no rules [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: symbol 'identifier_list' is used, but is not defined as a token and has no rules; did you mean 'initializer_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
      |              initializer_list
src/parser.y:40.30-38: warning: symbol 'type_name' is used, but is not defined as a token and has no rules [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: symbol 'abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'struct_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
      |                                        struct_declarator
src/parser.y:40.60-85: warning: symbol 'direct_abstract_declarator' is used, but is not defined as a token and has no rules; did you mean 'abstract_declarator'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                            abstract_declarator
src/parser.y:40.99-114: warning: symbol 'initializer_list' is used, but is not defined as a token and has no rules; did you mean 'identifier_list'? [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
      |                                                                                                   identifier_list
src/parser.y:45.16-29: warning: symbol 'unary_operator' is used, but is not defined as a token and has no rules; did you mean 'assignment_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
      |                assignment_operator
src/parser.y:45.31-49: warning: symbol 'assignment_operator' is used, but is not defined as a token and has no rules; did you mean 'unary_operator'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
      |                               unary_operator
src/parser.y:45.51-73: warning: symbol 'storage_class_specifier' is used, but is not defined as a token and has no rules; did you mean 'struct_specifier'? [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
      |                                                   struct_specifier
src/parser.y: warning: 19 nonterminals useless in grammar [-Wother]
src/parser.y: warning: 1 rule useless in grammar [-Wother]
src/parser.y:38.45-60: warning: nonterminal useless in grammar: struct_specifier [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                             ^~~~~~~~~~~~~~~~
src/parser.y:38.62-84: warning: nonterminal useless in grammar: struct_declaration_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                              ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.86-103: warning: nonterminal useless in grammar: struct_declaration [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                      ^~~~~~~~~~~~~~~~~~
src/parser.y:38.105-128: warning: nonterminal useless in grammar: specifier_qualifier_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                         ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:38.130-151: warning: nonterminal useless in grammar: struct_declarator_list [-Wother]
   38 | %type <node> init_declarator type_specifier struct_specifier struct_declaration_list struct_declaration specifier_qualifier_list struct_decl...
      |                                                                                                                                  ^~~~~~~~~~~
src/parser.y:39.14-30: warning: nonterminal useless in grammar: struct_declarator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |              ^~~~~~~~~~~~~~~~~
src/parser.y:39.32-45: warning: nonterminal useless in grammar: enum_specifier [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                ^~~~~~~~~~~~~~
src/parser.y:39.47-61: warning: nonterminal useless in grammar: enumerator_list [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                               ^~~~~~~~~~~~~~~
src/parser.y:39.63-72: warning: nonterminal useless in grammar: enumerator [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                               ^~~~~~~~~~
src/parser.y:39.103-109: warning: nonterminal useless in grammar: pointer [-Wother]
   39 | %type <node> struct_declarator enum_specifier enumerator_list enumerator declarator direct_declarator pointer parameter_list parameter_decla...
      |                                                                                                       ^~~~~~~
src/parser.y:40.14-28: warning: nonterminal useless in grammar: identifier_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |              ^~~~~~~~~~~~~~~
src/parser.y:40.30-38: warning: nonterminal useless in grammar: type_name [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                              ^~~~~~~~~
src/parser.y:40.40-58: warning: nonterminal useless in grammar: abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                        ^~~~~~~~~~~~~~~~~~~
src/parser.y:40.60-85: warning: nonterminal useless in grammar: direct_abstract_declarator [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                            ^~~~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:40.99-114: warning: nonterminal useless in grammar: initializer_list [-Wother]
   40 | %type <node> identifier_list type_name abstract_declarator direct_abstract_declarator initializer initializer_list statement labeled_statement
      |                                                                                                   ^~~~~~~~~~~~~~~~
src/parser.y:45.16-29: warning: nonterminal useless in grammar: unary_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                ^~~~~~~~~~~~~~
src/parser.y:45.31-49: warning: nonterminal useless in grammar: assignment_operator [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                               ^~~~~~~~~~~~~~~~~~~
src/parser.y:45.51-73: warning: nonterminal useless in grammar: storage_class_specifier [-Wother]
   45 | %type <string> unary_operator assignment_operator storage_class_specifier
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~
src/parser.y:167.1-24: warning: nonterminal useless in grammar: argument_expression_list [-Wother]
  167 | argument_expression_list
      | ^~~~~~~~~~~~~~~~~~~~~~~~
src/parser.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]
src/parser.y: note: rerun with option '-Wcounterexamples' to generate conflict counterexamples
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/parser.tab.o build/parser.tab.cpp
flex -o build/lexer.yy.cpp src/lexer.flex
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include   -c -o build/lexer.yy.o build/lexer.yy.cpp
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'b