#체스판
 #1,1부터 시작 -> 함정, 벽(체스판 밖도 벽)

 #기사
    #초기위치: (r,c)
    #r,c를 좌측상단으로 하여 HxW 크기의 직사각형 방패를 가짐
    #체력 k

    #이동
    #상하좌우 한칸
    #이동하는 칸에 기사가 있다면 그 기사도 연쇄적으로 한 칸 밀려남
    #기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없음 **
    #사라진 기사는 명령 수행 불가

    #대결 대미지
    #기사는 다른 기사를 밀침 -> 밀려난 기사는 피해를 입는다. -> WxH 직사각형에 놓인 함정의 수만큼 피해를 입음.
    #체력 고갈 -> 죽음
    #명령을 받은 기사는 피해를 입지 않음.
    #기사들은 모두 밀린 이후에 대미지를 받음. (밀린 위치에 함정이 없으면 피해x)

#Q번의 대결 이후 생존한 기사들이 받은 대미지의 합을 출력

L,N,Q = map(int,input().split())

#0이면 빈칸, 1이면 함정, 2면 벽
chess = [list(map(int,input().split())) for _ in range(L)]

knight_map = [[-1]*L for _ in range(L)]

#r,c,h,w,k -> h가 세로, w가 가로
knight = []
end = [0]*N

answer = 0

knight_num_chess = 0
for _ in range(N):
    r,c,h,w,k = map(int,input().split())
    r-=1
    c-=1
    knight.append([r,c,w,h,k])
    for i in range(r,r+h):
        for j in range(c,c+w):
            knight_map[i][j] = knight_num_chess
    knight_num_chess += 1

order = []

#i사라진 기사의 번호일 수 있다.
#d : 0,1,2,3 -> 위쪽,오른쪽, 아래쪽, 왼쪽
for _ in range(Q):
    i,d = map(int,input().split())
    i-=1
    order.append([i,d])

def check_range(x,y):
    return 0<= x < L and 0<= y < L

dr = [-1,0,1,0]
dc = [0,1,0,-1]



#r,c,h,w,k -> h가 세로, w가 가로


#기사가 밀칠 수 있는지 체크
def knight_move_check(k,r,c,w,h,d):

    for i in range(r,r+h):
        for j in range(c,c+w):
            i += dr[d]
            j += dc[d]
       
            if not check_range(i,j) or chess[i][j] == 2:
                return False
            if knight_map[i][j] != -1 and knight_map[i][j] != k:
                i = knight[knight_map[i][j]][0]
                j = knight[knight_map[i][j]][1]
                w = knight[knight_map[i][j]][2]
                h = knight[knight_map[i][j]][3]
                knight_move_check(knight_map[i][j],i,j,w,h,d)
    return True

#함정 체크하고 함정만큼 나이트 체력 깎기
def check_hole(knight_num,r,c,w,h):
    global knight
    global answer
    cnt = 0
    for i in range(r,r+h):
        for j in range(c,c+w):
            if chess[i][j] == 1:
                cnt += 1

    knight[knight_num][4] -= cnt
    answer += cnt
    if knight[knight_num][4] <= 0:
        end[knight_num] = 1
        r = knight[knight_num][0]
        c = knight[knight_num][1]
        w = knight[knight_num][2]
        h = knight[knight_num][3]
        for i in range(r,r+h):
            for j in range(c,c+w):
                knight_map[i][j] = -1

#기사 밀리는거
def knight_move(first_knight_num,knight_num,r,c,w,h,d):
    
    for i in range(r,r+h):
        for j in range(c,c+w):
            i += dr[d]
            j += dc[d]
            if knight_map[i][j] != knight_num and knight_map[i][j] != -1:
                ii = knight[knight_map[i][j]][0]
                jj = knight[knight_map[i][j]][1]
                wi = knight[knight_map[i][j]][2]
                hi = knight[knight_map[i][j]][3]
                knight_move(first_knight_num,knight_map[i][j],ii,jj,wi,hi,d)
            knight_map[i][j] = knight_num
            i -= dr[d]
            j -= dc[d]
            knight_map[i][j] = -1

    if knight_num != first_knight_num:
        check_hole(knight_num,r,c,w,h)
    return

#기사 이동 명령
def knight_order(i,d):
    r,c,w,h,k = knight[i]
   
    if knight_move_check(i,r,c,w,h,d):
        knight_move(i,i,r,c,w,h,d)


for i,d in order:
    if end[i] == 1:
        continue
    knight_order(i,d)

print(answer)