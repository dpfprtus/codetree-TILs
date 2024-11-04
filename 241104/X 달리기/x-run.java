import java.util.*;
import java.lang.Math;

public class Main {

    public static int X;
    public static int answer = Integer.MAX_VALUE;
    public static void main(String[] args) {

        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        X = in.nextInt();
        int leftDistance = X;
        int v = 1;
        int t = 0;

        while(true){
            
            leftDistance -= v;
            t++;

            if(leftDistance == 0)
                break;

            if(leftDistance >= (v+1)*(v+2)/2){
                v++;
            } else if(leftDistance >=(v+1)*v/2){

            } else{
                v--;
            }
        }
        System.out.print(t);
    }
}