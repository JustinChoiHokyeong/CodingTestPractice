a=lambda x,y : x+y
print(a(1,2))

#map(fn, seq)
#파이썬 3에서는 맵으로 나온 결과값을 리스트로 묶어줘야 새로운 리스트가 리턴된다.
b=list(map(lambda x:x**2, range(4)))
print(b) #[0, 1, 4, 9]

#reduce(fn, seq)
#각 원소를 하나씩(짝지어서) 함수를 작동시키고 시퀀스에 누적시켜서 마지막 결과값을 출력해준다.
from functools import reduce
c=reduce(lambda x,y:x+y, range(5))
d=reduce(lambda x,y:y+x, 'abcde') #문자열 순서를 거꾸로 만들어줌
print(c)
print(d)

#filter(fn, seq)
#각 원소를 함수에 적용하는데, 결과값이 참인 원소만 뽑아서 새로운 리스트로 리턴시켜준다.
#파이썬 3에서는 맵으로 나온 결과값을 리스트로 묶어줘야 새로운 리스트가 리턴된다.
f=list(filter(lambda x: x<5, range(10)))
g=list(filter(lambda x: x%2==0, range(10)))
print(f)
print(g)