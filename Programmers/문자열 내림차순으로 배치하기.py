'''
소문자 -> 대문자 순으로 
소문자에서는 역 알파벳 순으로
'''
# #대문자 있으면 분리해서 뒤로 보내기
# s='Zbcdefg'
# for i in s:
#     if i.isupper():
#         s=s[s.index(i)+1:]+s[s.index(i)]
#         print(s)

# #소문자 대문자 각각 내림차순으로 정렬
# s=''.join(sorted(s)[::-1])
# print(s)

s='Zbcdefg'
# def solution(s):
#     s=''.join(sorted(s)[::-1])
#     print(s)
#     for i in s:
#         if i.isupper():
#             s=s[s.index(i)+1:]+s[s.index(i)]
#     return s

def solution1(s):
    s=''.join(sorted(s)[::-1])
    return s

print(solution1(s))
'''
join은 앞에 괄호 안에 전달한 '' 구분자로 리스트의 문자열들을 하나의 문자열로 합쳐준다.
list.sort()는 원래의 리스트를 정렬해서 변환하는 것이고
sorted(list)는 원래의 리스트는 그대로 있고, 새로운 리스트를 리턴해주는 것이다.
reverse 조건을 줄 수도 있다.
리스트를 슬라이싱 할 때 -1을 쓰면 뒤에서부터 하는 것이다.

'''