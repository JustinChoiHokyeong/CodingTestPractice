'''
가장 먼저 탈락하는 사람은 몇 번째 사람이며,
자신의 몇 번째 차례에서 탈락하는가

마지막에 끝나는 문자로 시작해야 하고, 똑같은 단어를 두번 쓸 수 없다
'''


# #끝과 시작 문자 비교
# for i in range(len(words)-1):
#     if words[i][-1]==words[i+1][0]:
#         print(words[i])

# #리스트 안에 특정한 값이 중복되는지 확인
# for i in words:
#     if words.count(i)>1:
#         print(i)

# def solution(n, words):
#     for i in range(len(words)):
#         if words[i-1][-1]!=words[i][0] or words[i] in words[:i]:
#             #n으로 몇 번째 사람 차례인지 표현하기
#             #print(n) if i%n==0 else print((i+2)%n)
#             return [(i%n)+1 , (i//n)+1]
#         else:
#             return [0,0]        

# solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
#     #return [몇 번째 사람이며,자신의 몇 번째 차례에서 탈락]



#Other Answer
# def solution(n, words):
#     for i in range(1, len(words)):#1~8
#         if words[i][0] != words[i-1][-1] or words[i] in words[:i] : 
#             # in 으로 그 전까지의 애들 중에서(자기 자신 미포함) 포함 여부 확인
#             # 두 조건을 동시에 확인하고 그 i와 n 값으로 몇 번째인지 확인해야 하므로
#             # 
#             return [(i%n)+1, (i//n)+1]
#     return [0,0] # 위 조건에 해당되는 것이 없다면 그냥 [0,0] 리턴
# i=len(words)
# print(i) 
# for i in range(1, len(words)): #len은 7 , range는 1,2,3,4,5,6
#     #"hello", "one", "even", "never", "now", "world" 이 중에서 "hello" 이게 포함되어 있냐는 거니까
#     print(words[i] in words[:i])
# print(words[:i])

# print(solution(n, words))

# # Other Answer
# def solution(n, words):
#     answer = []
#     turn = 0
#     wordList = [words[0]]
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     for idx in range(1, len(words)):
#         if words[idx-1][-1] != words[idx][0]:
#             turn = idx
#             break
#         if words[idx] in wordList:
#             turn = idx
#             break
#         wordList.append(words[idx])
#     answer = [turn%n +1, turn//n + 1]
#     if turn == 0:
#         answer = [0, 0]
#     return answer
import math
n=2
words=["hello", "one", "even", "never", "now", "world", "hello"]

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else: #for ~ else -> break 없이 for이 끝나서 탈출되었을 때 실행된다.
        return [0,0]

for p in range(1, len(words)):
    print((p%n)+1, math.ceil(p//n))

print()
print(solution(n, words))