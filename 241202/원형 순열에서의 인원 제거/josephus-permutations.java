import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();

        Queue<Integer> q = new LinkedList<>();

        for(int i = 1;i<=n;i++){
            q.add(i);
        }

        while(q.size() != 0){
            for(int i = 1;i<k; i++){
                q.add(q.poll());
            }
            System.out.print(q.poll()+" ");
        }
    }
}