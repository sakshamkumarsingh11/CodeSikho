//Enter 3 numbers from the user & make a function to print their average.


import java.util.*;


public class ques1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 3 numbers");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.println("Average of the numbers is "+(a+b+c)/3);
        sc.close();
    } 

}