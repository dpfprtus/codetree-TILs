import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i = 0;i<N;i++){
            String[] str = br.readLine().split(" ");
            if(str[0].equals("push_back")){
                list.add(Integer.parseInt(str[1]));
            } else if(str[0].equals("pop_back")){
                list.remove(list.size()-1);
            } else if(str[0].equals("size")){
                System.out.println(list.size());
            } else{
                System.out.println(list.get(Integer.parseInt(str[1])-1));
            }
        }
    }
}