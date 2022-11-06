#My Answer

# x="0111010"
# #0을 제거
# a=x.replace('0','')
# print(a)

# #for문을 돌면서 0을 몇개 제거했는지 체크
# zero=0
# for i in x:
#     if i in '0':
#         x = x.replace('0','')
#         zero+=1
# print(x, zero)

# #0을 제거한 뒤에 x의 길이를 다시 2진법 문자열로 전환
# print(len(x))
# b=format(len(x), 'b')
# print(b) #100

# #다시 0을 제거
# for i in b:
#     if i in '0':
#         b = b.replace('0','')
#         zero+=1
# print(b, zero)

# 결과값이 1이 나왔다면, 이진변수 횟수와 제거한 0의 갯수 
# 배열에 담아 리턴

# s1="110010101001"
# count=0
# zero=0
# for i in s1:
#     if i in '0':
#         s1 = s1.replace('0','')
#         zero+=1
# s1=str(format(len(s1), 'b'))
# count+=1
# #여기까지가 이진변호나 1번
# print(s1, count, zero)

def solution(s):
    count=0 #전역변수, 지역변수 잘 구분하기
    zero=0
    while s!="1":
        for i in s:
            if i in '0':
                s = s.replace('0','')
                zero+=1
        s=str(format(len(s), 'b'))
        count+=1
    return [count,zero]

a="1111111"
print(solution(a))

#작은 부분부터 하나씩 확인하면서 풀어야 끝까지 답을 맞춰갈 수 있다.


#Other Answer

def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1') #1의 갯수를 세서
        b += len(s) - num #전체 길이에서 뺴주면, 사라진 0의 갯수가 나오고
        s = bin(num)[2:] #동시에 어차피 1만 남으니까 바로 2진수로 바꾼다
    return [a, b]


