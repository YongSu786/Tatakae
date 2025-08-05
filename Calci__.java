import java.util.Scanner;

public class Calci__ {

    public static double add(double a, double b, double c, double d) {
        return a + b + c + d;
    }

    public static double subtract(double a, double b, double c, double d) {
        return a - b - c - d;
    }

    public static double multiply(double a, double b, double c, double d) {
        return a * b * c * d;
    }

    public static double divide(double a, double b) {
        if (b == 0) {
            System.out.println("Error: Division by zero!");
            return Double.NaN;
        }
        return a / b;
    }

    public static double squareRoot(double a) {
        if (a < 0) {
            System.out.println("Error: Cannot take square root of a negative number!");
            return Double.NaN;
        }
        return Math.sqrt(a);
    }

    public static double logarithm(double a) {
        if (a <= 0) {
            System.out.println("Error: Logarithm undefined for zero or negative numbers!");
            return Double.NaN;
        }
        return Math.log10(a);
    }

    public static double sine(double angle) {
        return Math.sin(Math.toRadians(angle));
    }

    public static double cosine(double angle) {
        return Math.cos(Math.toRadians(angle));
    }

    public static double tangent(double angle) {
        return Math.tan(Math.toRadians(angle));
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double num1, num2, num3, num4, result = 0;
        char operator;

        System.out.println("Enter First Number :");
        num1 = input.nextDouble();

        System.out.println("Enter an operator (+, -, *, /, s for sqrt, l for log, "
                         + "n for sin, c for cos, t for tan):");
        operator = input.next().charAt(0);

        if (operator == 's') {
            result = squareRoot(num1);
            System.out.println("Result = " + result);
        } 
        else if (operator == 'l') {
            result = logarithm(num1);
            System.out.println("Result = " + result);
        }
        else if (operator == 'n') { // sine
            result = sine(num1);
            System.out.println("sin(" + num1 + ") = " + result);
        }
        else if (operator == 'c') { // cosine
            result = cosine(num1);
            System.out.println("cos(" + num1 + ") = " + result);
        }
        else if (operator == 't') { // tangent
            result = tangent(num1);
            System.out.println("tan(" + num1 + ") = " + result);
        }
        else {
            System.out.println("Enter Second Number:");
            num2 = input.nextDouble();
            System.out.println("Enter Third Number:");
            num3 = input.nextDouble();
            System.out.println("Enter Fourth Number:");
            num4 = input.nextDouble();

            switch (operator) {
                case '+':
                    result = add(num1, num2, num3, num4);
                    break;
                case '-':
                    result = subtract(num1, num2, num3, num4);
                    break;
                case '*':
                    result = multiply(num1, num2, num3, num4);
                    break;
                case '/':
                    result = divide(num1, num2);
                    break;
                default:
                    System.out.println("Invalid Operator!");
                    input.close();
                    return;
            }
            System.out.println("Result = " + result);
        }

        input.close();
    }
}

