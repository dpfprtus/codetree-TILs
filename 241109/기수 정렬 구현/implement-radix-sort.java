import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int[] arr = new int[N];
        int maxNum = 0;
        for(int i = 0;i<N;i++){
            arr[i] = in.nextInt();
            maxNum = Math.max(maxNum,String.valueOf(arr[i]).length());
        }
        ArrayList<Integer>[] digitList = new ArrayList[10];
        for(int i=0;i<10;i++)
            digitList[i] = new ArrayList();
        
        for(int k=1;k<=maxNum;k++){
            for(int num : arr){
                String str = Integer.toString(num);
                int[] tmp = new int[str.length()];
                for(int i = 0;i<tmp.length;i++){
                    tmp[i] = str.charAt(i)-'0';
                }
                int digit = 0;
                if(k <= tmp.length)
                    digit = tmp[tmp.length-k];
                
                digitList[digit].add(num);
            }

            int[] arr2 = new int[N];
            int idx = 0;
            for(int i=0;i<10;i++){
                for(int j = 0;j<digitList[i].size();j++){
                    arr2[idx] = digitList[i].get(j);
                    idx++;
                }
            }
            arr = arr2;
        }
        for(int num:arr){
            System.out.print(num+" ");
        }
        
    }
}