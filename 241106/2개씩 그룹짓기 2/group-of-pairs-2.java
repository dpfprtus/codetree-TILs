import java.util.*;

public class Main {
    public static int N = 0;
    public static Integer[] nums;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        nums = new Integer[2*N];
        for(int i = 0;i<2*N;i++){
            nums[i] = in.nextInt();
        }
       
        Arrays.sort(nums,Collections.reverseOrder());
        int answer = Integer.MAX_VALUE;
        for(int i = 0;i<N;i++){
            answer = Math.min(nums[i]-nums[nums.length-N+i],answer);
            
        }
        System.out.print(answer);

    }
}