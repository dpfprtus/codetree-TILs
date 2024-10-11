#n*n 격자 -> 각자의 무기
#빈 격자에 플레이어 위치 -> 초기 능력치는 모두 다르다

#노란색 -> 플레이어 번호
#플레이어의 빨간 숫자 -> 초기 능력치
#총의 빨간 숫자 -> 공격력

#라운드
    #1. 첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한칸 이동
        #격자를 벗어날 경우 정반대 방향으로 방향을 바꾸어서 1만큼 이동

    
    #2. 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지확인
        #총이 있는 경우 : 총을 획득(가지고 잇는 것과 비교해 공격력이 큰 것을 획득) 
            #나머지 총은 격자에 둔다.

    #3. 이동한 방향에 플레이어가 있는 경우 -> 파이팅
        #초기 능력치 + 총의 공격력이 큰 플레이어가 이김
            #같은 경우 초기 능력치가 큰 플레이어가 이김
            #이긴 플레이어는 초기 능력치 - (갖고 있는 총의 공격력의 합) = 포인트
        
        #진 플레이어 -> 갖고 있는 총을 격자에 내려놓고, 방향대로 한 칸 이동
            #이동하려는 칸에 플레이어가 있거나, 범의 밖이면 오른쪽으로 90도씩 회전하며 빈칸이 보이는 순간 이동
                #해당 칸에 총이 있다면 가장 공격력이 높은 총읠 획득하고 나머지 총들은 격자에 내려 놓음.

        #이긴 플레이어 -> 승라히나 칸에 있는 총과 들고 잇던 총 중 가장 공격력이높은 총을 획득하고, 나머지 총은 격자에 내려 놓음.

#각 플레이어들이 획득한 포인트 출력




#총이 두개 이상 놓여 있을 수 있나?
#총이 없는 플레이어와 싸우는 경우

n,m,k = map(int,input().split())



maps = []

for i in range(n):
    a = list(map(int,input().split()))
    maps.append([[j] for j in a])

players = []
player_point = [0]*m
player_gun = [[] for _ in range(m)]
for i in range(m):

    #x,y 위치 d 방향 s초기 능력치(모두 다름), #0 1 2 3, 상 우 하 좌
    x,y,d,s = map(int,input().split())
    x -= 1
    y -= 1
    players.append([x,y,d,s])

def check_range(x,y):
    return 0<= x < n and 0<= y < n


#상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def check_player_maps(x,y,idx):
    for play_idx in range(len(players)):
        if idx == play_idx:
            continue
        player_x = players[play_idx][0]
        player_y = players[play_idx][1]
        if player_x == x and player_y == y:
            return play_idx

    return -1
 

def fight(play_idx,player_map_idx):

    player_x,player_y,d1,player_s = players[play_idx]
    player_attack = sum(player_gun[play_idx]) + player_s
    
    map_player_x,map_player_y,d2,map_player_s = players[player_map_idx]
    map_player_attack = sum(player_gun[player_map_idx]) + map_player_s

    win_player_idx = -1
    lose_player_idx = -1

    if player_attack > map_player_attack:
        win_player_idx = play_idx
        lose_player_idx = player_map_idx

    elif player_attack == map_player_attack:
        if player_s > map_player_s:
            win_player_idx = play_idx
            lose_player_idx = player_map_idx
        else:
            win_player_idx = player_map_idx
            lose_player_idx = play_idx
    else:
        win_player_idx = player_map_idx
        lose_player_idx = play_idx
    return (win_player_idx,lose_player_idx)

def move_lose_player(player_idx):
    x,y,d = players[player_idx][0], players[player_idx][1], players[player_idx][2]

    for _ in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not check_range(nx,ny) or check_player_maps(nx,ny,player_idx) != -1:
            d = (d+1)%4
            players[player_idx][2] = d
            continue

        players[player_idx][0] = nx
        players[player_idx][1] = ny

        #이동 총이 있는 경우
        if maps[nx][ny][0] != 0:
            max_gun = max(maps[nx][ny])
            player_gun[player_idx].append(max_gun)
            maps[nx][ny].remove(max_gun)
            if len(maps[nx][ny]) == 0:
                maps[nx][ny].append(0)
      
        break
    
        

def move_player(play_idx):
    global player_point
    x,y,d,s = players[play_idx]

    #방향대로 한 칸 이동
    nx,ny = x + dx[d],y + dy[d]
    if not check_range(nx,ny):
        nx,ny = x + dx[(d+2)%4], y + dy[(d+2)%4]
        players[play_idx][2] = (d+2)%4

    players[play_idx][0] = nx
    players[play_idx][1] = ny

    #총이 있는지,플레이어가 있는지 확인하고 공격력이 큰 것을 픽
    player_map_idx = check_player_maps(nx,ny,play_idx)

    if maps[nx][ny][0] != 0 and player_map_idx == -1:

        if len(player_gun[play_idx]) == 0:
            player_gun[play_idx].append(maps[nx][ny][0])
            maps[nx][ny][0] = 0

            
        else:
            #맵의 총이 공격력이 높다면 교환
            max_gun_maps = max(maps[nx][ny])
    
            if max(player_gun[play_idx]) < max_gun_maps:
                tmp = player_gun[play_idx]
                player_gun[play_idx] = [max_gun_maps]

                maps[nx][ny].remove(max_gun_maps)
                maps[nx][ny].extend(tmp)

                if len(maps[nx][ny]) == 0:
                    maps[nx][ny].append(0)
    
    elif player_map_idx != -1:
 
        win_player_idx, lose_player_idx = fight(play_idx,player_map_idx)
    
        #포인트 획득
        winner = sum(player_gun[win_player_idx])+players[win_player_idx][3]
        loser = sum(player_gun[lose_player_idx])+players[lose_player_idx][3]
        player_point[win_player_idx] += abs(winner-loser)
        
        #진 플레이어 총을 격자에 내려 놓음.
        maps[nx][ny].extend(player_gun[lose_player_idx])
        player_gun[lose_player_idx] = []
        move_lose_player(lose_player_idx)

        #이긴 플레이어는 칸에 떨어져있는 총을 비교
        max_gun = max(maps[nx][ny])
        max_player_gun = 0

        if len(player_gun[win_player_idx]) != 0:
            max_player_gun = max(player_gun[win_player_idx])

        if max_gun > max_player_gun:
            tmp = player_gun[win_player_idx]
            player_gun[win_player_idx] = [max_gun]
            maps[nx][ny].remove(max_gun)
            maps[nx][ny].extend(tmp)

            if len(maps[nx][ny]) == 0:
                maps[nx][ny].append(0)
        
        else:
            if max_player_gun != 0:
                player_gun[win_player_idx].remove(max_player_gun)
                maps[nx][ny].extend(player_gun[win_player_idx])
                player_gun[win_player_idx] = [max_player_gun]


    return

#라운드 진행
for i in range(k):

    for play_idx in range(len(players)):
        move_player(play_idx) 

print(*player_point,end=" ")