#N,M,K를 공백으로 구분하여 입력받기
N, M, K =  map(int,input().split())
#N개의 수를 공백으로 구분하ㅕ 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수를 정렬하기
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두번째로 큰 수

#가자 큰 수가 더해지는 횟수 계산
count = int(m / (K + 1)) * K
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second  # 두번째로 큰 수 더하기

print(result)
