import java.util.*;
import java.io.*;

public class Main {
    
    public static int[] tile = new int[200001];
    public static int idx = 100000;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int rCount = 0;
        int lCount = 0;

        while(n != 0){
            int a = in.nextInt();
            String b = in.next();
            
            if(b.equals("R")){
                int target= idx+a;
                for(int i=idx;i<target;i++){
                    if(tile[i] == 1){
                        lCount--;
                    }
                    tile[i] = 2;

                    if(i!=target-1){
                        idx++;
                    }
                    
                    rCount++;
                }
            }else{
                int target= idx-a;

                for(int i=idx;i>target;i--){
                    if(tile[i] == 2){
                        rCount--;
                    }
                    tile[i] = 1;

                    if(i != target+1){
                        idx--;
                    }
                    lCount++;
                }
            }

            n--;
        }

        System.out.println(lCount+" "+rCount);

    }

}