#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = []
    list(tuple_a)
    list(tuple_b)
    for i in range(0, 2):
        tuple_add[i] = tuple_a[i] + tuple_b[i]
        tuple(tuple_add)
    return (tuple_add)

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

