import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int[] arr = new int[N];

        for(int i = 0;i<N;i++)
            arr[i] = in.nextInt();
        
        for(int i = 0;i<N;i++){
            for(int j =0;j<N-i-1;j++){
                if(arr[j] > arr[j+1]){
                    int tmp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = tmp;
                }
            }
        }
        for(int i = 0;i<N;i++){
            System.out.print(String.valueOf(arr[i])+" ");
        }
    }
}