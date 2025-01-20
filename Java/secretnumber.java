import java.util.*;

public class secretnumber {
   
    public static void main(String[] args) {
    int secretnumber= (int) (Math.random() * 100)+1;
    Scanner sc = new Scanner(System.in);
    int attempts = 0;
    System.out.println("Guess a number which could match the secret number");
    int guess=0;

    while (guess!=secretnumber) {
        attempts=attempts+1;
        guess= sc.nextInt();

        if( guess>secretnumber){
        System.out.println("Your guess is higher than the secret number");
        } else if(guess<secretnumber){
            System.out.println("Your guess is lower than the secret number");
        }else{
            System.out.println("You guessed the secret number");
            
        }
        }
        sc.close();

    }


   } 
    

