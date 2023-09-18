#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int factorial(int number) {
    int result = 1;
    for (int factor = 2; factor <= number; factor++) {
        result *= factor;
    }
    return result;
}

double square(double number) {
    return pow(number, 2);
}

vector<int> factor(int number) {
    vector<int> factors;
    for (int i = 1; i <= number; i++) {
        if (number % i == 0) {
            factors.push_back(i);
        }
    }
    return factors;
}

double sqrt(double number) {
    return sqrt(number);
}

double log(double number, double base) {
    return log(number) / log(base);
}

double cube(double number) {
    return pow(number, 3);
}

double sin(double number) {
    return sin(number * M_PI / 180.0);
}

double cos(double number) {
    return cos(number * M_PI / 180.0);
}

double tan(double number) {
    return tan(number * M_PI / 180.0);
}

double ln(double number) {
    return log(number);
}

double exp(double number) {
    return exp(number);
}

bool isPrime(int number) {
    if (number <= 1) {
        return false;
    } else if (number == 2) {
        return true;
    } else {
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

double abs(double number) {
    return abs(number);
}

double pow(double base, double exponent) {
    return pow(base, exponent);
}

double mod(double number1, double number2) {
    return fmod(number1, number2);
}

double hypot(double side1, double side2) {
    return hypot(side1, side2);
}

vector<int> fibonacci(int n) {
    vector<int> fibSequence;
    int a = 0, b = 1;
    while (a < n) {
        fibSequence.push_back(a);
        int temp = a;
        a = b;
        b = temp + b;
    }
    return fibSequence;
}

// Please note that C++ does not have built-in support for some mathematical functions like sqrt, log, exp, abs, pow, fmod, and hypot. You would need to include the <cmath> library to use these functions from my code.

// Also, C++ does not have built-in support for complex numbers or matrix operations. You would need to use a library that supports these features, such as the Eigen library.

// Finally, please note that this C++ code only includes the mathematical functions from my Python code. The Discord bot functionality cannot be directly translated to C++ as these libraries do not have direct equivalents in C++. You would need to use different libraries or frameworks in C++ to achieve similar functionality. For example, you might use discord.cpp for the Discord bot. Please consult the respective library’s documentation for more details on how to use them.
