import java.util.Scanner;

public class SimpleATM {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 1000.0; // starting balance
        int choice;

        while (true) {
            System.out.println("\n--- ATM Menu ---");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            try {
                choice = scanner.nextInt();

                if (choice == 1) {
                    System.out.println("Current Balance: $" + balance);
                } else if (choice == 2) {
                    System.out.print("Enter amount to deposit: ");
                    double deposit = scanner.nextDouble();

                    if (deposit <= 0) {
                        throw new IllegalArgumentException("Deposit must be more than 0.");
                    }

                    balance += deposit;
                    System.out.println("Deposited: $" + deposit);
                    System.out.println("New Balance: $" + balance);

                } else if (choice == 3) {
                    System.out.print("Enter amount to withdraw: ");
                    double withdraw = scanner.nextDouble();

                    if (withdraw <= 0) {
                        throw new IllegalArgumentException("Withdrawal must be more than 0.");
                    }

                    if (withdraw > balance) {
                        throw new ArithmeticException("Not enough balance.");
                    }

                    balance -= withdraw;
                    System.out.println("Withdrawn: $" + withdraw);
                    System.out.println("New Balance: $" + balance);

                } else if (choice == 4) {
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;
                } else {
                    System.out.println("Invalid choice. Try again.");
                }

            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                scanner.nextLine(); // clear wrong input
            } finally {
                System.out.println("-----------------------------");
            }
        }

        scanner.close();
    }
}

