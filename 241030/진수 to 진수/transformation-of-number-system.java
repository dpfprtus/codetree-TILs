import java.util.*;
import java.io.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        
        int a = in.nextInt();
        int b = in.nextInt();
        String n = in.next();

        int decem = 0;
        int cnt = 0;
        for(int i = n.length()-1;i >= 0;i--){
            decem += Math.pow(a,i)*Character.getNumericValue(n.charAt(cnt));
            cnt += 1;
        }

        String answer = "";
        while(decem != 0){
            answer += Integer.toString(decem%b);
            decem /= b;

        }
        String result = "";

        for(int i = answer.length()-1;i>=0;i--){
            result += answer.charAt(i);
        }

        System.out.print(result);

    }
}