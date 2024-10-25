import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner in = new Scanner(System.in);

        int y = in.nextInt();
        int m = in.nextInt();
        int d = in.nextInt();

        //4,6,9,11월은 한 달이 30일까지다...

        boolean yoonYear = isYoon(y);

        if(3<= m && m <=5){
            if(m==4 && d == 31){
                System.out.println(-1);
            } else{
                System.out.println("Spring");
            }

        }
        else if(6<=m && m <= 8){
            if(m == 6 && d == 31){
                System.out.println(-1);
            } else{
                System.out.println("Summer");
            }
        }
        else if(9<=m && m<=11){
            if((m==9 || m==11) && d == 31){
                System.out.println(-1);
            } else{
                System.out.println("Fall");
            }
            
        }

        else if(m <= 2 || m >=12){
            if(yoonYear == false && m == 2 && d == 29){
                System.out.println(-1);
            } else{
                System.out.println("Winter");
            }
        }
        
        
    }

    public static boolean isYoon(int y){
        if(y % 4 == 0 && y % 100 == 0){
            return false;
        }
        if(y%4 == 0 && y % 100 == 0 && y % 400 == 0){
            return true;
        }
        if(y%4 == 0){
            return true;
        }
        return false;
    }
}