import java.util.*;
import java.lang.Math;

public class Main {
    public static int N;
    public static int[] nums;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        nums = new int[N+1];
        
        for(int i = 1;i<=N;i++)
            nums[i] = in.nextInt();
        
        sort();
        for(int i = 1;i<=N;i++)
            System.out.print(nums[i]+" ");

    }   

    public static void heapify(int n,int i){
        int largest = i;
        int l = i*2;
        int r = i*2+1;

        if(l <= n && nums[l] > nums[largest]){
            largest = l;
        }
        
        if(r <= n && nums[r] > nums[largest]){
            largest = r;
        }
        
        if(largest != i){
            int tmp =  nums[i];
            nums[i] = nums[largest];
            nums[largest] = tmp;
            heapify(n,largest);
        }
          
    }

    public static void sort(){
        
        for(int i = N/2;i>=1;i--){
            heapify(N,i);
        }


        for(int i = N;i>1;i--){
            int tmp = nums[1];
            nums[1] = nums[i];
            nums[i] = tmp;
            heapify(i-1,1);

        }
    }
}