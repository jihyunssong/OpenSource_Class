def findMax(a, b, c):
    if a>b:
        big=a
    else:
        big=b

    if c>biggest:
        big=c

    return big

a = int(input("첫 번째 숫자 입력: "))
b = int(input("두 번째 숫자 입력: "))
c = int(input("세 번째 숫자 입력: "))

biggest = findMax(a,b,c)

print(a,b,c,"중 가장 큰 수는", biggest,"입니다.")
