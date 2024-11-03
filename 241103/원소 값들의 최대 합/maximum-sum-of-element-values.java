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
        int cnt = 0;
        for(int i = 0;i<N;i++){
            int j = nums[i]-1;
            int tmp = nums[i];
            while(cnt < M){
                j = nums[j]-1;
                tmp += nums[j];
                cnt++;
            }
        
            answer = Math.max(answer,tmp);
        }
        System.out.print(answer);
    }
}