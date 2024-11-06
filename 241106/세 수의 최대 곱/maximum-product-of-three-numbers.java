import java.util.*;
import java.lang.Math;
public class Main {

    public static int N;
    public static Integer[] nums;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        nums = new Integer[N];
        for(int i = 0;i<N;i++){
            nums[i] = in.nextInt();
        }
        Arrays.sort(nums);
        int a = nums[0];
        int b = nums[1];
        Arrays.sort(nums,Collections.reverseOrder());
        int d = nums[0];
        int e = nums[1];
        int c = nums[2];

        int answer = Math.max(d*e*c,b*a*d);
        System.out.print(answer);
        //+++
        //--+
        //


        
    }
}