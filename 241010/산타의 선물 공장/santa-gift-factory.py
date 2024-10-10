from collections import deque

#공장에서 순서대로 q개의 명령 수행
# 일 종류 5가지

    #1. 공장 설립
        #m개의 벨트를 설치하고, 각 벨트 위에 정확히 n/m개의 물건을 놓아 n개의 물건을 준비
        #각 물건에는 고유한 번호와 무게가 적혀있음. -> 번호는 상자마다 다르지만, 무게가 동일할 수 있음
    

    
    #3.물건 제거
        #고유 아이디 r_id가 있다면 해당 벨트에서 제거 그렇지 않으면 -1 출력
    
    #4. 물건 확인
        #고유 아이디 f_id -> 벨트위에 있다면 벨트 번호 출력, 없으면 -1 출력
        # 상자가 있는경우, 해당 상자 위에 있는 모든 상자를 전부 앞으로 "순서대로" 가져옴

    
    #5. 벨트 고장
        #벨트 번호 b_num이 주어짐, -> 해당 벨트는 다신 사용 불가
        #오른쪽 벨트부터 조회하며, 아직 고장 나지 않은 최초의 벨트 위로 b_num 벨트에 놓여있던
        #상자들을 아래에서부터 순서대로 하나씩 옮겨줌
        #m번 벨트까지 봤는데 고장나지 않은 벨트가 없다면, 다시 1번부터 순서대로 벨트 확인
            #-> b_num을 제외한 벨트 중 최소 하나 이상이 정상임. -> 모든 벨트가 망가지는 경우 없음.
        #만약 b_num이 이미 망가져있다면, -1 출력 그렇지 않다면 b_num 출력(고장 잘 처리함)

q = int(input())
break_belt_list = []
def make_belt(n,m,combo):    

    belt_q = deque([])
    for i in range(0,n,n//m):
        belt_q.append(deque(combo[i:i+n//m]))

    return belt_q

def down(weight):
    global belt_q
    global break_belt_list
    global n
    global m
    box_list = []
    for i in range(m):
        if i in break_belt_list:
            continue
        if len(belt_q[i]) != 0 and belt_q[i][0][1] <= weight:
            box_id,box_weight = belt_q[i].popleft()
            box_list.append([box_id,box_weight])
            continue
        elif len(belt_q[i]) == 0:
            continue
        belt_q[i].rotate(1)
        
    return box_list

def remove(r_id):
    global m
    global belt_q

    for i in range(m):
        if i in break_belt_list:
            continue
        if len(belt_q[i]) == 0:
            continue
        for idx,(box_id,weight) in enumerate(belt_q[i]):
            if box_id == r_id:
                if idx == 0:
                    belt_q[i].popleft()
                    return True
                else:
                    #성능 개선 여지 잇음
                    belt_q[i].remove(belt_q[i][idx])
                    return True
    return False

def check_box(f_id):
    global belt_q
    global m
    global n

    for i in range(m):
        if i in break_belt_list:
            continue
        if len(belt_q[i]) == 0:
            continue
        for idx,(box_id,weight) in enumerate(belt_q[i]):
            if  box_id == f_id:
                if idx == 0:
                    first = belt_q[i].popleft()
                    belt_q[i].append(first)
                    return i
                elif idx == len(belt_q[i])-1:
                    return i
                else: 
                    belt_q[i].rotate(idx-1)
                    return i
    return -1
            
def belt_break(b_num):
    
    global belt_q
    global break_belt_list
    global n
    global m
    b_num -= 1
    break_belt_list.append(b_num)
    next_belt = b_num
    while True:
        next_belt = (next_belt+1) % m

        if next_belt in break_belt_list:
            continue

        belt_q[next_belt].extend(belt_q[b_num])
        belt_q[b_num] = deque([])
        return


belt_q = deque([])
n,m = 0,0
for k in range(q):
    order = list(map(int,input().split()))

    #공장 설립,출력 x
    if order[0] == 100:
        #m개 벨트, n개 선물
        n,m = order[1],order[2]
        present = order[3:n+3]
        weight = order[n+3:]
        combo = list(map(list,zip(present,weight)))
        belt_q = make_belt(n,m,combo)

        #벨트에 선물 올림

    #물건 하차
    elif order[0] == 200:
        box_list = down(order[1])
        down_weight = 0
   
        for box_id,weigth in box_list:
            down_weight += weigth
        print(down_weight)

    #물건 제거
    elif order[0] == 300:

        remove_bool = remove(order[1])
        if remove_bool == True:
            print(order[1])
        else:
            print(-1)
        
    #물건 확인
    elif order[0] == 400:
        check_bool = check_box(order[1])
        if check_bool != -1:
            print(check_bool+1)
        else:
            print(-1)

    #벨트 고장
    elif order[0] == 500:
        if order[1]-1 in break_belt_list:
            print(-1)
        else:
            belt_break(order[1])
            print(order[1])