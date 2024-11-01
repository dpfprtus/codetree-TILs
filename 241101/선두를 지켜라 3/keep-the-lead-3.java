import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        int[] a = new int[1000001];
        int[] b = new int[1000001];
        //A
        int aIdx = 1;
        for(int i = 0;i<n;i++){
            int v = in.nextInt();
            int t = in.nextInt();

            for(int j = 1;j<=t;j++){
                a[aIdx] = a[aIdx-1]+v;
                aIdx++;
            }
        }
        
        int bIdx = 1;
        //B
        for(int i = 0;i<m;i++){
            int v = in.nextInt();
            int t = in.nextInt();

            for(int j = 1;j<=t;j++){
                b[bIdx] = b[bIdx-1]+ v;
                bIdx++;
            }
        }
        int cnt = 0;
        int maxIdx = aIdx > bIdx ? aIdx : bIdx;
        int sundu = 0;
        int tmp = 0;

        for(int i = 1;i<maxIdx;i++){
            if(a[i] > b[i]){
                tmp = -1;
            }
            else if(a[i] == b[i]){
                tmp = 2;
            }
            else if(a[i]<b[i]){
                tmp = 1;
            }

            if(sundu != tmp){
                cnt++;
            }
            sundu = tmp;
        }

        System.out.print(cnt);

        
    }
}