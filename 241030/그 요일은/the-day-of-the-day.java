import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
 
        int[] nums = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();

        

        //2 -> 29
        //4,6,9,11 -> 30

        String[] dayList = {"Mon","Tue","Wed","Thu","Fri","Sat","Sun"};
        String day = br.readLine();

        

        int dayIdx = Arrays.asList(dayList).indexOf(day);
        
        if(nums[0] == nums[2]){
            int answer = nums[3]-nums[1]+1;
            int tmp = answer % 7;
            int result = answer / 7;
            if(tmp >= dayIdx+1){
                result += 1;
            }
            System.out.print(result);
            return;
        }

        int answer = 0;
        int checkNum = 0;
        

        for(int i = nums[0];i< nums[2];i++){
            checkNum = check(i);
            if(checkNum == 2){
                if(i == nums[0]){
                    answer += 29-nums[1]+1;
                } else{
                    answer += 20;
                }
            }
            else if(checkNum == 1){
                if(i == nums[0]){
                    answer += 30-nums[1]+1;
                } else{
                    answer += 30;
                }
            } else{
                if(i == nums[0]){
                    answer += 31-nums[1]+1;
                } else{
                    answer += 31;
                }
            }
        }
        answer += nums[3];
        int tmp = answer % 7;
        int result = answer / 7;
        if(tmp >= dayIdx+1){
            result += 1;
        }
        System.out.print(result);
        
    }

    public static int check(int n){
        if(n == 2){
            return 2;
        }
        if(n == 4 || n== 6 || n == 9 || n == 11){
            return 1;
        }
        return 0;
    }
}