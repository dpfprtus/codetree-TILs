from collections import deque

#n*n 격자 위
#m명 m분
# 베이스캠프 -> 편의점 이동(목표로하는 편의점이 다 다름)

#행동
    #1.본인이 가고 싶은 편의점 방향으로 1칸
        #최단거리, 상/좌/우/하
    
    #2. 편의점 도달 시 편의점에서 멈추게되고, 다른 사람은 이 칸 이동 못함
        #격자 사람들 모두 이동 후 해당 칸 false
    
    #3. 현재 시각 t -> t<=m 이면 t번 사람은 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들억마
        #베이스캠프 -> 행이 작고, 열이 작은게 우선, 이동 소요시간 x
        #이 베이스캠프에 누가들어간 후에 아무도 이제 해당 베이스캠프에 들어갈 수 없음

#조건
    #편의점과, 베이스 캠프 위치는 겹치지 않는다.
    #이미 사람들이 도착한 편의점이나 출발한 적 있는 베이스캠프의 경우 움직일 때 절대 지나갈 수 없음.

#출력
    #모든 사람이 편의점에 도착하는 시간 출력
    #원하는 사람이 편의점에 도달하지 못하는 경우는 없음
    #동일한 칸에 둘 이상의 사람이 위치할 수 있음.
n,m = map(int,input().split())

maps = []
base_camp = []

#1이면 베이스캠프, 0이면 빈 공간
for i in range(n):
    a = list(map(int,input().split()))

    for j in range(n):
        if a[j] == 1:
            base_camp.append([i,j,0])

    maps.append(a)

#순서가 같음
store = []
goal_store = []
people = [[-1,-1,0] for _ in range(m)]


for _ in range(m):
    #편의점 정보
    a,b = map(int,input().split())
    a-=1
    b-=1
    store.append([a,b])

dx = [-1,0,0,1]
dy = [0,-1,1,0]

time = 1

def check_range(x,y):
    return 0<= x <n and 0<= y < n


#최단거리를 찾고 움직여야 하는 좌표 반환
def go_store(people_x,people_y,store_x,store_y):
    
    minimum_distance = 1000

    goal_x = -1
    goal_y = -1

    for i in range(4):
        nx = people_x + dx[i]
        ny = people_y + dy[i]
        a1,b1 = nx,ny
        visited = [[0]*n for _ in range(n)]
        q = deque([(nx,ny)])    
        
        flag = 0
        if not check_range(nx,ny) or maps[nx][ny] == -2:
            continue
        visited[nx][ny] = 1
        if (nx,ny) == (store_x,store_y):
            return (nx,ny)

        while q:
            nx,ny = q.popleft()
            for j in range(4):
                nnx = nx + dx[j]
                nny = ny + dy[j]
            
                if not check_range(nnx,nny) or visited[nnx][nny] != 0 or maps[nnx][nny] == -2:
                    continue
                
                visited[nnx][nny] = visited[nx][ny] + 1
                q.append((nnx,nny))

                if (nnx,nny) == (store_x,store_y):
                    if visited[nnx][nny] < minimum_distance:
                        minimum_distance = visited[nnx][nny]
                        goal_x,goal_y = a1,b1
                        flag = 1
                        break
            if flag == 1:
                break

    return (goal_x,goal_y)
                

#가고 싶은 편의점과 가장 가까운 베이스 캠프 계산
def minimum_distance(store_x,store_y):

    #행이 작고 열이 작은 거 우선
    base_camp.sort(key=lambda x:(x[0],x[1]))
    minimum_distance = 1000
    minimum_basecamp_x = -1
    minimum_basecamp_y = -1

    goal_idx = 0
    for idx,(x,y,c) in enumerate(base_camp):
        if c == 1:
            continue
        q = deque([(x,y)])
        visited = [[0]*n for _ in range(n)]
        visited[x][y] = 1
        flag = 0
        while q:
            r,c = q.popleft()
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]

                if not check_range(nr,nc) or visited[nr][nc] != 0 or maps[nr][nc] == -2:
                    continue
                
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))

                if (nr,nc) == (store_x,store_y):
                    if visited[nr][nc] < minimum_distance:
                        minimum_distance = visited[nr][nc]    
                        minimum_basecamp_x,minimum_basecamp_y = x,y
                        goal_idx = idx
                        flag = 1
                        break
            if flag == 1:
                break
    return (minimum_basecamp_x,minimum_basecamp_y,goal_idx)

#사람이 도착한 편의점 좌표를 -2로 변환해 못가게 함.
def check_store_basecamp():
    global base_camp
    global goal_store
    for i in range(n):
        for j in range(n):
            if (i,j) in goal_store:
                maps[i][j] = -2

    for a,b,c in base_camp:
        #사람이 갔떤 베이스 캠프라면
        if c == 1:
            maps[a][b] = -2

def check_time():

    for a,b,c in people:
        if c == 0:
            return False
    return True
    

while True:
    
    check_store_basecamp()

    for idx,(people_x,people_y,c) in enumerate(people):
        #편의점 도착한 경우
        if c == 1 or idx+1 > time:
            continue

        if (people_x,people_y) != (-1,-1):
            store_x = store[idx][0]
            store_y = store[idx][1]
  
        #액션 1
            goal_x,goal_y = go_store(people_x,people_y,store_x,store_y)
            people[idx][0] = goal_x
            people[idx][1] = goal_y


        #액션 2
        #편의점 도착 시 이동 정지
        if (people_x,people_y) != (-1,-1) and (goal_x,goal_y) == (store_x,store_y):
            
            #사람이 도착한 편의점의 좌표를 저장
            goal_store.append([goal_x,goal_y])
            people[idx][2] = 1 
            continue 

        if time <= m and idx+1 == time:
      
            (basecamp_x,basecamp_y,goal_idx) = minimum_distance(store[idx][0],store[idx][1])
            people[idx][0] = basecamp_x
            people[idx][1] = basecamp_y
            base_camp[goal_idx][2] = 1


        #액션 3
    if check_time():
        print(time)
        break
    time += 1