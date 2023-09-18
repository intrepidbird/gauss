import java.util.ArrayList;
import java.util.List;
import java.lang.Math;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // Code here
    }

    public static int factorial(int number) {
        int result = 1;
        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }
        return result;
    }

    public static double square(double number) {
        return Math.pow(number, 2);
    }

    public static List<Integer> factor(int number) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                factors.add(i);
            }
        }
        return factors;
    }

    public static double sqrt(double number) {
        return Math.sqrt(number);
    }

    public static double log(double number, double base) {
        return Math.log(number) / Math.log(base);
    }

    public static double cube(double number) {
        return Math.pow(number, 3);
    }

    public static double sin(double number) {
        return Math.sin(Math.toRadians(number));
    }

    public static double cos(double number) {
        return Math.cos(Math.toRadians(number));
    }

    public static double tan(double number) {
        return Math.tan(Math.toRadians(number));
    }

    public static double ln(double number) {
        return Math.log(number);
    }

    public static double exp(double number) {
        return Math.exp(number);
    }
}
public static boolean isPrime(int number) {
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

public static double abs(double number) {
    return Math.abs(number);
}

public static double pow(double base, double exponent) {
    return Math.pow(base, exponent);
}

public static double mod(double number1, double number2) {
    return number1 % number2;
}

public static double hypot(double side1, double side2) {
    return Math.hypot(side1, side2);
}

// For the 'solve_quad' function, you would need to use a library that supports complex numbers in Java, such as Apache Commons Math.

// For the 'std_dev' function, you would need to calculate the standard deviation manually or use a library that provides this functionality, such as Apache Commons Math.

public static List<Integer> fibonacci(int n) {
    List<Integer> fibSequence = new ArrayList<>();
    int a = 0, b = 1;
    while (a < n) {
        fibSequence.add(a);
        int temp = a;
        a = b;
        b = temp + b;
    }
    return fibSequence;
}

// For the 'inverse_matrix' function, you would need to use a library that supports matrix operations in Java, such as JAMA or Apache Commons Math.

// For the 'determinant' function, you would need to use a library that supports matrix operations in Java, such as JAMA or Apache Commons Math.

// Please note that this Java code only includes the mathematical functions from my Python script. 
// The Discord bot functionality cannot be directly translated to Java as these libraries do not have direct equivalents in Java. 
// You would need to use different libraries or frameworks in Java to achieve similar functionality. For example, you might use JDA (Java Discord API) for the Discord bot. 
// Please consult the respective library’s documentation for more details on how to use them.

// Cheers, IntrepidBird
