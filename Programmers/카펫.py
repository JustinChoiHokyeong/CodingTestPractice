'''
return [가로, 세로] =[a,b]

1. 가로 길이는 세로 길이보다 크거나 같다 
a>=b

2. 테두리 1줄은 갈색으로 칠해야 있고, 중앙은 노란색으로 채워져 있다.
brown = a*b - (a-2)*(b-2) = ab - ab + 2a + 2b -4 = 2a + 2b -4
yellow = (a-2)*(b-2) = ab -2a -2b + 4
brown + yellow = ab이다


3. 
brown 과 yellow 갯수는 매개변수로 각각 전달된다.

'''

def solution(brown, yellow):
    total=brown+yellow
    for a in range(1,total+1):
        if total%a==0:
            b=int(total/a)
            if a>=b:
                if brown==2*a+2*b-4:
                    return [a,b]
# a>=b , brown = 2a + 2b -4 , ab=total 모든 조건을 걸고 1~total까지 돌리면서 찾았다.

print(solution(24,24))


# Other Answer
    
def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0: #나머지가 0이 아니면 다음 턴으로 바로 넘어간다
            continue 
        # 나머지 0이면 위 조건문으로 안들어가고 여기로 와서 동작을 실행한다.
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)