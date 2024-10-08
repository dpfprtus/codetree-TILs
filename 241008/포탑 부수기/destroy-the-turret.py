from collections import deque

#모든 위치에 포탑 존재

#포탑
    #공격력 존재 -> 상황에 따라 공격력이 늘어나거나 줄어들음
    #공격력 0이하 -> 포탑 부서짐

#턴제
    #가장 약한 포탑이 공격자로 선정 -> N+M만큼 공격력이 증가
    #우선순위(가장 약한 포탑)
        #1. 공격력이 가장 약한 포탑
        #2. 가장 최근에 공격한 포탑(모든 포탑은 시점 0에 공격한 경험이 있음)
        #3. 행과 열의 합이 가장 큰 포탑
        #4. 열이 가장 큰 포탑
    
    #공격포탑은 자신을 제외한 가장 강한 포탑을 공격
        #우선순위(가장 강한 포탑)
        #1. 공격력이 가장 강한 포탑
        #2. 가장 공격한지 오래된 포탑
        #3. 행과 열의 합이 가장 작은 포탑
        #4. 열이 가장 작은 포탑

    #공격
        #레이저 공격
        #1. 상하좌우 4개 방향
        #2. 부서진 포탑이 있는 위치는 지날 수 없음
        #3. 가장자리에서 막힌 방향으로 진행하면 반대편으로 나옴.
        #공격대상 - 공격위치 최단 경로로 공격
            #1. 경로가 없으면 포탄 공격
            #2. 경로가 같으면 -> 우/하/좌/상
            #3. 공격대상은 공격력만큼 공격력이 깎임
            #4. 레이저 경로에 있는 포탑도 공격을 받게 됨. -> 공격력의 절반 만큼 /2로 나눈 몫

        #포탄 공격
        #1. 주위 8개에 있는 포탑도 피해를 받음 -> 공격력의 절반만큼(공격자는 영향 X)
            #만약 가장자리에 포탄이 떨어지면, 레이저 이동처럼 포탄의 추가 피해가 반대편 격자에 영향을 미침

    #포탑 정비
        #1. 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력이 1씩 올라감(공격자, 피해자도 아닌 포탑)

    
#남아있는 포탑 중 가장 강한 포탑의 공격력을 출력

N,M,K = map(int,input().split())

potap = []
maps = []

cnt = 0
for i in range(N):
    a = list(map(int,input().split()))
    for j in range(M):
        if a[j] != 0:
            #포탑 기록
            
            potap.append([i,j,a[j],0,cnt,0])
            cnt += 1
    maps.append(a)


def pick_attack():
    potap_tmp = sorted(potap,key=lambda x :(-x[5],x[2],-x[3],-(x[0]+x[1]),-x[1]))
    return potap_tmp[0]

def pick_defence():
    potap_tmp = sorted(potap,key=lambda x :(-x[5],-x[2],x[3],x[0]+x[1],x[1]))
    return potap_tmp[0]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

#포탑 x,y,공격력,공격한 턴,포탑 번호

def rager(attack,defence,k,attack_tmp):
    global potap
    q = deque([(attack[0],attack[1])])
    visited = [[[] for _ in range(M)] for _ in range(N)]

    attack[2] += (N+M)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N:
                nx = 0
            if nx < 0:
                nx = N-1
            if ny >= M:
                ny = 0
            if ny < 0:
                ny = M-1
   
            if maps[nx][ny] <= 0 or len(visited[nx][ny]) != 0:
                continue
            q.append((nx,ny))
            visited[nx][ny] = [x,y]
            
                        #공격 개시

            if nx == defence[0] and ny == defence[1]:
          
                potap[defence[4]][2] -= attack[2]
                potap[attack[4]][2] += (N+M)
                maps[attack[0]][attack[1]] += (N+M)
                #공격한 턴 입력
                potap[attack[4]][3] = k+1
                maps[defence[0]][defence[1]] -= attack[2]
                
                if potap[defence[4]][2] <= 0:
                    potap[defence[4]][5] = -1

                a,b = nx,ny

                while (a,b) != (attack[0],attack[1]):
        
                    a,b = visited[a][b]
                   
                    if (a,b) == (attack[0],attack[1]):
                        break
                    for a1,b1,c1,d1,e1,f1 in potap:
                        if f1 == -1:
                            continue
                        if (a1,b1) == (a,b):
                            attack_tmp.append(e1)
                            potap[e1][2] -= attack[2]//2
                            maps[potap[e1][0]][potap[e1][1]] -= attack[2]//2
                            if potap[e1][2] <= 0:
                                potap[e1][5] = -1
                            break
                return attack_tmp
    return False
            

def potan(attack,defence,k,attack_tmp):
    
    dx = [-1,0,1,1,1,0,-1,-1]
    dy = [-1,-1,-1,0,1,1,1,0]

    x,y = defence[0],defence[1]

    attack[2] += (N+M)
    potap[attack[4]][2] += (N+M)

    maps[attack[0]][attack[1]] += (N+M)
    potap[attack[4]][3] = k+1

    potap[defence[4]][2] -= attack[2]
    maps[defence[0]][defence[1]] -= attack[2]

    if potap[defence[4]][2] <= 0:
        potap[defence[4]][5] = -1

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if (nx,ny) == (attack[0],attack[1]):
            continue
        
        if nx < 0 and ny < 0:
            nx = N-1
            ny = M-1
        if nx < 0 and ny >= M:
            nx = N-1
            ny = 0
        if nx >= N and ny < 0:
            nx = 0
            ny = M-1
        if nx >= N and ny >= M:
            nx = 0
            ny = 0
        elif ny < 0:
            ny = M-1
        elif nx >= N:
            nx = 0
        elif nx < 0:
            nx = N-1
        elif ny >= M:
            ny = 0

        if maps[nx][ny] <= 0:
            continue
        
        for a1,b1,c1,d1,e1,f1 in potap:
            if (nx,ny) == (a1,b1):
                potap[e1][2] = potap[e1][2] - attack[2]//2
                maps[a1][b1] = potap[e1][2] - attack[2]//2
                attack_tmp.append(e1)
                if potap[e1][2] <= 0:
                    potap[e1][5] = -1
                break
    return attack_tmp

def run(i):
    attack = pick_attack()
    defence = pick_defence()
    if (attack[0],attack[1]) == (defence[0],defence[1]):
        return
    attack_0 = [i for i in attack]
    defence_0 =[i for i in defence]
    attack_1 = [i for i in attack]
    defence_1 = [i for i in defence]

    attack_tmp = []
    attack_tmp = rager(attack_0,defence_0,i,[])
    if attack_tmp == False:
        attack_tmp = potan(attack_1,defence_1,i,[])

    cnt = 0
    for j in range(len(potap)):
        if potap[j][5] == 0:
            cnt += 1
    if cnt == 1:
        return
        
    for i in range(len(potap)):
        if potap[i][4] in attack_tmp:
            continue
        if potap[i][4] == attack[4] or potap[i][4] == defence[4] or potap[i][5] == -1:
            continue
        potap[i][2] += 1
        maps[potap[i][0]][potap[i][1]] += 1 
    return 


for i in range(K):

    run(i)
    cnt = 0
    for j in range(len(potap)):
        if potap[j][5] == 0:
            cnt += 1
    if cnt == 1:
        break
    
    

potap.sort(key=lambda x :(-x[5],-x[2]))
print(potap[0][2])