import java.util.*;
import java.lang.Math;

public class Main {
    public static int N,K;
    public static int[] nums;
    public static int minNum = Integer.MAX_VALUE;
    public static int answer = 0;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        K = in.nextInt();

        nums = new int[N];
        for(int i = 0;i<N;i++){
            nums[i] = in.nextInt();
        }
    
        

        for(int i = 1;i<10001;i++){
            int cnt = 0;
            for(int j = 0;j<N;j++){
                if(nums[j] < i){
                    cnt += (Math.abs(i-nums[j]));
                }else if(nums[j]>i+K){
                    cnt += (Math.abs(i+K-nums[j]));
                }
            }
            minNum = Math.min(minNum,cnt);
        }
        System.out.print(minNum);

    }

}