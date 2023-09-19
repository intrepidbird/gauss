#include <stdio.h>

long long factorial(int n) {
    long long fact = 1;
    for(int i = 2; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    int number = 5;
    printf("The factorial of %d is: %lld\n", number, factorial(number));
    return 0;
}

// Just the factorial function because I'm new to C lol
