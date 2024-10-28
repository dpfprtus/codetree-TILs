import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int[] nums = new int[n];
        for(int i = 0;i<n;i++){
            nums[i] = in.nextInt();
        }
        if(n==1){
            System.out.println(nums[0]);
            return;
        }

        int gcdNum = gcd(nums[0],nums[1]);
        int lcmNum = (nums[0]*nums[1]) / gcdNum;

        for(int i = 2;i<n;i++){
            gcdNum = gcd(lcmNum,nums[i]);
            lcmNum = (lcmNum*nums[i]) / gcdNum;
        }
        System.out.println(lcmNum);

    }

    public static int gcd(int a, int b){
        if(b == 0){
            return a;
        }
        return gcd(b,a%b);
    }
}