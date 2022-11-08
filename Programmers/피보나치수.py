def solution(n):   
    answer = [0,1] #answer[0]=0, answer[1]=1, 인덱스가 곧 n이 된다
    for i in range(2, n+1):
        answer.append(answer[i-1]+answer[i-2]) #F(n)=F(n-1)+F(n-2)
        #F(n)을 리스트의 인덱스를 사용해서 넣어준다.
    return answer[-1]%1234567

#Other Answer
def fibonacci(num):
    a,b = 0,1 # f(0),f(1)이 0,1 로 시작하고
    for i in range(num):
        a,b = b,a+b # 한 칸씩 밀려나는 느낌으로 치환해줌
    return a