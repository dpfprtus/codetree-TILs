import java.util.Scanner;

public class Main {
    static int a[];
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        a = new int[n];

        for(int i=0;i<n;i++){
            a[i] = in.nextInt();
        }

        for(int i=0;i<m;i++){
            int a1 = in.nextInt();
            int b1 = in.nextInt();
            int result = sumNum(a1,b1);
            System.out.println(result);
        }
    }
    public static int sumNum(int a1,int b1){
        int result = 0;

        for(int i =a1;i<=b1;i++){
            result += a[i-1];
        }
        return result;
    }
}