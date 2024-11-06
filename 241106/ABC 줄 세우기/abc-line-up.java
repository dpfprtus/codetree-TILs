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
        }
    
        int answer = 0;
        for(int i = 0;i<N;i++){
            for(int j =0;j<N-1;j++){
                if((int)alpha[j] > (int)alpha[j+1]){
                    char tmp = alpha[j];
                    alpha[j] = alpha[j+1];
                    alpha[j+1] = tmp; 
                    answer++;
                }
            }
        }
        System.out.print(answer);

    }
}