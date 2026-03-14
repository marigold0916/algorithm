import math as m
def fibonacci_seq_iter(n):#반복문사용, 시간복잡도O(n)
    if n <2: return n
    a, b = 0, 1
    for i in range(n):
        a , b = b, a + b
    return a
def fibonacci_seq_rec(n):#재귀함수, 시간복잡도O(2^n)
    if n < 2: return n
    return fibonacci_seq_rec(n - 1) + fibonacci_seq_rec(n-2)
def fibonacci_seq_form(n):#수식사용, 시간복잡도O(1), 70이상에서 정확도 하락
    sq5 = m.sqrt(5)
    phi = (1+sq5)/2
    return int(m.floor(phi**n / sq5))
def find_fib():
    n = int(input("Enter n: "))
    #rec = fibonacci_seq_rec(n)
    #iter = fibonacci_seq_iter(n)
    form = fibonacci_seq_form(n)
    #print("rec = ",rec)
    #print("iter = ", iter)
    print("form = ", form)
if __name__ == "__main__":
    find_fib()