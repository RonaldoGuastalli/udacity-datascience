tuple_a = 1, 2
tuple_b = (1, 2)
tuple_c = 1, 2, 3, 6, 9, 4, 5
tuple_d = 1, "texto na tupla", 4.6
# tuple_a[1] = 9 #TypeError: 'tuple' object does not support item assignment

print(tuple_a == tuple_b)
print(tuple_a[1])
print(len(tuple_c))
print(max(tuple_c))
print(min(tuple_c))
print(sorted(tuple_c))
print(sum(tuple_a))
print(tuple_d)
# print(sorted(tuple_d)) erro str e int
