//Write a program to create a Car class with a parameterized constructor to initialize brand, model, and price
// Print the car details using a method.
import java.util.*;

public class quesTwo {
    String brand;
    String model;
    double price;

    public quesTwo(String brand, String model, double price) {
    this.brand=brand;
    this.model=model;
    this.price=price;
    }

public void display(){
    System.out.println("Brand: "+brand);
    System.out.println("Model: "+model);
    System.out.println("Price: "+price);
}
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the brand name, model name and price respectively in order");
    String brand_name= sc.nextLine();
    String model_name= sc.nextLine();
    double price_cost= sc.nextDouble();
    quesTwo car = new quesTwo(brand_name,model_name, price_cost);
    car.display();
}
        
        
    
    
}
