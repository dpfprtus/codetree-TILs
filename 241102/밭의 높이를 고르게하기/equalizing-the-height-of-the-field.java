import java.util.*;
import java.lang.Math;

public class Main {
    
    public static int N,H,T;
    public static int[] height;
    public static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        H = in.nextInt();
        T = in.nextInt();

        height = new int[N];

        for(int i = 0;i<N;i++){
            height[i] = in.nextInt();
        }

        for(int i = 0;i <= N-T;i++){
            int sumTmp = 0;
            for(int j =i;j<i+T;j++){
                sumTmp += Math.abs(H-height[j]);
                
            }
            answer = Math.min(answer,sumTmp);
        }

        System.out.print(answer);

    }

}