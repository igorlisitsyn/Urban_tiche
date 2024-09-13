

def get_matrix(n, m, value):
    a = []
    b = []
    for j in range(m):
        b.append(value)
    for i in range(n):
        a.append(b)
    return a

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

