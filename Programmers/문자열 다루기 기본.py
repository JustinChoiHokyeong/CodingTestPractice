s="2334"
def solution(s):

    s.split()
    for i in range(len(s)):
        if s[i].isdigit()==False:
            return False
    else:
        return True

print(solution(s))

# 놓친 조건이 있다. 
'''
    if len(s)!=4 or len(s)!=6: 
        return False
'''

#My Answer
def solution(s):
    while len(s)==4 or len(s)==6:
        s.split()
        for i in range(len(s)):
            if s[i].isdigit()==False:
                return False
        else: return True
    return False

s="2334"

#Other Answer
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
    # 2가지 조건은 말 그대로 True, False를 리턴하기 때문에
    # and를 써서 동시에 True일때만 True이고 
    # 조건이 충족이 하나라도 안되면 나머지는 다 False를 리턴한다

# print(s.isdigit())
# print(len(s) in (4, 6))

#Other Answer
def alpha_string46(s):
    try:
        int(s) #숫자가 아닌 값이 들어오면 에러가 뜨니까
    except:
        return False # 자동으로 False가 되고
    return len(s) == 4 or len(s) == 6 #숫자가 들어왔으면 
        #길이만 체크해서 True False로 출력시킨다 
'''
예외처리 : 예외가 발생했을 때도 스크립트 실행을 중단하지 않고
게속 실행하게 한다.
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드 
'''

def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
    # 정규식을 이용해서 숫자이고 길이가 4와 6인 것만 확인해서 boolean으로 출력

def alpha_string46(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)
    # 숫자이면서, 길이 체크해서 and와 or만 써서 boolean 리턴