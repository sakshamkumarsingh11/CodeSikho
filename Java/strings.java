import java.util.*;

public class strings{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the input 1");
        String str = sc.nextLine();
        String str1 = str.toLowerCase();
        System.out.println("Enter the input 2");
        String str2= sc.nextLine();
        String str22 = str2.toLowerCase();
        System.out.println(str1);
        if (str1.compareTo(str22)==0){
            System.out.println("Strings are equal");
        }else{
            System.out.println("Strings are not equal");
        }sc.close();

        
    }
} 

// used toLowerCase (similiary toUpperCase bhi use kar sakte hai)
// fir use kiya humne name1.comapareTo.(name2)