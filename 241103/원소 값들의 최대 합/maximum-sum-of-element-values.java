import java.util.*;
import java.lang.Math;

public class Main {
    public static int N,M;
    public static int[] nums;
    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        M = in.nextInt();
        nums = new int[N];
        for(int i = 0;i<N;i++)
            nums[i] = in.nextInt();

    
        int answer = 0;
        
        for(int i = 0;i<N;i++){
            int j = i;
            int tmp = 0;
            int cnt = 0;
            while(cnt < M){
                tmp += nums[j];
                j = nums[j]-1;
                cnt++;
            }
        
            answer = Math.max(answer,tmp);
        }
        System.out.print(answer);
    }
}