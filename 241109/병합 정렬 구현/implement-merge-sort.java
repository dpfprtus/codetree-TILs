import java.util.*;

public class Main {
    public static int N;
    public static int[] temp;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        N = in.nextInt();
        int[] arr = new int[N];
        temp = new int[N];
        for(int i = 0;i<N;i++)
            arr[i] = in.nextInt();

        mergeSort(arr,0,arr.length-1);
        for(int num : arr)
            System.out.print(num+" ");
    }
    
    public static void mergeSort(int[] arr,int low,int high){
        if(low == high)
            return;

        int mid = (low+high)/2;
     
        mergeSort(arr,low,mid);
        mergeSort(arr,mid+1,high);
        merge(arr,low,mid,high);

    }
    public static void merge(int[] arr,int low,int mid,int high){
        int i = low;
        int j = mid+1;
        int k= low;
      
        while(i<=mid && j <=high){
            if(arr[i]<arr[j]){
                temp[k] = arr[i];
                i++;
            }else{
                temp[k] = arr[j];
                j++;
            }
            k++;
        }
        while(i <= mid){
            temp[k] = arr[i];
            i++;
            k++;
        }

        while(j<=high){
            temp[k] = arr[j];
            j++;
            k++;
        }

        for(int t = low;t<=high;t++){
            arr[t] = temp[t];
        }

    }
}