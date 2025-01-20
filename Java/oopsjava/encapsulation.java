// learning encapsulation  by an example '

public class encapsulation{
        private void display(){
            System.out.println("The name is saksham kumar singh");
        }
        public void hello(){
            System.out.println("He says you hello");
        }
        public static void main(String[] args) {
            encapsulation object= new encapsulation();
            object.hello();
            object.display();
        }
}

