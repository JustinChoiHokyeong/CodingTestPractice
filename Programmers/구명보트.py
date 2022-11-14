'''

'''


# sum=0
# count=0
# for i in range(len(people)):
#     if i==len(people)-1:
#         count+=1
#     elif people[i]+people[i+1]>limit:
#         count+=1
# print(count)

people=[70, 50, 80]
limit=100

def solution(people, limit):
    cnt=0
    sum=0
    for i in range(len(people)):
        if sum+people[i]>=limit:
            cnt+=1
            sum=0
        elif sum+people[i]<limit:
            sum+=people[i]
            continue
    return cnt

print(solution(people, limit))

# 순서대로 타는게 아님, 그냥 최대한 적게 카운팅되면 됌
# Other Answer
def solution(people, limit) :
    answer = 0
    people.sort() #오름차순으로 정렬시켜서 
    #인덱스 번호를 사용해서
    a = 0 #가장 작은 수와
    b = len(people) - 1 #가장 큰 수부터 조사한다
    while a < b : #두 인덱스 숫자가 같아질 때까지
        if people[b] + people[a] <= limit : #리미트보다 작거나 같으면
            a += 1 #가장 작은 애 태우고
            answer += 1 # 같이 태울 수 있는 경우 하나 추가
        b -= 1 #가장 큰 수는 되든 안되든 무조건 태우고
    return len(people) - answer

people=[70, 50, 80]
limit=100

def solution(people, limit):
    people.sort()
    a=0
    b=len(people)-1
    answer=0
    while a<b:
        if people[a]+people[b]<=limit:
            answer+=1
            a+=1
        b-=1
    return len(people)-answer

print(solution(people, limit))

#Other Answer
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people)) #오름차순 정렬하고
    #deque는 스택과 큐의 기능을 모두 가진 객체
    # 출입구를 양쪽으로 갖고 있어서 다양하게 활용 가능
    # 문자열을 전달하면 각 요소를 갖는 리스트처럼 생긴 deque가 생성된다.

    while deque_people:
        left = deque_people.popleft() #가장 작은거
        if not deque_people: #모든 요소가 다 빠지면, 결과값은 1이다.
            return result + 1
        right = deque_people.pop() #가장 큰거
        if left + right > limit: #가장 큰거와 가장 작은거의 합이 리미트보다 크면
            deque_people.appendleft(left) #작은거는 그냥 둔다
        result += 1 #그리고 결과값에 1을 더한다
    return result
    #무조건 큰거 작은거 빼서 더할건데 한번만 빼면 null이 되면 1명 밖에 없는 것이므로 결과값 1
    # 두개의 합이 리미트보다 크면 결과값에 1을 더하면 작은거는 못 탔으니까 다시 큐에 넣는다
    