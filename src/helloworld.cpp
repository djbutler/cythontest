#include <iostream>
#include "helloworld.h"

namespace cythontest {

void CppWrapper::helloWorld() {
	std::cout << "Hello world!" << std::endl;
}

}
