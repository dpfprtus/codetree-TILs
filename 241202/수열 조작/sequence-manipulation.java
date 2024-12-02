import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<>();

        int n = in.nextInt();
        for(int i = 1;i<=n;i++)
            deque.addLast(i);
        
        while(deque.size() != 1){
            deque.pollFirst();
            deque.addLast(deque.pollFirst());
        }
        System.out.println(deque.peekFirst());
    }
}