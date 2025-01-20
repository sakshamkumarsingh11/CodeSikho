public class upsidedownpyramid {
    public static void main(String[] args) {
        int n=5;

        for (int i=1;  i<=n; i++){

            for (int j= 1; j<=n-1; j++){

                System.out.print(" ");
            }
            for(int j = n- i; j<=i ; i++){
                System.out.print("*");
            } 
        } System.out.println();


}
}

