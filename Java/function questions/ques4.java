//Write a function that takes in radius as input and returns the circumference & area of  circle.


import java.util.*;

public class ques4{
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the radius of circle");
        double r = sc.nextDouble();

        double area = circleArea (r);
        double circumfernce = circleCircumference(r);
        System.out.println("The circumference of the given circle is " + circumfernce);
        System.out.println("The are of the given  circe is " + area);
    
        sc.close();

    }
    public static double circleArea (double r){
         return 3.14 * r * r;
    
    }
    public static double circleCircumference(double r){
        return 2 * 3.14 * r;
    }
}