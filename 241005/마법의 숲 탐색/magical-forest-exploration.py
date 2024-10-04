from collections import deque
import sys
input = sys.stdin.readline
r,c,k = map(int,input().split())

stone = []
maps = [[0]*(c) for _ in range(r+3)]
answer = 0
#회전순서 => 서, 동,
#0,1,2,3 => 북, 동, 남, 서


direction = []
for i in range(k):
    t1,t2 = map(int,input().split())
    stone.append([t1,t2])


def fill_dir(x,y,d):
 
    if d == 0:
        maps[x-1][y] = 2
    elif d == 1:
        maps[x][y+1] = 2
    elif d == 2:
        maps[x+1][y] = 2
    elif d == 3:
        maps[x][y-1] = 2

#dfs로 회전하면서 재귀돌린다. 남
#1 = 골렘위치, 2 = 출구
def map_clean():
    global maps

    for i in range(3):
        for j in range(c):
            maps[i][j] = 0

    
    
#0,1,2,3 => 북, 동, 남, 서 => 이동가능한지 체크
def check(x,y,d):
    #남쪽
    if d == 2:
        if x+1 >= len(maps)-1:
            return False
        if maps[x+2][y] == 0 and maps[x+1][y+1] == 0 and maps[x+1][y-1] ==0:
            return True

    #서쪽회전 내려가기
    elif d == 3:
        if y < 2 or x+3 > len(maps):
            return False
        if maps[x][y-2] == 0 and maps[x-1][y-1] == 0 and maps[x+1][y-1] == 0 and maps[x+1][y-2] == 0 and maps[x+2][y-1] == 0:
            return True
    #동쪽회전 내려가기
    elif d == 4:
        if y+2 >= len(maps[0]) or x+2 >= len(maps):
            return False
        if maps[x][y+2] == 0 and maps[x+1][y+1] == 0 and maps[x-1][y+1] ==0 and maps[x+1][y+2]==0 and maps[x+2][y+1] == 0:
            return True

#남쪽으로 이동
def fill(x,y,d):
    #기존꺼 지우기
    maps[x-1][y] = 0
    maps[x][y-1] = 0
    maps[x][y+1] = 0

    #채우기
    maps[x+1][y-1]=1
    maps[x+1][y+1]=1
    maps[x+2][y]=1
    fill_dir(x+1,y,d)



#서쪽,동쪽 회전
def chain(d,x,y,k):

    #서쪽
    if k == 3:
        #지우기
        maps[x][y] = 0
        maps[x-1][y] = 0
        maps[x][y+1] = 0

        #채우기
        maps[x+1][y-1] = 1
        maps[x+2][y-1] = 1
        maps[x+1][y-2] = 1

        if d == 0:
            d = 3
        else:
            d-=1
        fill_dir(x+1,y-1,d)
        return d
    #동쪽
    elif k == 4:
        #지우기
        maps[x][y] = 0
        maps[x-1][y] = 0
        maps[x][y-1] = 0

        #채우기
        maps[x+1][y+1] = 1
        maps[x+1][y+2] = 1
        maps[x+2][y+1] = 1

        if d == 3:
            d = 0
        else:
            d+=1
        fill_dir(x+1,y+1,d)
        return d

#정령 이동


def bfs(a,b):

    q = deque([(a,b)])
    visited = [[0]*c for _ in range(r+3)]
    tmp = a+1
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= c:
                continue
            if (maps[nx][ny] == maps[x][y]) and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                tmp = max(tmp,nx)
            elif [nx,ny] in direction:
                q.append((nx,ny))
                visited[nx][ny] = 1
                tmp = max(tmp,nx)
            elif maps[x][y] == 2 and visited[nx][ny] == 0 and maps[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                tmp = max(tmp,nx)

    return tmp-2

seperate = 3

def fill_diferent(x,y,d):
   
    global seperate

    maps[x][y] = seperate
    maps[x][y+1] = seperate
    maps[x][y-1] = seperate
    maps[x-1][y] = seperate
    maps[x+1][y] = seperate
    fill_dir(x,y,d)
    if maps[x][y+1] == 2:
        t1,t2 = x,y+1
    elif maps[x][y-1] == 2:
        t1,t2 = x,y-1
    elif maps[x-1][y] == 2:
        t1,t2 = x-1,y-1
    elif maps[x+1][y] == 2:
        t1,t2 = x+1,y
  
    direction.append([t1,t2])
    seperate += 1

def dfs(x,y,d):
    global maps
    global answer

    if x == len(maps)-2:
        answer = answer+x-1

        fill_diferent(x,y,d)
        return True

    #남쪽
    if check(x,y,2):
        fill(x,y,d)
        dfs(x+1,y,d)
    #서쪽
    elif check(x,y,3):
        d = chain(d,x,y,3)
        dfs(x+1,y-1,d)
    #동쪽
    elif check(x,y,4):
        d = chain(d,x,y,4)
        dfs(x+1,y+1,d)
    else:
        if x < 4:
            return False
        fill_diferent(x,y,d)
        answer += bfs(x,y)
        return True

for a,d in stone:
    a -= 1
    map_clean()
    maps[0][a] = 1
    maps[1][a] = 1
    maps[1][a+1] = 1
    maps[1][a-1] = 1
    maps[2][a] = 1
    fill_dir(1,a,d)

    #중심좌표
 
    if dfs(1,a,d) == False:
            maps = [[0]*(c) for _ in range(r+3)]
            direction = []
            dfs(1,a,d)
        
print(answer)