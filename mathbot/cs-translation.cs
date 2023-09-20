using System;
using System.Collections.Generic;

public class Program
{
    public static int Factorial(int number) {
        int result = 1;
        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }
        return result;
    }

    public static double Square(double number) {
        return Math.Pow(number, 2);
    }

    public static List<int> Factor(int number) {
        List<int> factors = new List<int>();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                factors.Add(i);
            }
        }
        return factors;
    }

    // Other functions almost the same lol

    public static bool IsPrime(int number) {
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

    public static List<int> Fibonacci(int n) {
        List<int> fibSequence = new List<int>();
        int a = 0, b = 1;
        while (a < n) {
            fibSequence.Add(a);
            int temp = a;
            a = b;
            b = temp + b;
        }
        return fibSequence;
    }

    public static void Main() {
        // Test the functions here
    }
}
