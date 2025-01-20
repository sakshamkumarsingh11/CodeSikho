// practising short and and normal method

import java.util.*;

public class practise {
    public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    int Age = sc.nextInt();
/*    if (Age>60){
        System.out.println("Senior citizen");
    }else{
        System.out.println("Not senior citizen");
    }
*/
// by short hand
 String result= (Age>60)? "Senior citizen": "Not senior citizen";
 System.out.println(result);
 sc.close();
} 


}
