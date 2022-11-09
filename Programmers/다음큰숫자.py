# n=78
# print(bin(n))

# print()
# #2진수로 변환했고
# bin(n)[2:]
# #1의 갯수 세기
# str(bin(n)[2:]).count('1')
# print(str(bin(n)[2:]).count('1'))

# #1, 2, 2**2, 2**3, 2**4, ...
# #1의 갯수는 같지만 바로 다음으로 큰수 이기 때문에, 길이는 같을 것이다.

# #2진수 길이
# length=len(str(bin(n)[2:]))
# print(len(str(bin(n)[2:])))
# sum=0
# for i in range(length):
#     sum+=2**i
#     print(sum)

# Other Answer
# def solution(n):
#     c=bin(n).count('1')
#     for i in range(n+1,1000001):
#         if c==bin(i).count('1'):
#             return i
# print(solution(15))


# Other Answer
# def nextBigNumber(n):
#     num1 = bin(n).count('1')
#     #갯수가 같은게 나오면 break로 반복문 탈출하고
#     #그때까지는 n부터 n+=1로 1씩 키우면서 반복 동작한다.
#     while True:
#         n = n + 1
#         if num1 == bin(n).count('1'):
#             break
#     return n


# Other Answer
def nextBigNumber(n, count = 0):
    return n if bin(n).count("1") is count else nextBigNumber(n+1, bin(n).count("1") if count is 0 else count)
# count는 초기값과 함께 전달
# 삼항연산자 return 조건이 참일때 값 if 조건 else 조건이 거짓일때 값
# else 뒤에 재귀함수 형태로 함수 자기자신을 전달하였다.
# n에 1씩 더한 값들을 이진수로 바꿔서 1의 갯수를 확인해서 n과 같은 값을 가진 값이 나오면, 그때의 n을 리턴해준다.

print(nextBigNumber(15))