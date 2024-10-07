from collections import deque

#최상단 1,1 -> r,c

#미로의 각 칸
    #1. 빈칸 -> 이동 가능
    #2. 벽 -> 이동x,1~9이하의 내구도, 회전할 때 내구도 1씩 깎임, 내구도 0 -> 빈 칸
    #3. 출구 -> 참가자가 해당 칸 도달 -> 탈출


#운영
    #1. 1초마다 모든 참가자가 한 칸씩 움직임
        #모든 참가자는 동시에 움직임
        #상하좌우, 벽이 없는 곳으로 이동 가능
        #움직인 칸은 출구까지의 최단거리가 가까워야 한다.
        #움직일 수 있는 칸이 2개 이상이면, 상하로 움직이는 것을 우선시
        #움직일 수 없는 상황이면 움직이지 않음
        #한 칸에 2명 이상의 참가자 있을 수 있음


    
#결과
#모든 참가자들의 이동거리 합과 출구 좌표를 출력

#k -> 게임시간
N,M,K = map(int,input().split())
miro = [list(map(int,input().split())) for _ in range(N)]

#참가자 좌표 -> 초기엔 모두 빈칸
people = []
for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    people.append([a,b,0])


#출구
dest = [0,0]
a,b = map(int,input().split())
a-=1
b-=1
dest[0] = a
dest[1] = b

miro[a][b] = -1

#참가자들의 이동 거리
move = [0]*M


#
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def check_range(x,y):
    return 0<=x <N and 0<= y<N

#참가자와 출구 까지의 최단 거리를 계산하고 참가자를 이동
def minimum_distance(k,r,c):
    now_distance = abs(r-dest[0])+abs(c-dest[1])
    appendix = []

    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]

        if not check_range(nr,nc) or (miro[nr][nc] != -1 and miro[nr][nc] != 0):
            continue

        tmp = abs(nr-dest[0])+abs(nc-dest[1])

        if tmp < now_distance:
            now_distance = tmp
            appendix = [nr,nc]

    if len(appendix) == 0:
        return

    people[k][0] = appendix[0]
    people[k][1] = appendix[1]
    move[k] += 1

    if appendix[0] == dest[0] and appendix[1] == dest[1]:
        people[k][2] = 1

    return
        
#참가자 이동
def people_move():
    for i,(r,c,k) in enumerate(people):
        if k == 1:
            continue
        minimum_distance(i,r,c)     
    return

#미로 회전
    #2. 미로 회전
        #한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡음
        #가장 작은 크기를 갖는 정사각항이 2개이상 -> 좌상단 r좌표가 작고, c좌표가 작은 것 우선시
        #시계방향으로 90도 회전하며, 회전된 벽은 내구도 1씩 깎임

##중요
def spin_rectangle(idx):

    r1,c1 = people[idx][0],people[idx][1]
    row = abs(r1-dest[0])
    column = abs(c1-dest[1])
    d,r,c = max(row,column),min(r1,dest[0]),min(c1,dest[1])

    if row > column:
        c = max(c1,dest[1]) - d
        while c <0:
            c +=1
        return (d,r,c)
    elif row < column:
        r = max(r1,dest[0]) - d
        while r < 0:
            r += 1
        return (d,r,c)
    else:
        return (d,r,c)
    
def spin():
    distance = []
    for idx,(r,c,k) in enumerate(people):
        if k == 1:
            continue
        distance.append(spin_rectangle(idx))
    distance.sort()
    d,r,c = distance[0]


    tmp = [[i for i in a] for a in miro]
    people_idx = [0]*M
    for i in range(d+1):
        for j in range(d+1):
            if tmp[r+i][c+j] > 0:
                tmp[r+i][c+j] -= 1

            miro[r+j][c+d-i] = tmp[r+i][c+j]

            if miro[r+j][c+d-i] == -1:
                dest[0] = r+j
                dest[1] = c+d-i

            for idx,(a1,b1,c1) in enumerate(people):
                if (r+i,c+j) == (a1,b1) and people_idx[idx] == 0:
                    people_idx[idx] = 1
                    people[idx][0] = r+j
                    people[idx][1] = c+d-i

def run():
    people_move()
    spin()
    
#게임 시작

for t in range(K):
    run()
    if all(k == 1 for r, c, k in people):
        break

print(sum(move))
print(dest[0]+1,dest[1]+1)