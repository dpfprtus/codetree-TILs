import java.util.*;
import java.lang.Math;

public class Main {

    public static int[] visited;
    public static int[] nums;
    public static int[] args;
    public static int maxNum = 100000;
    public static void main(String[] axrgs) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int s = in.nextInt();

        nums = new int[n];

        for(int i = 0; i< n;i++){
            nums[i] = in.nextInt();
        }
        
        visited = new int[n];
        args = new int[n];
        generate(0,s,n);
        System.out.print(maxNum);
        
    }

    

    public static void generate(int x,int s,int n){
        if(x == 2){
            int result = 0;
            for(int i = 0;i<args.length;i++){
                if(args[i] == 0){
                    result += nums[i];
                }
                
            }
            result -= s;
            if(result>=0 && maxNum >= result){
                maxNum = result;
            }
            return;

        }

        for(int i = 0;i<n;i++){
            if(visited[i] == 0){
                visited[i] = 1;
                args[i] = nums[i];
                generate(x+1,s,n);
                visited[i] = 0;
                args[i] = 0;
            }
        }
    }
}