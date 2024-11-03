import java.util.*;

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

        Arrays.sort(nums);
        int answer = 0;
        for(int i = N-1;i>=N-M;i--)
            answer += nums[i];
        System.out.print(answer);
        
    }
}