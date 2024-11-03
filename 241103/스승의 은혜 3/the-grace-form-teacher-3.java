import java.util.*;
import java.lang.Math;

public class Main {
    public static int N,B;
    public static int answer = Integer.MAX_VALUE;
    public static int[] gift,deliver;
    public static int flag = 0;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        B = in.nextInt();

        gift = new int[N];
        deliver = new int[N];
        for(int i = 0; i< N;i++){
            gift[i] = in.nextInt();
            deliver[i] = in.nextInt();
        }
        


        //선물 가격 -> 짝수
        //선물 하나 반값 할인 쿠폰 
        
        for(int i = N;i >= 1;i--){
            int[] ans = new int[i];
            int[] visited = new int[i];
            dfs(0,ans,visited);
            if(flag == 1)
                break;
        }
        System.out.print(answer);
    }

    public static void dfs(int x, int[] ans,int[] visited){
        if(x == ans.length){
            cal(ans);
            return;
        }
    
        for(int i = 0;i<ans.length;i++){
            if (visited[i] == 0){
                visited[i] = 1;
                ans[i] = i;
                dfs(x+1,ans,visited);
                visited[i] = 0;
            }
        }
    }

    public static boolean cal(int[] ans){
        int result = Integer.MAX_VALUE;
        for(int i = 0;i<ans.length;i++){
            int tmp = 0;
            for(int j = 0;j<ans.length;j++){
                if(i == j)
                    tmp += (gift[ans[j]]/2+deliver[j]);
                else
                    tmp += (gift[ans[j]]+deliver[j]);

            result = Math.min(result,tmp);
            }
        }

        if(result <= B){
            answer = Math.min(answer,result);
            flag = 1;
            return true;
        }
        return false;
    }

    

}