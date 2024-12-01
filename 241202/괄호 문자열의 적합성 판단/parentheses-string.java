import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);
        Stack<Character> s = new Stack<>();
        String a = in.next();
        for(int i = 0;i<a.length();i++){
            Character chr1 = a.charAt(i);
            if(chr1 == '('){
                s.push(chr1);
            } else{
                if(s.empty()){
                    System.out.print("No");
                    return;
                }
                s.pop();
            }
        }
        if(s.size() != 0){
            System.out.print("No");
        }else{
            System.out.print("Yes");
        }
    }
}