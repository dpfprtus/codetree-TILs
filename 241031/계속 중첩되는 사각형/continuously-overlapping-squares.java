import java.util.*;
import java.io.*;

public class Main {
    public static int[][] maps = new int[201][201];
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int color = -1;

        for(int i = 0;i<n;i++){
            int x1 = in.nextInt()+100;
            int y1 = in.nextInt()+100;
            int x2 = in.nextInt()+100;
            int y2 = in.nextInt()+100;
            
            for(int j = y1;j<y2;j++){
                for(int k = x1;k<x2;k++){
                    maps[j][k] = color;
                }
            }
            if(color == -1){
                color = 1;
            }else{
                color = -1;
            }
        }
        int cnt = 0;
        for(int i = 0;i<=200;i++){
             for(int j = 0;j<=200;j++){
                if(maps[i][j] == 1){
                    cnt++;
                }
        }
    }
        System.out.print(cnt);
    }
}