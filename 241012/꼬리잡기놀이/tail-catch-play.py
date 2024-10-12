from collections import deque
#n*n 격자

#3명 이상이 한팀
#맨앞 -> 머리사람, 맨 뒤 -> 꼬리사람

#이동선을 따라 이동-> 각 팀의 이동선은 끝이 이어져있음.
#각 팀의 이동선은 서로 겹치지 않음.

#머리 사람을 따라 한 칸 이동

#공이 던져짐 우 상 좌 하

#공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 공을 얻음
#머리사람을 기준으로 팀 내에서 k 번째 사람이면 k의 제곱만큼 점수 획득.
#공을 획득한 팀의 경우 -> 머리 사람과 꼬리 사람이 바뀜 -> 방향 전환

#각 팀의 획득한 점수의 총합 출력


#n-> 격자의 크기, m -> 팀의 갯수
n,m,k = map(int,input().split())

#1은 머리사람, 2는 중간사람, 3은 꼬리사람, 4는 이동 선

head = []
maps = []
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == 1:
            head.append([i,j])
    maps.append(a)
    

#맨 앞이 머리, 맨 뒤가 꼬리
team = []
point = [0]*m


dx = [0,-1,0,1]
dy = [1,0,-1,0]

def check_range(x,y):
    return 0<= x<n and 0<= y < n


def make_team(head):

    head_x,head_y = head[0],head[1]
    q = deque([(head_x,head_y)])

    visited = [[0]*n for _ in range(n)]

    visited[head_x][head_y] = 1

    team_tmp = [[head_x,head_y]]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if not check_range(nx,ny) or maps[nx][ny] == 0 or maps[nx][ny] == 4 or visited[nx][ny] == 1:
                continue

            if maps[nx][ny] == 2:
                q.append((nx,ny))
                team_tmp.append([nx,ny])
                visited[nx][ny] = 1

            elif maps[nx][ny] == 3:
                if len(team_tmp) == 1:
                    continue
                team_tmp.append([nx,ny])
                visited[nx][ny] = 1
    return team_tmp
            
#팀 구성
for i in range(m):
    team.append(make_team(head[i]))

#공 맞으면 방향 전환
#공 맞은 사람 점수 계산
#방향 대로 한칸 이동

#꼬리 한칸 이동

# #머리부터 중간까지 한 칸 이동

def move_one_head(x,y,team_idx):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not check_range(nx,ny):
            continue
        
        if maps[nx][ny] == 4:
            return nx,ny

    return -1,-1

def move_people():
    for i in range(m):
        
        #머리 이동
        head_x,head_y = team[i][0]
 
        next_head_x,next_head_y = move_one_head(head_x,head_y,i)


        #머리랑 꼬리가 이어져있는 경우
        if (next_head_x,next_head_y) == (-1,-1):
            next_head_x,next_head_y = team[i][-1]
      
            tail_x,tail_y = team[i][-1]
            maps[tail_x][tail_y] = 1

            before_tail_x, before_tail_y = team[i][-2]
            team[i][-1] = [before_tail_x,before_tail_y]
            maps[before_tail_x][before_tail_y] = 3

            for j in range(len(team[i])-2,0,-1):
                people_x,people_y = team[i][j]
                next_x,next_y = team[i][j-1]
                team[i][j] = [next_x,next_y]
            team[i][0] = [next_head_x,next_head_y]
  
 
        else:
            maps[next_head_x][next_head_y] = 1
            maps[head_x][head_y] = 2

            #꼬리부터 한 칸 이동
            tail_x,tail_y = team[i][-1]
            maps[tail_x][tail_y] = 4

            before_tail_x, before_tail_y = team[i][-2]
            team[i][-1] = [before_tail_x,before_tail_y]
    
            maps[before_tail_x][before_tail_y] = 3
            
            #중간 이동
            for j in range(len(team[i])-2,0,-1):
                people_x,people_y = team[i][j]
                next_x,next_y = team[i][j-1]
                team[i][j] = [next_x,next_y]
            team[i][0] = [next_head_x,next_head_y]

        
    return







#공에 부딪힌 팀 번호 찾기
def find_people(x,y):
    for team_idx in range(m):
        for a,b in team[team_idx]:
            if (x,y) == (a,b):
                return team_idx

#머리에서 몇번째 떨어진 사람인지 찾기
def find_order(team_idx,x,y):
    for idx,(a,b) in enumerate(team[team_idx]):
        if (a,b) == (x,y):
            return idx+1

#공에 부딪혀서 팀의 방향 전환
def change_direction(team_idx):
    tmp = []
    head_x,head_y = team[team_idx][0]
    tail_x,tail_y = team[team_idx][-1]
    maps[head_x][head_y] = 3
    maps[tail_x][tail_y] = 1
    for i in range(len(team[team_idx])-1,-1,-1):
        tmp.append(team[team_idx][i])

    return tmp

        


#공을 던지는 순서가 중요
#공 던지는 방향 전환

def throw_ball(start_x,start_y,d):
    global team

    if maps[start_x][start_y] != 0 and maps[start_x][start_y] != 4:
        team_idx = find_people(start_x,start_y)
        #포인트 추가
        people_order = find_order(team_idx,start_x,start_y)
        point[team_idx] += people_order**2
        #방향전환
        team[team_idx] = change_direction(team_idx)
        return True

    nx,ny = start_x,start_y
    for i in range(n-1):
        nx += dx[d]
        ny += dy[d]

        #공에 부딪힘
        if maps[nx][ny] != 0 and maps[nx][ny] != 4:
            team_idx = find_people(nx,ny)

            #포인트 추가
            people_order = find_order(team_idx,nx,ny)
            point[team_idx] += people_order**2

            #방향전환
            team[team_idx] = change_direction(team_idx)

            return True
    return False

#라운드 진행
now_round = 1
ball_d = 0
game_round = 1

while now_round <= k:

    
    if 1<= game_round <= n:
        ball_d = 0
        for i in range(n):
            move_people()
            throw_ball(i,0,ball_d)
            now_round+=1
            game_round += 1
            if now_round > k:
                break
        
    if n < game_round <= 2*n:

        ball_d = 1
        for i in range(n):
            move_people()
            throw_ball(n-1,i,ball_d)
            now_round+=1
            game_round += 1
            if now_round > k:
                break

    if 2*n < game_round <= 3*n:
        ball_d = 2
        for i in range(n):
            move_people()
            throw_ball(n-1-i,n-1,ball_d)
            now_round+=1
            game_round += 1
            if now_round > k:
                break
                
    if 3*n < game_round <= 4*n:
        ball_d = 3

        for i in range(n):
            move_people()
            throw_ball(0,n-1-i,ball_d)
            now_round+=1
            game_round += 1

            if now_round > k:
                break

            if game_round > 4*n:
               game_round = 1
               break

print(sum(point))