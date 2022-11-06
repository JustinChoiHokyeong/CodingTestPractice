#join은 리스트의 문자열을 하나의 문자열로 합쳐준다.
#split은 하나의 문자열을 문자열의 리스트로 분리해준다.
str='hi my name is Justin'
str2='hi, my, name, is, Justin'
a=str.split()
d=str2.split(', ')
print(a) #['hi', 'my', 'name', 'is', 'Justin']
print(d) #['hi', 'my', 'name', 'is', 'Justin']
#요소별로 구분해줄 문자열을 전달해주면 된다.

b="".join(a)
print(b) #himynameisJustin
c=" ".join(a)
print(c) #hi my name is Justin
#요소들을 연결해줄 문자열을 전달하고 조인을 쓰면 된다.
