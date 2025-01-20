// creating a class with two methods where in one is deposit and another is withdrawl

public class Bank{
    private double balance;
    public double amount;

    public  Bank (double amount){
        this.amount=amount;
    }
    public void deposit(double balance){
        this.balance += amount;
        System.out.println("Balance after deposit"+ this.balance);
    }
    public void withdrawl(double balance){
        if(amount> balance){
            System.out.println("Withdrawl amount is too much");
        }else{
        this.balance-=amount;
        System.out.println("Balance after withdrawl "+ this.balance);
        }
    }
    public static void main(String[] args) {
        Bank bank = new Bank(0);
        bank.deposit(50000);
        bank.withdrawl(20000);
    }
    

}
