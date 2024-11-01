import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int t = in.nextInt();
        int[][] box = new int[n][n];

        int[] dx = {-1,0,1,0};
        int[] dy = {0,1,0,-1};
        int x = n/2;
        int y = n/2;
        int nx = n/2;
        int ny = n/2;
        int direction = 0;

        String str1 = in.next();

        for(int i =0;i<n;i++){
            for(int j=0;j<n;j++){
                box[i][j] = in.nextInt();
            }
        }
        int answer = box[x][y];
        for(int i = 0;i<str1.length();i++){
            if (str1.charAt(i) == 'L'){
                direction--;
                if(direction < 0){
                    direction = 3;
                }
            } else if(str1.charAt(i) == 'R'){
                direction = (direction+1) %4;
            } else{
                nx = x+dx[direction];
                ny = y+dy[direction];

                if(0<=nx && nx < n && 0<=ny && ny < n){
                    answer += box[nx][ny];
                    x = nx;
                    y = ny;
                }
            }
        }
        System.out.print(answer);

}
}