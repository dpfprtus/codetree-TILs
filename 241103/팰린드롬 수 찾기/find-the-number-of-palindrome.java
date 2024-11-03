import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int x = in.nextInt();
        int y = in.nextInt();
        int answer = 0;
        for(int i = x;i<=y;i++){
            String a = String.valueOf(i);
            String b = new StringBuilder(a).reverse().toString();
            if(a.equals(b))
                answer++;
        }
        System.out.print(answer);
    }
}