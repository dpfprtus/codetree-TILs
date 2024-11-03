import java.util.*;
import java.lang.Math;

public class Main {
    public static int N,B;
    public static int answer = 0;
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

        int[] a = new int[N];
        for(int i = 0;i<N;i++){

            int tmp[] = new int[N];

            for(int j = 0;j<N;j++){
                tmp[j] = gift[j];
            } 

            tmp[i] /= 2;

            int[] sumList = new int[N];

            for(int j = 0;j<N;j++){
                sumList[j] = (tmp[j]+deliver[j]);
            }

            Arrays.sort(sumList);

            int student = 0;
            int tmp1 = 0;

            for(int k = 0;k<N;k++){
                if(tmp1 +  sumList[k] > B)
                    break;
                tmp1 += sumList[k];
                student++;
            }
            answer = Math.max(answer,student);
            
        }
        System.out.print(answer);
    }

}