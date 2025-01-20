

public class Understanding {

    
        int rno;
        String name;
        String course;
    
//Constructor -> Special method executed automatic wnen object created
// Class name and  Method Name is same
        public  Understanding (int rno, String name, String course) {
            this.rno = rno;
            this.name = name;
            this.course = course;
        }
        public void display_printing(){
            System.out.println("Name: " +name);
            System.out.println("Course: " + course);
            System.out.println("Roll number: " + rno);
        }

        public static void main(String[] args) {
            System.out.println("The name of the student(s) is/are:");
            Understanding object = new Understanding(1,"SKS","CSE");  
            // yaha pe parameters nhi aenge,,,, jake prinitng class me paramenter pass karne honge jo intiallizing me hai
            object.display_printing();
            
        }
    
}