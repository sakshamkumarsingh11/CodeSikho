// here we are taking input from the user for array and sorting it in ascending and descending order

import java.util.*;

public class sorting {
    //made a function to print the array which will be used further
    public static void printArr(int arr[]){
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //input is taken here for the array
        int[] arr = new int[4];
        System.out.println("Enter the elements of array one by one");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("Original array is");
        
        //sorted the array here  for ascending order
        for (int i=0; i<arr.length-1; i++){
            for (int j = i+1; j<arr.length; j++){
                if (arr[i] > arr[j]) {
                    int temprorary = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temprorary;
                }
            }
            
        } 
        System.out.println("Array in ascending order is");
        printArr( arr );
        
        //descending order
        for (int i=0; i<arr.length-1; i++){
            for (int j = i+1; j<arr.length; j++){
                if (arr[i] < arr[j]) {          //swapped here
                    int temprorary = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temprorary;
                }
    
            }
            System.out.println("Array in descending order is");
            printArr(arr);
        }sc.close();
    }
}