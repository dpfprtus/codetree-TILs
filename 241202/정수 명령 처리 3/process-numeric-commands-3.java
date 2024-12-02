import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();

        for(int i = 0;i<n;i++){
            String order = in.next();

            if(order.equals("push_front")){
                deque.addFirst(in.nextInt());
            } else if(order.equals("push_back"))
                deque.addLast(in.nextInt());
            else if(order.equals("pop_front"))
                System.out.println(deque.pollFirst());
            else if(order.equals("pop_back"))
                System.out.println(deque.pollLast());
            else if(order.equals("size"))
                System.out.println(deque.size());
            else if(order.equals("empty")){
                if(deque.isEmpty()){
                    System.out.println("1");
                }else{
                    System.out.println("0");
                }
            } else if(order.equals("front"))
                System.out.println(deque.peekFirst());       
            else if(order.equals("back"))
                System.out.println(deque.peekLast());         
        }
    }
}