import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int num = in.nextInt();

        int[] nums = new int[n];
        for(int i = 0;i<n;i++){
            nums[i] = in.nextInt();
        }

        int maxNum = -1;

        for(int i = 0;i<n;i++){
            int tmp = 0;
            for(int j = i;j<n;j++){
                if(nums[j] > num){
                    tmp += 1;
                } else{
                    break;
                }
            }
            maxNum = Math.max(tmp,maxNum);
        }

        System.out.print(maxNum);

    }
}