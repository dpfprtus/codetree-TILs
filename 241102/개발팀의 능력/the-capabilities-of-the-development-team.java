import java.util.*;
import java.lang.Math;

public class Main {
    public static int[] nums;
    public static int answer = Integer.MAX_VALUE;
    public static int[] team1 = new int[2];
    public static int[] team2 = new int[2];
    public static int sum1 = 0;
    public static int sum2 = 0;
    public static int team3 = 0;


    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        nums = new int[5];

        for(int i = 0;i<5;i++){
            nums[i] = in.nextInt();
        }

        for(int i = 0;i<5;i++){
            team1[0] = nums[i];
            for(int j = 0;j<5;j++){
                if(j == i){
                    continue;
                }
                team1[1] = nums[j];
                for(int k = 0;k<5;k++){
                    if(k == j || k == i){
                        continue;
                    }
                    team2[0] = nums[k];
                    for(int t =0;t<5;t++){
                        if(t == k || t == j || t == i){
                            continue;
                        }
                        team2[1] = nums[t];
                        int idx = cal();
                        team3 = nums[idx];
                        if(check()){
                            int maxNum = Math.max(sum1,Math.max(sum2,team3));
                            int minNum = Math.min(sum1,Math.min(sum2,team3));
                            
                            answer = Math.min(answer,Math.abs(maxNum-minNum));
                        }


                    }
                }
            }
        }
        if(answer == Integer.MAX_VALUE){
            System.out.print(-1);
        } else{
            System.out.print(answer);
        }
        


    }
    public static int cal(){
        int idx = 0;
        for(int i = 0;i<5;i++){
            if(team1[0] == nums[i] || team1[1] == nums[i]  || team2[0] == nums[i]  || team2[1] == nums[i]  || team3 == nums[i] ){
                continue;
            }
            idx = i;
            break;
        }
        return idx;
    }

    public static boolean check(){
        sum1 = 0;
        sum2 = 0;
        for(int i = 0; i< 2;i++){
            sum1 += team1[i];
            sum2 += team2[i];
        }

        if(sum1 == sum2 && sum2 == team3){
            return false;
        }
        return true;
    }
}