import java.util.*;

public class Factorial {
    public static void main(String[] args) {
    Scanner sc = new Scanner (System.in);
    System.out.println("Enter a number: ");
    int n = sc.nextInt();
    if (n < 0) {
        System.out.println("Factorial does not exist for negative numbers");
        } else if (n == 0) {
        System.out.println("The factorial is 1");
        } else {
            System.out.println("The factorial of number"+ n + "is" + fact(n));
        }sc.close();
    }


public static long fact(int n ){
    if(n==0|| n==1){
        return 1;
    }else{
        return n*fact(n-1);}
      
    
    }
}