import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList();

        int N = in.nextInt();
        for(int i = 0;i<N;i++){
            String order = in.next();
            if(order.equals("push_back")){
                int a = in.nextInt();
                list.addLast(a);
            }else if(order.equals("push_front")){
                int a = in.nextInt();
                list.addFirst(a);
            } else if(order.equals("pop_front")){
                System.out.println(list.pollFirst());
            } else if(order.equals("pop_back")){
                System.out.println(list.pollLast());

            }else if(order.equals("size")){
                System.out.println(list.size());
            }else if(order.equals("empty")){
                if(list.isEmpty()){
                    System.out.println(1);
                }else{
                    System.out.println(0);
                }
                
            }else if(order.equals("front")){
                System.out.println(list.peekFirst());
            }else if(order.equals("back")){
                System.out.println(list.peekLast());
            }
        }
    }
}