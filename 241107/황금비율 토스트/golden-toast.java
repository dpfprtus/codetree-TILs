import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();

        LinkedList<Character> list = new LinkedList();
        
        String a = in.next();
        for(int i =0;i<N;i++){
            list.add(a.charAt(i));
        }
        ListIterator<Character> it = list.listIterator(list.size());

        for(int i = 0;i<M;i++){
            String order = in.next();
            if(order.equals("L")){
                if(it.hasPrevious()){
                    it.previous();
                }

            }else if(order.equals("P")){
                char b = in.next().charAt(0);
                it.add(b);

            }else if(order.equals("R")){
                if(it.hasNext())
                    it.next();
                
            }else{
                if(it.hasNext()){
                    it.next();
                    it.remove();
                }
            }
        }
        for(Character e : list){
            System.out.print(e);
        }
    }  
    
}