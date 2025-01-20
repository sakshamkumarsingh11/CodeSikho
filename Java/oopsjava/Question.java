// //Write a Java program to create a class called Student with attributes name, rollNumber, and grade. 
// Create an object of this class, assign values, and display the details.

public class Question {
    double rollNo;
    String name;
    char grade;
    //Default Construvtor
    // public Question()
    // {
        
    // }   
    // this is for the case where only one argument is passed
    // public Question(int roll)
    // {
    //     rollNo=roll;
    // }    
    public Question(double rollNo, String name,  char grade){
    this.name=name;
    this.rollNo= rollNo;
    this.grade=grade;
    }
    public void display(){
    System.out.println("Name: "+name);
    System.out.println("Roll Number: "+rollNo);
    System.out.println("Grade: "+grade);
    }
    public static void main(String[] args) {
    Question obj = new Question(101, "Alice", 'A');
    // Question objDefaultConstructor = new Question();
    // Question objOneArgumentConstructor = new Question(1000);
    obj.display();
    }
}