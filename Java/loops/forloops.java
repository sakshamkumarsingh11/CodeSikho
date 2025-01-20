// printing tables

/*import java.util.*;



public class forloops {
    public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.println("Enter the numbers whose table should be printed");
    int num = sc.nextInt();
    for(int i=0; i <= 10; i++){
        System.out.println(i+"*"+num+"="+i*num);
    }sc.close();
    }
}*/

//programming the same thing again but this time will take input of how much should the table loop

import java.util.*;
public class forloops {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the number whose table should be printed");
        int num = sc.nextInt();
        System.out.println("Enter the number of times the table should be printed");
        int j = sc.nextInt();
        for (int i = 0 ; i<=j ; i++){
            System.out.println(i+"*"+num+"="+i*num);
        } sc.close();
    
    }
}