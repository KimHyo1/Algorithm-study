##1.정수형 다루기
a = 1000 #양의 정수
print(a)

a = -7 #음의 정수
print(a)

a = 0 #0
print(a)

##2.실수형 다루기
a = 157.93 #양의 실수
print(a)

a = -1837.2 #음의 실수
print(a)

a = 5. #소수부가 0알때 0 생략
print(a)

a = -.7 #정수부가 0일 때 0 생략
print(a)

##3.지수표현다루기
a = 1e9 #10억
print(a)

a = 75.25e1 # 752.5
print(a)

a = 3954e-3 # 3.954
print(a)

##5.2진수 
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print("True")
else: 
    print("False")

##6.반올림하기
a = 0.3 + 0.6
print(round(a, 4)) 

if round(a, 4) == 0.9:
    print("True")
else:
    print("False")

##7.수 자료형의 연산
a = 7 
b = 3

print(a / b) #나누기

print(a % b) #나머지

print(a // b) #몫

##7. 거듭제곱 연산자
a = 5
b = 3

print ( a ** b) # a의 b승

##7. 리스트
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[4]) #인덱스 4에 해당하는 원소 출력

a = list() #빈 리스트 만들기
print(a)

a = [] #빈 리스트 만들기2
print(a)

n = 10 # 크기가 n이고, 모든 값이 0인 리스트 만들기(리스트 초기화)
a = [0] * n #길이가 n인 리스트 만들기
print(a)

##8. 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1]) #뒤에서 첫번째 원소 출력

print(a[-3]) #뒤에서 세번째 원소 출력

a[3] = 7 #인덱스 3에 해당하는 원소를 7로 변경
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4]) #인덱스 1부터 3까지의 원소 출력

##9. 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1] #0부터 19까지의 수 중에서 홀수만 포함하는 리스트
print(array)

#array = []
#for i in range(20):
#    if i % 2 == 1:
#        array.append(i)
#   print(array)

array = [ i * i for i in range(1, 10)] #1부터 9까지의 수의 제곱값을 포함하는 리스트
print(array)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

##10. 리스트 관련 기타 메서드

a = [1, 3, 4]
print("기본 리스트: ", a)

#리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

#오름차순정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

#특정값인 데이터 개수 세기
print("리스트에 3이 몇 개 있는지 세기: ", a.count(3))

#특정값인 데이터 삭제
a.remove(1)
print("리스트에서 1 제거: ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} #집합 자료형을 이용하여 제거할 원소를 지정
result = [i for i in a if i not in remove_set] #리스트 컴프리헨션을 이용하여 remove_set에 포함되지 않는 원소들로 구성된 새로운 리스트 생성
print(result)