import sys
from collections import deque
input = sys.stdin.readline


K,M = map(int,input().split())


umul = [list(map(int,input().split())) for _ in range(5)]
wall = deque(list(map(int,input().split())))


#회전,우선순위 반영

#열이작음 -> 행이 작음


dx = [0,0,-1,1]
dy = [-1,1,0,0]

#회전한다, k는 회전횟수(3까지)
def rotate_and_fill(x,y,k):
    tmp_tmp = [[i for i in a] for a in umul]
    tmp_rotate = [[0]*3 for _ in range(3)]
   
    for i in range(3):
        for j in range(3):
            tmp_rotate[i][j] = tmp_tmp[x-1+i][y-1+j]
            
    if k == 1:
        
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]
        

    elif k == 2:
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]

    elif k == 3:
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]
        tmp_rotate = zip(*tmp_rotate[::-1])
        tmp_rotate = [list(i) for i in tmp_rotate]

    for i in range(3):
        for j in range(3):
            tmp_tmp[x-1+i][y-1+j] = tmp_rotate[i][j]
    return tmp_tmp

def check_range(x,y):
    return 0<=x<5 and 0<=y<5

#유물을 조각을 찾고 visited에 표시한다.
def bfs(tmp):
    visited =[[0]*5 for _ in range(5)]
    result = []

    for i in range(5):
        for j in range(5):
            q = deque([(i,j)])
            k = [(i,j)]
            if visited[i][j] == 0:
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for p in range(4):
                        nx = x + dx[p]
                        ny = y + dy[p] 
                        if not check_range(nx,ny):
                            continue
                        if tmp[i][j] == tmp[nx][ny] and visited[nx][ny] == 0:
                            visited[nx][ny]+=1
                            q.append((nx,ny))
                            k.append((nx,ny))
            if len(k) >= 3:
                result.append(k)


    return result


def dfs():
    result = 0
    max_tmp = []
    kkk = []
    global umul
    global answer
    for k in range(1,4):
        for i in range(1,4):
            for j in range(1,4):
                
                tmp = rotate_and_fill(j,i,k)
                visited = bfs(tmp)
                
                cnt = 0
                for t in visited:
                    cnt += len(t)
                if cnt <= result:
                    continue
                    
                else:
                    result = cnt
                    max_tmp = visited
                    
                    kkk = [j,i,k]
           
    if len(kkk)!=0:
        umul = rotate_and_fill(kkk[0],kkk[1],kkk[2])

    if result >= 3:
        holy = []
        for t in max_tmp:
            for i,j in t:
                holy.append((i,j))
        
        holy.sort(key=lambda x:(x[1],-x[0]))
        for i,j in holy:
            umul[i][j] = wall.popleft()
        answer += result

        while True:
            holy = []
            visited = bfs(umul)
            cnt = 0

            for t in visited:
                cnt += len(t)
            if cnt < 3:
                break
            for t in visited:
                for i,j in t:
                    holy.append((i,j))
            holy.sort(key=lambda x:(x[1],-x[0]))
            for i,j in holy:
                umul[i][j] = wall.popleft()
 
            answer += cnt
        return result
    else:
        return 0

for _ in range(K):
    answer = 0

    a = dfs()
    if a != 0:
        print(answer,end=" ")
#유물조각 찾기