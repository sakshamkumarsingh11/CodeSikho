//Write a function which takes in 2 numbers and returns the greater of those two.

import java.util.*;

public class ques3{
    public static int greater( int a,  int b){
    
        if (a>b){
            return a;
        } else{
            return b;}
    
        }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number");
        int b = sc.nextInt();
        System.out.println("The greater number between the two input is " + greater(a,b));
        sc.close();
    }
}