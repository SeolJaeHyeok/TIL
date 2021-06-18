# 1000번 A + B
a, b = map(int, input().split())
print(a+b)

# 1001번 A - B
c, d = map(int, input().split())
print(c-d)

# 1002번 A * B
e, f = map(int, input().split())
print(e*f)

# 1003번 A / B
h, i = map(int, input().split())
print(h/i)

# 10869번
j, k = map(int, input().split())
print(j+k)
print(j-k)
print(j*k)
print(j//k)
print(j%k)

# 10430번
A, B, C = map(int, input().split())
print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 2588번
num1 = int(input(''))
num2 = int(input(''))
print(num1 * (num2 % 10))
print(num1 * (num2 % 100 // 10))
print(num1 * (num2 // 100))
print(num1 * num2)