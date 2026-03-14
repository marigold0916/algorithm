def convfromdec_lager(num, base):
    strings = "0123456789ABCDEFGHIJ" #10진수이상에서 사용하는 문자
    result = ""#결과 초기화
    while num >0:
        digit = num % base #strings에서 몇번째 문자를 뽑을지 결정
        result = strings[digit] + result #예:num=31,base=16일때 digit=15->F ,digit = 1 ->1
        #이전 result가 stings[digit]뒤에 있어서 출력은 계산의 역순으로 나타남
        num = num // base #31 // 16= 1
    return result
def test():
    num = int(input("Enter num: "))
    base = int(input("Enter base: "))
    result = convfromdec_lager(num,base)
    print(result)
if __name__ =="__main__":
    test()