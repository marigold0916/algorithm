def conv2any(num, base):
    strings = "0123456789ABCDEF"
    if num < base:
        return strings[num]
    else:
        return conv2any(num // base, base) \
        + strings[num%base]
    #num=9, base=2일때 conv2any(4,2) + string[9%2=1]-> 1반환
    #num=4이기 때문에 conv2any[2,2] + string[4%2=0] ->0반환
    #num=2이기 때문에 conv2any[1,2] + string[2%2=0] ->0반환
    #num=1이기 때문에 conv2any[0,2] + string[1%2=1] ->1반환
def test():
    num = int(input("Enter num: "))
    base = int(input("Enter base: "))
    result = conv2any(num, base)
    print(result)
if __name__ =="__main__":
    test()