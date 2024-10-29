import java.util.*;
import java.io.*;


class Data implements Comparable<Data>{
    String day,date,weather;

    Data(String day, String date, String weather){
        this.day = day;
        this.date = date;
        this.weather = weather;
    }

    @Override
    public int compareTo(Data d){
        String[] str1 = this.day.split("-");
        String[] str2 = d.day.split("-");

        if (str1[0].equals(str2[0])){
            if(str1[1].equals(str2[1])){
                return Integer.parseInt(str1[2]) - Integer.parseInt(str2[2]);
            }
            return Integer.parseInt(str1[1]) - Integer.parseInt(str2[1]);
        }
        return Integer.parseInt(str1[0]) - Integer.parseInt(str2[0]);
    }
}
public class Main {

    public static void main(String[] args) throws IOException{
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Data[] data = new Data[n];
        for(int i = 0;i<n;i++){
            String[] tmp = br.readLine().split(" ");
            data[i] = new Data(tmp[0],tmp[1],tmp[2]);

        }
        Arrays.sort(data);

        for(Data d : data){
            if(d.weather.equals("Rain")){
                System.out.print(d.day+" "+d.date+" "+d.weather);
                break;
            }
        }
    }
}