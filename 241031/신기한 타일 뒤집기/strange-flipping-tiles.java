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
                    if(tile[i] != 2){
                        rCount++;
                    }
                    tile[i] = 2;
                    
                    
                    
                }

                idx=idx+a-1;
            }else{
                int target= idx-a;

                for(int i=idx;i>target;i--){
                    if(tile[i] == 2){
                        rCount--;
                    }
                    if(tile[i] != 1){
                        lCount++;
                    }
                    tile[i] = 1;
                    
                }
                idx = idx-a+1;
            }
            n--;
        }

        System.out.println(lCount+" "+rCount);

    }

}