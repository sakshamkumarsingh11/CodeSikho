import java.util.*;

public class stringbuilder {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Hello, World!");
        System.out.println(sb);
        System.out.println(sb.charAt(0));           //using charAt

        sb.setCharAt(0,'p');
        System.out.println(sb);             //used .setCharAt to set the character at the given index
        

        // deleting
        sb.delete(2,5);
        System.out.println(sb); //used .delete to delete the characters from the given index to th

        //appending
        sb.append("Java");
        System.out.println(sb); //used .append to append the string to the end of the StringBuilder
    }
    
}
