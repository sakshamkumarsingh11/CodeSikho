// Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered. 


import java.util.*;


public class ques5{
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        

        int count_positive =0;
        int count_negative =0;
        int count_zero =0;
        String result;          // declaration thatit is a string variable


        do{
            System.out.println("Enter the input");
            int i = sc.nextInt();

            if(i>0){
                count_positive++;}

            else if(i<0){
                count_negative++;
            }else{
                count_zero++;}
            
            System.out.println("Doyou wish to exit(Yes/No) ");

            result = sc.next();
            }while(result.equalsIgnoreCase("No")); 

        System.out.println("The count of positives are " + count_positive);
        System.out.println("The count of negatives are " + count_negative);
        System.out.println("The count of zeros are " + count_zero);

        
        sc.close();
    }

}

