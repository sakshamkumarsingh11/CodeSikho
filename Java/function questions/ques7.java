//Write a program to print Fibonacci series of n terms where n is input by user :
//0 1 1 2 3 5 8 13 21 ..... 


import java.util.*;

public class ques7{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the input");
        int n = sc.nextInt();
        if (n<=0){
            System.out.println("Enter a positive integer.");
            }else{
                System.out.println("The first " + n + " Fibonacci numbers are:");
                print_Fibonaci(n);
            } sc.close();
        }

    public static void print_Fibonaci(int n){
        int a = 0, b = 1;
            for (int i = 0; i <= n; i++) {
            System.out.println(a + " ");
            int next= a+b;
            a= b;
            b = next;
            }
            System.out.println();

    }
}