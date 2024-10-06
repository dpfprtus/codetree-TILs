#루돌프가 산타를 박치기하며 선물 배달 방해
#산타들은 루돌프를 잡아야 함.

#배열 최상단 1,1 -> r,c

#매 턴마다 루돌프와 산타가 한번씩 움직임, 루독프가 한번 움직인뒤, 1~p번 산타까지 순서대로 움직임
#기절해 있거나 격자 밖으로 빠져 탈락한 산타는 움직일 수 없음.


##루돌프
#가장 가까운 산타를 향해 1칸 돌진(탈락하지 않은 산타에게로)
#->가장 가까운 산타가 2명이상이면, r좌표가 큰 산타를 향해 돌진, r도 같으면 c좌표가 큰 산타에게 돌진
#8칸 중 1칸으로 돌진하는 것

##산타
#루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
#움직일 수 있는 칸이 없으면 산타는 움직이지 않음
#다른 산타나 게임판 밖으로 이동금지
#칸이 있더라도 루돌프로부터 가까워질 수 있는 방법이 없다면 움직이지 않음
#상하좌우 4칸만 움직일 수 있음. 우선순위 상 -> 우 -> 하 -. 좌

##충돌
#루돌프가 움직여 충돌이 일어난 경우 : 산타는 C만큼 점수를 얻고, 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀림
#산타가 움직여 충돌이 일어난 경우 : 산타는 D만큼 점수롤 얻고 산타는 자신이 이동해온 반대 방향으로 D칸 만큼 밀림
#밀려나는 과정에선 충돌 x
#밀려난 위치가 게임판 밖이면 산타는 게임에서 탈락
#밀려난 칸에 산타가 있으면 상호작용
    #충돌후 밀려난 칸에 산타가 잇으면 그 산타는 해당 방향으로 1칸 밀림 -> 연쇄적

##기절
#산타는 루돌프와 충돌 후 1턴 기절
#기절한 도중 충돌이나 상호작용으로 밀려날 수 있음
#루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있음

#게임종료
#P명의 산타가 모두 게임에 탈락하면 게임 종료
#매 턴 이후 아직 탈락하지 않은 산타들에게 1점 추가점수 부여

N,M,P,C,D = map(int,input().split())

# P 산타의 수, c 루돌프의 힘(밀려나는 거리), D 산타의 힘

#루돌프 -1, 산타는 번호

maps = [[0]*N for _ in range(N)]
#루돌프
a,b = map(int,input().split())
rudolf = [a-1,b-1,0]

#산타 점수
score = [0]*(P)

#기절 상태
honsu = [[0,0] for _ in range(P)]

#게임 종료 상태
end = [0]*(P)

#산타
santa = [[0,0,0] for _ in range(P)]
for _ in range(P):
    a,b,c = map(int,input().split())
    #위치, 방향
    santa[a-1] = [b-1,c-1,0]

def check_range(x,y):
    return 0 <= x < N and 0 <= y < N

#루돌프와 가장 가까운 산타 계산
def cal_distance():
    result = float("inf")
    distance = []
    for idx,(a,b,c) in enumerate(santa):
        if end[idx] == 1:
            continue
        tmp = abs(rudolf[0]-a)**2+abs(rudolf[1]-b)**2
        if result >= tmp:
            distance.append((tmp,a,b))
    distance.sort(key=lambda x:(x[0],-x[1],-x[2]))
    return distance


def rudolf_move(ik):
    global rudolf
    global santa
    global honsu
    global end
    distance = cal_distance()
    a,b = distance[0][1],distance[0][2]
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,-1,-1,-1,0,1,1,1]
    result = float("inf")
    direction = []

    for k,(i,j) in enumerate(zip(dr,dc)):

        distance = abs(rudolf[0]+i-a)**2+abs(rudolf[1]+j-b)**2
        if result >= distance:
            result = distance
            direction = [rudolf[0]+i,rudolf[1]+j]
            rudolf[2] = k
    rudolf[0] = direction[0]
    rudolf[1] = direction[1]
    
 
    #루돌프와 산타 충돌
    
    for k,(r,c,d) in enumerate(santa):
        if rudolf[0] == r and rudolf[1] == c:
            score[k] += C
            santa[k][2] = rudolf[2]
            
            santa[k][0] = santa[k][0]+ dr[santa[k][2]]*C
            santa[k][1] = santa[k][1]+ dc[santa[k][2]]*C
            honsu[k] = [ik+2,1]
            if not check_range(santa[k][0],santa[k][1]):
                end[k] = 1
                continue

            while True:
                flag = 0
                for i,(r,c,d) in enumerate(santa):

                    if i == k or end[i] == 1:
                        continue
                    if santa[k][0] == r and santa[k][1] == c:
                        santa[i][0] += dr[santa[k][2]]
                        santa[i][1] +=  dc[santa[k][2]]
                        santa[i][2] = santa[k][2]
                        k = i
                        flag = 1
                        #죽으면
                        if not check_range(santa[i][0],santa[i][1]):
                            end[i] = 1
                            flag = 0
                            break
                if flag == 0:
                    break
            

def santa_move(iok):
    global santa
    global rudolf
    global honsu
    global end
    #상,우,하,좌
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    for k,(a,b,d) in enumerate(santa):
        result = float("inf")
        tmp = []
        if honsu[k][1] == 1 or end[k] == 1:
            continue
        #루돌프와의 거리
        ax = abs(a-rudolf[0])**2+abs(b-rudolf[1])**2
        
        for t,(i,j) in enumerate(zip(dr,dc)):
            flag = 0
            if not check_range(a+i,b+j):
                continue

            for tp in range(P):
                if end[tp]==0 and a+i == santa[tp][0] and b+j == santa[tp][1]:
                    flag = 1
                    break
            if flag == 1:
                continue
            distance = abs(a+i-rudolf[0])**2+abs(b+j-rudolf[1])**2
            if ax < distance:
                continue

            if result > distance:
                result = distance
                tmp = [a+i,b+j,t]
  

        if len(tmp) == 0:
            continue
        santa[k] = tmp
    
        #충돌
        if santa[k][0] == rudolf[0] and santa[k][1] == rudolf[1]:

    
            score[k] += D
            santa[k][2] = (santa[k][2]+2) % 4
            santa[k][0] = santa[k][0]+ dr[santa[k][2]]*D
            santa[k][1] = santa[k][1] + dc[santa[k][2]]*D
            honsu[k] = [iok+2,1]
 
            if not check_range(santa[k][0],santa[k][1]):
                end[k] = 1

                continue
            #연쇄 충돌
            while True:
                flag = 0
         
                for i,(r,c,d) in enumerate(santa):
                    if i == k or end[i] == 1:
                        continue
                    if santa[k][0] == r and santa[k][1] == c:
                        santa[i][0] += dr[santa[k][2]]
                        santa[i][1] +=  dc[santa[k][2]]
                        k = i
                        flag = 1
                        #죽으면
                        if not check_range(santa[i][0],santa[i][1]):
                            end[i] = 1
                            flag = 0
                            break
                if flag == 0:
                    break

                            
                    
#게임 턴
for i in range(M):
    for idx,(t,k) in enumerate(honsu):
        if t == i:
            honsu[idx][1] = 0
    rudolf_move(i)
    santa_move(i)
    if 0 not in end:
        break
    for i in range(P):
        if end[i] == 0:
             score[i] += 1
        
    

for i in range(P):
    print(score[i],end=" ")