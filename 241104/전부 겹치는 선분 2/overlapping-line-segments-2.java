import java.util.*;

public class Main {
    public static int[][] location;
    public static int minNum = 101;
    public static int maxNum = 0;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        location = new int[n][2];
        for(int i = 0;i<n;i++){
            location[i][0] = in.nextInt();
            minNum = Math.min(minNum,location[i][0]);
            location[i][1] = in.nextInt();
            maxNum = Math.max(maxNum,location[i][1]);
        }
        int flag = 0;

        for(int i = 0;i<n;i++){
            for(int k = minNum;k<=maxNum;k++){
                if(check(k,i)){
                    flag = 1;
                    break;
                }
            }
            if(flag == 1)
                break;
            
        }
        if(flag == 1){
            System.out.print("Yes");
        }else{
            System.out.print("No");
        }
    }

    public static boolean check(int k,int j){
        for(int i=0;i<location.length;i++){
            if(i == j)
                continue;
            if(location[i][0] <= k && location[i][1] >=k){
                continue;
            }else{
                return false;
            }
        }
        return true;

    }

}