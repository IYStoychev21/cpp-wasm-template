#include <iostream>
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
void helloWorld()
{ 
    std::cout << "Hello from CPP" << std::endl;
}
