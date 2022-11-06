#파이썬에서는 for in, 한가지 방식의 for문만을 제공한다
#for item in iterable:
    #반복할 구문
#iterable는 반복가능한 객체들을 의미한다. 
# 여기에는 리스트, 딕셔너리, 세트, 스트링, 튜플, 바이츠가 있다.
#객체의 요소들을 돌면서, 아이템을 가지고 함수를 동작시킨다.

#range(start, end, step)
#다른 객체 형태로 변환해줘야 결과값이 리턴된다.
print(list(range(5))) #[0, 1, 2, 3, 4]
for i in range(5):
    print(i)
#객체의 길이와 인덱스를 이용해서 for을 도는 것보다
#객체 자체와 아이템을 이용해서 for문을 도는 것을 파이썬에서 권장한다

#enumerate(obj)
#객체의 인덱스 번호와 원소값을 튜플 형태로 리턴해준다.
#몇 번째 반복문인지 확인할 때 유용하다.
a=[3,5,6,7,9,30]
for i in enumerate(a):
    print(i)
'''
(0, 3)
(1, 5)
(2, 6)
(3, 7)
(4, 9)
(5, 30)
'''