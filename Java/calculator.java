// Implement a basic calculator with a for loop


import java.util.*;

public class calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double num1 = sc.nextDouble();
        double num2 = sc.nextDouble();

        for (;;){
        System.out.println("choose the mode to be used for calculation: (+,-,*, /) or 'exit' to quit");
        String mode = sc.next();
        if (mode.equals("exit")){
            break;

        }
        switch(mode){
            case "+":
            System.out.println(num1 + num2);
            break;

            case "-":
            System.out.println(num1 - num2);
            break;

            case "*":
            System.out.println(num1 * num2);
            break;

            case "/":
            System.out.println(num1/num2);
            break;

            default:
            System.out.println("Invalid mode");

        
        }sc.close();
    } 
   }
}