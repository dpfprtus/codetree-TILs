import java.util.*;
import java.lang.Math;

public class Main {
    public static int[][] nums;
    public static int n;
    public static int answer = 101;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        nums = new int[n][n];

        for(int i =0;i<n;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            nums[i][0] = a;
            nums[i][1] = b;
        
        }
        Arrays.sort(nums,(a,b)->Integer.compare(a[0],b[0]));
    
        for(int i = 0;i<n;i++){
            int tmp = check(i);
            answer = Math.min(answer,tmp);
            }
        System.out.print(answer);
        }
        
    
    public static int check(int j){
        int[][] num2 = new int[n-1][n-1];

        for(int i = 0,k=0;i<n;i++){
            if(i != j){
                num2[k][0] = nums[i][0];
                num2[k][1] = nums[i][1];
                k++;
            }
        }
    
        return num2[num2.length-1][1]-num2[0][0];

    }
}