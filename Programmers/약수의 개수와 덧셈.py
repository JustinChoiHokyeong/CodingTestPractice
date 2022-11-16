'''
약수의 개수가 짝수인 수는 더하고
약수의 개수가 홀수인 수는 빼서
결과값 리턴
'''




#약수 갯수 구하기
n=10
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)


left=24;right=27

def solution(left, right):
    result=0
    for n in range(left, right+1):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count%2==0:
            result+=n
        else:
            result-=n
    return result

print(solution(24,27))

#Other Answer
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''
제곱근을 씌웠을 때도 정수로 나타나는 수는 약수의 갯수가 반드시 홀수이다.
그래서 for 문으로 돌면서 홀수면 빼고 짝수면 더햇다
'''