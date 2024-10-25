import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();

        int[] numArray = fixNum(a,b);
        System.out.print(numArray[0]+" "+numArray[1]);

    }
    public static int[] fixNum(int a, int b){
        if(a<b){
            a += 10;
            b *= 2;
            int[] arrayNum = {a,b};
            return arrayNum; 
        }
        b += 10;
        a *= 2;
        int[] arrayNum = {a,b};
        return arrayNum; 
    }
}