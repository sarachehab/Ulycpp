#include "context.hpp"
#include <iostream>

int label_count = 0;

void Context::useRegister(int i){
    std::cerr << "Using register " << i << std::endl;
    used_registers[i] = 1;
}

void Context::freeUpRegister(int i){
    // fail-safe
    if (i == 5 || i == 6 || i == 7 || i == 28 || i == 29 || i == 30 || i == 31) {
        used_registers[i] = 0;
        std::cerr << "Deallocating register " << i << std::endl;
    } else {
        std::cerr << "Tried to deallocate non-temporary register" << std::endl;
    }
}

int Context::allocateRegister(Specifier type){

    // define range of registers to chose form
    int start_reg_file;
    switch(type){
        case Specifier::_int:
            start_reg_file = 0;
            break;
        case Specifier::_float:
        case Specifier::_double:
            start_reg_file = 32;
            break;
        default: std::cerr << "unrecognised type in allocateRegister" << std::endl;
    }

    // find unused temporary register
    for (int i = start_reg_file; i < start_reg_file+32; i++){
        if (!used_registers[i]){
            useRegister(i);
            return i;
        }
    }

    // if all registers are used up, free up a register dating from oldest scope and use it
    for (auto stack : scopes) {
        auto scope_variable_bindings = stack.variable_bindings;

        for (auto it = scope_variable_bindings.begin(); it != scope_variable_bindings.end(); it++){

        Variable variable_specs = it->second;
        int reg = variable_specs.reg;

            if (reg != -1){
                freeUpRegister(reg);
                std::runtime_error("Missing code in allocateRegister, check ast_context");
                variable_specs.reg = -1; // variable spilled into memory, no longer in register file
                useRegister(reg);
                return reg;
            }
        }
    }
    throw std::runtime_error("Unable to allocate a register! Check ast_context.cpp");

}

std::string Context::getRegisterName(int i){
    return registers_name[i];
}


void Context::enterScope(int current_scope_size_ = 0){
    Scope scope(current_scope_size_);
    scopes.push_back(scope);
}

void Context::exitScope(){
    if (scopes.size() == 0) {
        throw std::runtime_error ("No scopes left for exitScope, check ast_context.cpp");
    }
    scopes.pop_back();
}

int Context::getCurrentScopeSize() {
    return scopes.back().current_scope_size;
}


void Context::addVariable(std::string name, int memory_cells_allocated, int sp_offset, Specifier type, int reg){
    scopes.back().variable_bindings[name] = Variable(type, memory_cells_allocated, sp_offset, reg);
}


int Context::findVariableScope(std::string name) const {
    int scopeIndex = scopes.size() - 1;
    for (auto it = scopes.rbegin(); it != scopes.rend(); ++it, --scopeIndex) {
        auto& scope_variable_bindings = it->variable_bindings;
        if (scope_variable_bindings.find(name) != scope_variable_bindings.end()){
            return scopeIndex;
        }
    }
    throw std::runtime_error ("Could not find variable in bindings, check findVariableScope in context.cpp");
}


Variable Context::getVariableSpecs(std::string name) const {
    int scope_index = findVariableScope(name);
    auto scope = scopes[scope_index];
    return scope.variable_bindings[name];
}

void Context::updateVariableSpecs(std::string name, Variable variable_specs){
    int scope_index = findVariableScope(name);
    scopes[scope_index].variable_bindings[name] = variable_specs;
}


int Context::increaseCurrentStackSize(int memory_cells_allocated) {
    scopes.back().current_scope_size += memory_cells_allocated;
    return scopes.back().current_scope_size;
}


std::string Context::createLabel(std::string name) const {
    return "_" + name + "_" + std::to_string(label_count++);
}


void Context::pushLabels(std::string start_label, std::string end_label) {
    start_labels.push(start_label);
    end_labels.push(end_label);
}

void Context::popLabels() {

    if (start_labels.size() < 1) {
        throw std::runtime_error("No start labels to pop, check context.cpp");
    }
    if (end_labels.size() < 1) {
        throw std::runtime_error("No end labels to pop, check context.cpp");
    }

    start_labels.pop();
    end_labels.pop();
}

std::string Context::getStartLabel() const {

    if (start_labels.size() < 1) {
        throw std::runtime_error("No start labels to be attributed to CONTINUE, check context.cpp");
    }

    return start_labels.top();
}

std::string Context::getEndLabel() const {

    if (end_labels.size() < 1) {
        throw std::runtime_error("No end labels to be attributed to BREAK, check context.cpp");
    }

    return end_labels.top();
}


void Context::enterFunction(Specifier type) { // TODO: Review
    // define new scope
    enterScope(0);

    // define end_label for returns
    std::string function_end_label = createLabel("function_end");
    Function new_function = Function(function_end_label, type);
    functions.push(new_function);
}

void Context::exitFunction() {
    // exit scope
    exitScope();

    // pop function from stack
    functions.pop();
}

Specifier Context::getReturnType() {
    Function current_function = functions.top();
    return current_function.return_type;
}


std::string Context::getFunctionEndLabel() const {
    if (functions.size() == 0) {
        throw std::runtime_error("No end labels to be attributed to function, check context.cpp");
    }

    return functions.top().end_label;
}


void Context::defineFloat(float number) {
    FloatIntUnion u;
    u.f = number;               // Set as float
    uint32_t intValue = u.i;    // Access as unsigned int
    std::string numberStr = std::to_string(intValue);
    floats_representation.push_back(numberStr);
}

void Context::defineDouble(double number) {
    DoubleIntUnion u;
    u.d = number;

    uint32_t int_lower = u.parts.lower;    // Access as unsigned int
    std::string str_lower = std::to_string(int_lower);
    doubles_representation.push_back(str_lower);

    uint32_t int_upper = u.parts.upper;
    std::string str_upper = std::to_string(int_upper);
    doubles_representation.push_back(str_upper);

}

unsigned int Context::getFloatLabelNumber() const {
    return floats_representation.size() - 1;
}

unsigned int Context::getDoubleLabelNumber() const {
    return doubles_representation.size()/2 - 1;
}

void Context::printImmediates(std::ostream& stream) const {
    for (long unsigned int index = 0; index < floats_representation.size(); index++){
        stream << ".LF" << index << ":" << std::endl;
        stream << "\t .word " << floats_representation[index] << std::endl;
    }
    for (long unsigned int index = 0; index < doubles_representation.size(); index+=2){
        stream << ".LD" << index/2 << ":" << std::endl;
        stream << "\t .word " << doubles_representation[index] << std::endl;
        stream << "\t .word " << doubles_representation[index+1] << std::endl;
    }
}

std::string Context::getStoreInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "sw";
        case Specifier::_float:
            return "fsw";
        case Specifier::_double:
            return "fsd";
        default: throw std::runtime_error("type not recognised in assignement emitrisc");
    }
}

std::string Context::getLoadInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "lw";
        case Specifier::_float:
            return "flw";
        case Specifier::_double:
            return "fld";
        default: throw std::runtime_error("type not recognised in assignement emitrisc");
    }
}


void Context::setOperationType(Specifier type) {
    last_operation_type = type;
}

Specifier Context::getLastOperationType() const {
    return last_operation_type;
}