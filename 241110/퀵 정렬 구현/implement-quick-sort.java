import java.util.*;

public class Main {
    public static int N;
    public static int[] arr;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        arr = new int[N];
        for(int i = 0;i<N;i++)
            arr[i] = in.nextInt();
        quickSort(1,arr.length-1);
        for(int num : arr)
            System.out.print(num+" ");
    }

    public static int select(int low,int high){
        int i = low-1;
        int pivot = arr[high];

        for(int j = low;j<=high;j++){
            if(arr[j] < pivot){
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++;
            }
        }
        int tmp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = tmp;
        return i+1;
    }

    public static void quickSort(int low,int high){

        if(low >= high)
            return;
        int pos = select(low,high);
        quickSort(low,pos-1);
        quickSort(pos+1,high);
    }
}