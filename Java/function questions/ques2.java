//Write a function to print the sum of all odd numbers from 1 to n.

import java.util.*;

public class ques2{
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a number: ");
    int n = sc.nextInt();
    int sum = 0;
    for (int i=1; i<n; i++) {
        if (i%2 != 0) {
            sum += (i);}
    }
    System.out.println("The sum of all odd numbers are " +  sum);
    sc.close();

}
}