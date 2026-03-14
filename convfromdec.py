def convfromdec(num, base):
    mult, result = 1,0 #가중치1, 결과0으로 초기화
    while num > 0:
        result += num % base * mult #입력받은 수를 진수로 나눈 나머지를 가중치에 곱함
        #9%2 = 1, 1*1수행하고 더함
        #4%2 =0, 0*10수행
        #2%2 = 0 0 *100수행
        #1%2 = 1 1*1000 수행
        mult *= 10 #가중치에 10곱하고 앞자리수로 이동
        num = num//base #정수 나눗셈, 9//2 = 4, num=4 > 0이기때문에 다시 처음으로 이동
        #4//2=2, num=2>0이기 때문에 처음으로 이동
        #2//2=1, num=1>0이기 때문에 처음으로 이동
        #1//2 = 0, num=0이기때문에 루프종료
    return result
def test():
    num = int(input("Enter num: "))
    base = int(input("Enter base: "))
    result = convfromdec(num, base)
    print("conv: ",result)
if __name__ == "__main__":
    test()