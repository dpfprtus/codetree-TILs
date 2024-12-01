import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        Stack<Integer> s = new Stack<>();
        int n = in.nextInt();

        for(int i = 0;i<n;i++){
            String order = in.next();
            if(order.equals("push"))
                s.push(in.nextInt());
            else if(order.equals("size"))
                System.out.println(s.size());
            else if(order.equals("empty")){
                if(s.empty()){
                    System.out.println("1");
                }else{
                    System.out.println("0");
                }
            }
                
            else if(order.equals("pop"))
                System.out.println(s.pop());
            else
                System.out.println(s.peek());

        }

    }
}