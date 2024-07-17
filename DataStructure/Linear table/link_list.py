def multiply(arr, n):
    carry = 0
    for i in range(len(arr)):
        prod = arr[i] * n + carry
        arr[i] = prod % 10
        carry = prod // 10
    while carry:
        arr.append(carry % 10)
        carry //= 10

def power(r, n):
    if n == 0:
        return [1]
    arr = [int(x) for x in str(r).replace('.', '')]
    point = str(r).index('.')
    for _ in range(n - 1):
        multiply(arr, r)
    point *= n
    while len(arr) <= point:
        arr.append(0)
    arr = arr[:point] + ['.'] + arr[point:]
    while arr[-1] == 0:
        arr.pop()
    if arr[-1] == '.':
        arr.pop()
    return ''.join(map(str, arr))

while True:
    try:
        r, n = input().split()
        r = float(r)
        n = int(n)
        result = power(r, n)
        print(result)
    except:
        break

