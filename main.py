## 함수
def add_func(n1, n2):
    result = n1 + n2
    return result


def sub_func(n1, n2):
    resrult = n1 - n2
    return n1 - n2

def mul_func(n1, n2):
    result = n1 * n2
    return result




## 전역변수
num1, num2, res = 100, 200, 0



## 메인 코드
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, 'x', num2, '=', res)

