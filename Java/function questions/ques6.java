//Write a function that calculates the Greatest Common Divisor of 2 numbers. 
import java.util.*;


public class ques6{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first input");
        int a  = sc.nextInt();
        System.out.println("Enter the second input");
        int b= sc.nextInt();
        System.out.println("The greatest comoon divisior of "+a+" and "+b+" is "+gcd(a,b));
        sc.close();}

    public static int gcd(int a, int b){
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return  Math.abs(a);
    }
}
