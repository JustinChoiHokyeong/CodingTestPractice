
# 같은 알파벳 2개 붙어있는 짝 찾기
# for i in range(len(s)):
#     if s[i]==s[i+1]:
#         s=s[:i]+s[i+2:]
#         break
# print(s)


#위 동작을 반복하기
# def solution(s):
#     for i in range(len(s)-1): #길이 6, 인덱스 4,5까지만 비교하면 됨
#         if s[i]==s[i+1]:
#             s=s[:i]+s[i+2:]
#             print(s)

    
    # if len(s)==0:
    #     return 1
    # else:
    #     return 0


# for i in range(len(s)-3):
#     if s[i]==s[i+1]:
#         s=s[:i]+s[i+2:]
#         print(s)#bbaa
        # for i in range(len(s)):
        #     if s[i]==s[i+1]:
        #         s=s[:i]+s[i+2:]
        #         print(s)#aa
# len()은 바뀌지 않았기 때문에 string index out of range 에러가 나는 것인가?
s='baabaa'
'''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        s=s[:i]+s[i+2:]
        print(s) 
        break
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        s=s[:i]+s[i+2:]
        print(s)
        break
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        s=s[:i]+s[i+2:]
        print(len(s))
        break
'''
'''
bbaa
aa
0
'''
# s='baabaa'
# def solution(s):
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             s=s[:i]+s[i+2:]
#             if len(s)==0:
#                 print(s)
#                 return 1
#             else:
#                 solution(s)

# print(solution(s))

# Other Answer
# def solution(s): 
#     stack = [] # 비어 있는 스택을 사용하여
#     for i in s: #문자열을 돌면서
#         if len(stack) == 0: stack.append(i) #비어 있으면 넣고
#         elif stack[-1] == i: stack.pop()# 새로 넣는 애가 이미 넣은 애랑 같으면 제거 
#         else: stack.append(i) # 안같으면 그냥 넣음
#     if len(stack) == 0: return 1 # 했을 때 짝이 지어려는 애들은 다 제거 되었으니까
#     else: return 0 # 결론이 나온다.

s='cdcd'
def solution(s):
    stack=[]
    for i in s: #여기서는 i가 인덱스가 아니라 그냥 해당 문자열임
        if len(stack)==0:
            stack.append(i)
        elif stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        return 1
    else:
        return 0

print(solution(s))
