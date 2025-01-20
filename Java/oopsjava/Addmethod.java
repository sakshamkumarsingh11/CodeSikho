class  Vehicle{
    int passenger;
    int fuelcap;
    int mpg;
    //displaying method 
    void range(){
        int dist = fuelcap * mpg;
        System.out.println("The  range of the vehicle is " + dist + " miles");
    }
 }
class Addmethod {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        Vehicle u = new Vehicle();          // created objects

        

        v.passenger=100;
        v.fuelcap=15;
        v.mpg=25;                       // assigned them values
        u.passenger=200;
        u.fuelcap=20;
        u.mpg=30;
        u.range();
        v.range(); 

    }
    
}
