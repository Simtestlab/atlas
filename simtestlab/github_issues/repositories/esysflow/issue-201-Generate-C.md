# Issue #201: Generate C++

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-06-07  
**Updated:** 2025-08-02  
**Closed:** 2025-08-02  
**Author:** @Muralipandiyan  
**Assignees:** @harish-ramar  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/201)

## Description

## Generate C++

![Image](https://github.com/user-attachments/assets/74d6d274-fd65-4625-8062-73b881c15f1a)



## Generated C++ Code
``` 
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Class declarations


// Function declarations
void inport_1() {
    // TODO: Implement 1
    void result;
    return result;
}

void outport_1() {
    // TODO: Implement 1
    void result;
    return result;
}

std::string api_call_node(std::string api_url, std::string method) {
    // TODO: Implement Network
    std::string response;
    return response;
}

void inport_2() {
    // TODO: Implement 2
    void result;
    return result;
}

int main(void) {
    inport_1();
    inport_2();
    std::string response = api_call_node(inport_2_result);
    outport_1();
    return 0;
}
```

## Summary of Mistakes in Your Original Code:
void result; – Invalid variable declaration. void can't be used as a variable type.

return result; – Invalid return statement in void functions.

Incorrect parameters and types in function calls (api_call_node expects two parameters).

Undefined variables (inport_2_result was never declared).

@divya-rosy @harish-ramar @aeroramesh @prabhagaran 