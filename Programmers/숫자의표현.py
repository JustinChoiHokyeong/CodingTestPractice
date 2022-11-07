# n=15
# count=0
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(sum)
#     if sum==n:
#         break
'''
1
3
6
10
15
'''    

# 시작하는 숫자도 1씩 키워주기 위해서 for으로 감싸줌
n=15
count=0
for j in range(1,n+1):
    sum=0
    for i in range(j,n+1):
        sum+=i
        if sum==n:
            count+=1
            print(sum, count)
            break
'''
15 1
15 2
15 3
15 4
'''

#함수로 만들어서 확인 -> 효율성에서 탈락
def solution(n):
    count=0
    for j in range(1,n+1):
        sum=0
        for i in range(j,n+1):
            sum+=i
            if sum==n:
                count+=1
                break
            elif sum>n:
                break
            #굳이 계산할 필요없는 부분은 날려버리도록 해야 효율성이 높아짐
    return count

print(solution(15))




