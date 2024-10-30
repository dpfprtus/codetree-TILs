import java.util.*;
import java.io.*;

class Data implements Comparable<Data>{
    int height,weight,idx;

    Data(int height,int weight,int idx){
        this.height = height;
        this.weight = weight;
        this.idx = idx;
    }

    @Override
    public int compareTo(Data d){
        if(this.height == d.height){
            return d.weight - this.weight;
        }
        return this.height - d.height;
    }
}
public class Main {
    public static void main(String[] args) throws IOException{
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int idx = 1;
        Data[] data = new Data[n];
        for(int i =0;i<n;i++){
            String[] tmp = br.readLine().split(" ");
            data[i] = new Data(Integer.parseInt(tmp[0]),Integer.parseInt(tmp[1]),idx);
            idx+=1;
        }

        Arrays.sort(data);
        for(Data d : data){
            System.out.println(d.height+" "+d.weight+" "+d.idx);
        }
    }
}