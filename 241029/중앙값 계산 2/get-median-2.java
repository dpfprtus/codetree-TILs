import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;


public class Main {
    public static void main(String[] args) {

        
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i = 0;i<n;i++){
            list.add(in.nextInt());
            if((i+1) % 2 == 1){
                list.sort(Comparator.naturalOrder());
                System.out.print(list.get(list.size()/2)+" ");
            }
            
        }
        
        


    }
}