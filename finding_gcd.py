def finding_gcd(a, b):
    while(b != 0): #num2가 0이 아닐 동안
        result = b #결과값은 num2
        a, b =b, a % b #num2 = num1%num2
        #num1 = 21, num2 =12일때
        #result = 12, num1=21, num2=21%12=9
        #다음루프 result = 9, num1=21, num2 = 21%9 = 3
        #다음루프 result = 3, num1 =21 , num2 = 21 % 3 = 0, 루프종료
    return result
def gcd():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = finding_gcd(num1,num2)
    print(result)
if __name__ == "__main__":
    gcd()
