import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int gcdNum = gcd(n,m);
        int answer = n*m/gcdNum;
        System.out.println(answer);
      
    }
    public static int gcd(int n,int m){

        while(m != 0){
            int r = n % m;
            n = m;
            m = r;
        }
        return n;
    }
}