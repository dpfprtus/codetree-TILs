import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();

        int n = in.nextInt();

        for(int i = 0;i<n;i++){
            String order = in.next();

            if(order.equals("push")){
                q.add(in.nextInt());
            } else if(order.equals("front")){
                System.out.println(q.peek());
            } else if(order.equals("size")){
                System.out.println(q.size());
            } else if(order.equals("empty")){
                if(q.isEmpty()){
                    System.out.println("1");
                } else{
                    System.out.println("0");
                }
            } else{
                System.out.println(q.poll());
            }
        }
    }
}