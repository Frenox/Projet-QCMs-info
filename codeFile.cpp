#include <iostream>

void test(int a) {
    int b = 5;
    std::cout << a * b << std::endl;
}

int main() {
    test(5);
    test(8);
    test(3);
    return 0;
}
