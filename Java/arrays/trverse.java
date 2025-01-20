import java.util.*;

public class trverse{
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter the number of rows");
        int n = sc.nextInt();
        System.out.println("Enter the number of rows");
        int m = sc.nextInt();
        int[][]arr=new int[n][m];       // initiallized an array



    //Input in the array
        for (int i = 0; i<n; i++){
           for (int j=0; j<m; j++){
           System.out.print("Enter element at row " + (i + 1) + ", column " + (j + 1) + ": ");
           arr[i][j] = sc.nextInt();
           }
    } 
        //output
        System.out.println("The array is:");
        for (int i = 0; i<n; i++){
            for (int j=0; j<m; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        
        // code for finding the number given by user
        System.out.println("Enter the row for the search");
        int row = sc.nextInt();
        System.out.println("Enter the column for the search");
        int col = sc.nextInt();

        if (row>=0 && row<n && col>=0 && col<m){
            System.out.println("The element of row"+row+"and column"+col+"is");
            System.out.println(arr[row][col]);
        }else{
            System.out.println("Invalid row or column");
        }
        sc.close();
        
        
    }

}