import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt();
        int[] arr = new int[N];
        for(int i=0;i<N;i++)
            arr[i] = in.nextInt();
        
        for(int i = 0;i<N;i++){
            int min = i;
            for(int j = i+1;j<N;j++){
                if(arr[j] < arr[min]){
                    min = j;
                }
            }
            int tmp = arr[i];
            arr[i] = arr[min];
            arr[min] = tmp;
        }

        for(int i = 0;i<N;i++)
            System.out.print(String.valueOf(arr[i])+" ");

    }
}