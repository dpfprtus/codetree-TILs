import java.util.*;


public class Main {
    public static int N;
    public static char[] alpha;
    public static int[] nums;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        alpha = new char[N];
        nums = new int[N];
        for(int i = 0;i<N;i++){
            alpha[i] = in.next().charAt(0);
            nums[i] = (int)alpha[i];
        }
        Arrays.sort(nums);
        int answer = 0;
        for(int i = 0;i<N;i++){
            if(nums[i] == (int)alpha[i])
                continue;
            int idx = i;
            while(true){
                if(idx == N)
                    break;
                if((int)alpha[idx] == nums[idx])
                    break;
                if((int)alpha[idx] > (int)alpha[idx+1]){
                    char tmp = alpha[idx];
                    alpha[idx] = alpha[idx+1];
                    alpha[idx+1] = tmp;
                }
                answer++;
                idx++;
            }
        }
        System.out.print(answer);

    }
}