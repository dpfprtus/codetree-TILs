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

def spin_rectangle(r,c,cm,people_tmp):
    tmp = [[0]*cm for _ in range(cm)]
    people_miro = [[0]*N for _ in range(N)]
    tmp_people = [[0]*cm for _ in range(cm)]

    appendix = [0]*M
    cnt = 1
    for idx in people_tmp:
        if people_miro[people[idx][0]][people[idx][1]] != 0:
            appendix[idx] = people_miro[people[idx][0]][people[idx][1]]
        else:
            people_miro[people[idx][0]][people[idx][1]] = cnt
            appendix[idx] = cnt
            cnt += 1

    for a in range(r,r+cm):
        for b in range(c,c+cm):
            tmp_people[a-r][b-c] = people_miro[a][b]

    tmp_people = list(map(list,zip(*tmp_people[::-1])))

    for a in range(r,r+cm):
        for b in range(c,c+cm):
            people_miro[a][b] = tmp_people[a-r][b-c]

            if people_miro[a][b] != 0:
                for idx,cnt in enumerate(appendix):
                    if cnt == 0:
                        continue
                    if cnt == people_miro[a][b]:
                        people[idx][0] = a
                        people[idx][1] = b

    #미로 회전
    for a in range(r,r+cm):
        for b in range(c,c+cm):
            tmp[a-r][b-c] = miro[a][b]
     
    tmp = list(map(list,zip(*tmp[::-1])))

    for a in range(r,r+cm):
        for b in range(c,c+cm):
            miro[a][b] = tmp[a-r][b-c]

            if miro[a][b] == -1:
                dest[0] = a
                dest[1] = b

            if miro[a][b] > 0:
                miro[a][b] -= 1


def spin():
    cm = 2
    cnt = 1
    while True:
        for j in range(N-1):
            for i in range(N-1):
                r = i
                c = j
                nr = r+cnt
                nc = c+cnt 

                if not check_range(nr,nc):
                    break
                    
                people_tmp = []
                if (r<= dest[0]<= nr and c <= dest[1] <= nc):
                    for idx,(a1,b1,c1) in enumerate(people):
                        if c1 == 1:
                            continue
                        if r<= a1 <= nr and c <= b1 <= nc:
                            people_tmp.append(idx)
                
                if len(people_tmp) != 0:
                        #회전
                    spin_rectangle(r,c,cm,people_tmp)
                    return
        cm += 1
        cnt += 1
        if cm > N:
            break
    return

def run():
    people_move()
    spin()
    
#게임 시작
flag = 0
for _ in range(K):
    run()
    for r,c,k in people:
        if k == 0:
            flag = 0
            break
        flag = 1

    if flag == 1:
        break

print(sum(move))
print(dest[0]+1,dest[1]+1)