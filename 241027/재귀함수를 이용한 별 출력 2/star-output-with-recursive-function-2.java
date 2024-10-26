import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        
        printMinusStar(n,n);
        printPlusStar(n,1);
    }

    public static void printPlusStar(int n,int x){

        if(x == n+1){
            return;
        }
        StringBuilder sb = new StringBuilder();
        for(int j = 1;j <=x;j++){
            sb.append("* ");
        }
        System.out.println(sb);
        printPlusStar(n,x+1);
        
    }

        public static void printMinusStar(int n,int x){

        if(x == 0){
            return;
        }
        StringBuilder sb = new StringBuilder();
        for(int j = 1;j <=x ;j++){
            sb.append("* ");
        }
        System.out.println(sb);
        printMinusStar(n,x-1);
        
    }
}