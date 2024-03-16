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
[31mError when making: ['make', '-C', PosixPath('/workspaces/langproc-2023-cw-Uly_Cpp'), 'bin/c_compiler'] took more than 59.99997042100222[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# git add -A 
[?2004lgit commit 0m [?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# git commit 0m "header"[1P[1@-
[?2004lgit pus[functions 955eb4d] header
h 9 files changed, 1267 insertions(+), 16 deletions(-)
 create mode 100644 test.py
[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# git push origin functions 
[?2004lEnumerating objects: 28, done.
Counting objects:   3% (1/28)Counting objects:   7% (2/28)Counting objects:  10% (3/28)Counting objects:  14% (4/28)Counting objects:  17% (5/28)Counting objects:  21% (6/28)Counting objects:  25% (7/28)Counting objects:  28% (8/28)Counting objects:  32% (9/28)Counting objects:  35% (10/28)Counting objects:  39% (11/28)Counting objects:  42% (12/28)Counting objects:  46% (13/28)Counting objects:  50% (14/28)Counting objects:  53% (15/28)Counting objects:  57% (16/28)Counting objects:  60% (17/28)Counting objects:  64% (18/28)Counting objects:  67% (19/28)Counting objects:  71% (20/28)Counting objects:  75% (21/28)Counting objects:  78% (22/28)Counting objects:  82% (23/28)Counting objects:  85% (24/28)Counting objects:  89% (25/28)Counting objects:  92% (26/28)Counting objects:  96% (27/28)Counting objects: 100% (28/28)Counting objects: 100% (28/28), done.
Delta compression using up to 16 threads
Compressing objects:   6% (1/15)Compressing objects:  13% (2/15)Compressing objects:  20% (3/15)Compressing objects:  26% (4/15)Compressing objects:  33% (5/15)Compressing objects:  40% (6/15)Compressing objects:  46% (7/15)Compressing objects:  53% (8/15)Compressing objects:  60% (9/15)Compressing objects:  66% (10/15)Compressing objects:  73% (11/15)Compressing objects:  80% (12/15)Compressing objects:  86% (13/15)Compressing objects:  93% (14/15)Compressing objects: 100% (15/15)Compressing objects: 100% (15/15), done.
Writing objects:   6% (1/15)Writing objects:  13% (2/15)Writing objects:  20% (3/15)Writing objects:  26% (4/15)Writing objects:  33% (5/15)Writing objects:  40% (6/15)Writing objects:  46% (7/15)Writing objects:  53% (8/15)Writing objects:  60% (9/15)Writing objects:  66% (10/15)Writing objects:  73% (11/15)Writing objects:  80% (12/15)Writing objects:  86% (13/15)Writing objects:  93% (14/15)Writing objects: 100% (15/15)Writing objects: 100% (15/15), 6.62 KiB | 101.00 KiB/s, done.
Total 15 (delta 12), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas:   0% (0/12)[Kremote: Resolving deltas:   8% (1/12)[Kremote: Resolving deltas:  16% (2/12)[Kremote: Resolving deltas:  25% (3/12)[Kremote: Resolving deltas:  33% (4/12)[Kremote: Resolving deltas:  41% (5/12)[Kremote: Resolving deltas:  50% (6/12)[Kremote: Resolving deltas:  58% (7/12)[Kremote: Resolving deltas:  66% (8/12)[Kremote: Resolving deltas:  75% (9/12)[Kremote: Resolving deltas:  83% (10/12)[Kremote: Resolving deltas:  91% (11/12)[Kremote: Resolving deltas: 100% (12/12)[Kremote: Resolving deltas: 100% (12/12), completed with 12 local objects.[K
To https://github.com/LangProc/langproc-2023-cw-Uly_Cpp.git
   918e304..955eb4d  functions -> functions
[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# git pull origin functions
[?2004lFrom https://github.com/LangProc/langproc-2023-cw-Uly_Cpp
 * branch            functions  -> FETCH_HEAD
Already up to date.
[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# g git pull origin functionssh origin functions [4Pcommit -m "header"[11Padd -A ./test.sh compiler_tests/custom
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
make: Leaving directory '/workspaces/langproc-2023-cw-Uly_Cpp'
compiler_tests/custom/custom_assignements/assignement_double_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_right_shift.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_single_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/identifier.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/updated_value.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/do_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stdout.log[0m

compiler_tests/custom/custom_functions/one_arg.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/multiple_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_add.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_and.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional_add.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_expression.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than_equal.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than_equal.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_modulus.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_or.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_sub.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.assembler.stdout.log[0m


>> Test Summary: [32m0 Passed, [31m37 Failed[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh compiler_tests/custom
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
make: Leaving directory '/workspaces/langproc-2023-cw-Uly_Cpp'
compiler_tests/custom/custom_assignements/assignement_double_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_right_shift.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_single_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/identifier.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/updated_value.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/do_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stdout.log[0m

compiler_tests/custom/custom_functions/one_arg.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/multiple_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_add.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_and.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional_add.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_expression.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than_equal.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than_equal.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_modulus.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_or.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.assembler.stdout.log[0m

compiler_tests/custom/custom_operations/simple_sub.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.assembler.stdout.log[0m


>> Test Summary: [32m0 Passed, [31m37 Failed[0m
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
g++ -std=c++20 -W -Wall -g -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -fsanitize=address -static-libasan -O0 -rdynamic --coverage -I include -o bin/c_compiler build/ast_assignment.o build/ast_compound_statement.o build/ast_constant.o build/ast_declaration.o build/ast_identifier.o build/ast_node.o build/ast_type_specifier.o build/cli.o build/compiler.o build/context.o build/ControlFlows/ast_conditional_statement.o build/ControlFlows/ast_loop.o build/ControlFlows/ast_transfer_control.o build/Functions/ast_function_declarator.o build/Functions/ast_function_definition.o build/Functions/ast_parameter.o build/Functions/ast_return_statement.o build/Operations/ast_arithmetic_operation.o build/Operations/ast_binary_operation.o build/Operations/ast_bitwise_operation.o build/Operations/ast_comparaison.o build/Operations/ast_increment.o build/Operations/ast_logical_operation.o build/Operations/ast_unary_operation.o build/parser.tab.o build/lexer.yy.o
make: Leaving directory '/workspaces/langproc-2023-cw-Uly_Cpp'
compiler_tests/custom/custom_assignements/assignement_double_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_right_shift.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_single_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/identifier.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/updated_value.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/do_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stdout.log[0m

compiler_tests/custom/custom_functions/one_arg.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/left_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/multiple_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment_2.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.assembler.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.assembler.stdout.log[0m

^C[0mTraceback (most recent call last):
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 511, in <module>
    main()
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 502, in main
    run_tests(args, xml_file)
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 422, in run_tests
    result = run_test(driver)
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 215, in run_test
    return_code, _, timed_out = run_subprocess(
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

[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh compiler_tests/custom
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
make: Leaving directory '/workspaces/langproc-2023-cw-Uly_Cpp'
compiler_tests/custom/custom_assignements/assignement_double_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_right_shift.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_single_init.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/identifier.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.assembler.stdout.log[0m

compiler_tests/custom/custom_assignements/updated_value.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/do_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_for.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_if.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_break.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_continue.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.assembler.stdout.log[0m

compiler_tests/custom/custom_control_flow/while.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.assembler.stdout.log[0m

compiler_tests/custom/custom_functions/one_arg.c
[31m	> Failed to assemble: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.assembler.stdout.log[0m

^C[0mTraceback (most recent call last):
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 511, in <module>
    main()
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 502, in main
    run_tests(args, xml_file)
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 422, in run_tests
    result = run_test(driver)
  File "/workspaces/langproc-2023-cw-Uly_Cpp/./scripts/test.py", line 215, in run_test
    return_code, _, timed_out = run_subprocess(
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

[?2004h]0;root@1a17860be5aa: /workspaces/langproc-2023-cw-Uly_Cpproot@1a17860be5aa:/workspaces/langproc-2023-cw-Uly_Cpp# ./test.sh compiler_tests/custom
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
make: Leaving directory '/workspaces/langproc-2023-cw-Uly_Cpp'
compiler_tests/custom/custom_assignements/assignement_double_init.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_double_init/assignement_double_init.simulation.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement/assignement.simulation.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_right_shift.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_right_shift/assignement_right_shift.simulation.stdout.log[0m

compiler_tests/custom/custom_assignements/assignement_single_init.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/assignement_single_init/assignement_single_init.simulation.stdout.log[0m

compiler_tests/custom/custom_assignements/identifier.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/identifier/identifier.simulation.stdout.log[0m

compiler_tests/custom/custom_assignements/updated_value.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_assignements/updated_value/updated_value.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/do_while.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/do_while/do_while.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_break.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_break/for_break.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/for_continue.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for_continue/for_continue.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/for.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/for/for.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/if.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/if/if.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_for.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_for/nested_for.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_if.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_if/nested_if.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/nested_while.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/nested_while/nested_while.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_break.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_break/while_break.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/while_continue.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while_continue/while_continue.simulation.stdout.log[0m

compiler_tests/custom/custom_control_flow/while.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_control_flow/while/while.simulation.stdout.log[0m

compiler_tests/custom/custom_functions/one_arg.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_functions/one_arg/one_arg.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/left_decrement.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_decrement/left_decrement.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/left_increment.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/left_increment/left_increment.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/multiple_increment.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/multiple_increment/multiple_increment.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement_2.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement_2/right_decrement_2.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/right_decrement.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_decrement/right_decrement.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment_2.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment_2/right_increment_2.simulation.stdout.log[0m

compiler_tests/custom/custom_increment/right_increment.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_increment/right_increment/right_increment.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_add.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_add/simple_add.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_and.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_and/simple_and.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional_add.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional_add/simple_conditional_add.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_conditional.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_conditional/simple_conditional.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_expression.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_expression/simple_expression.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than/simple_greater_than.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_greater_than_equal.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_greater_than_equal/simple_greater_than_equal.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than/simple_less_than.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_less_than_equal.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_less_than_equal/simple_less_than_equal.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_modulus.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_modulus/simple_modulus.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_or.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_or/simple_or.simulation.stdout.log[0m

compiler_tests/custom/custom_operations/simple_sub.c
[31m	> Failed to simulate: 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.compiler.stdout.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.s.printed 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.simulation.stderr.log 
	 /workspaces/langproc-2023-cw-Uly_Cpp/bin/output/custom/custom_operations/simple_sub/simple_sub.simulation.stdout.log[0m


>> Test Summary: [32m0 Passed, [31m37 Failed[0m
[0m[?2004h]0;root@1a17860be5aa: /workspaces/langproc-202