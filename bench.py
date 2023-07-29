#!/usr/bin/env python3

import random

global_variable = 0

for i in range(1000):
    global_variable += 1

for i in range(1000):
    global_variable = global_variable - 1

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fizzbuzz(n):
    if n % 15 == 0:
        return "fizzbuzz"

    if n % 3 == 0:
        return "fizz"

    if n % 5 == 0:
        return "buzz"

    return n

def arithmetic_operations(a, b, c, d):
    foo = (((-a * 123 + b * 123.456 + c * 23) / 31) * a) / (b + 1) + 2.0 * d
    bar = ((foo * a) / (b + 1)) * c + 3 * d
    baz = foo + bar + a + b + c + d
    bam = foo * 2 + bar * 3 + baz * 4
    return bam

def bitwise_operations(a, b, c):
    foo = a << 1
    bar = ((foo | a) & b) ^ c
    baz = bar >> 1
    return baz

def comparison_operations(a, b):
    result = 0

    if a == b:
        result += 1

    if a != b:
        result += 1

    if a < b:
        result += 1

    if a <= b:
        result += 1

    if a > b:
        result += 1

    if a >= b:
        result += 1

    return result

def string_operations(a, b, c):
    vec = []
    sep = "::"

    string = "foo" + sep + a + sep + b + sep + c + sep + "bar"

    for element in string.split(sep):
        vec.append(element)

    return sep.join(vec)

def make_adder_closure(n):
    def adds_n(arg):
        return arg + n
    return adds_n

class ObjectWithoutConstructor:
    pass

class ObjectWithConstructor:
    def __init__(self, value):
        self.value = value

class Object:
    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

def main():
    vec = list()
    map = dict()

    # Basic global variable operations.
    global global_variable
    for i in range(1000):
        global_variable += 1
    for i in range(1000):
        global_variable = global_variable - 1

    # Basic local variable operations.
    local_variable = 0
    for i in range(1000):
        local_variable += 1
    for i in range(1000):
        local_variable = local_variable - 1

    # Basic arithmetic operations.
    for i in range(1000):
        result = (i * 109153 + 257) / 253 - 751 + 4059.123
        vec.append(result)
        map[i] = result

    # Basic string operations.
    basic_string = ""
    for i in range(1000):
        basic_string += str(i)
        vec.append(basic_string)
        map[i] = basic_string

    # Basic string interpolation operations.
    for i in range(10):
        for j in range(10):
            for k in range(10):
                map[f"{i}-{j}-{k}"] = f"foo-{i + j + k}-bar"

    # Basic vector getting and setting.
    for i in range(1000):
        vec[i] = vec[i + 1]

    # Basic map getting and setting.
    for i in range(1000):
        map[i * 2] = map[i]

    # Basic type conversions.
    for i in range(1000):
        vec[i] = int(str(i))

    # Basic iterating over a vector.
    new_vec = []
    for value in vec:
        new_vec.append(value)

    # Basic iterating over a map.
    new_map = {}
    for key, value in map.items():
        new_map[key] = value

    # Basic sorting.
    vec_to_sort = []
    for i in range(1000):
        vec_to_sort.append(i)
    random.shuffle(vec_to_sort)
    vec_to_sort.sort()

    # Recursive function calls.
    for i in range(25):
        vec.append(fibonacci(i))

    # FizzBuzz.
    for i in range(1000):
        vec.append(fizzbuzz(i))

    # Basic object initialization without a constructor.
    for i in range(1000):
        object = ObjectWithoutConstructor()
        object.value = i
        vec.append(object)

    # Basic object initialization with a constructor.
    for i in range(1000):
        object = ObjectWithConstructor(i)
        vec.append(object)

    # Basic field operations.
    object = Object()
    for i in range(1000):
        object.value += 1
    for i in range(1000):
        object.value = object.value - 1

    # Basic method operations.
    for i in range(1000):
        object.set_value(i)
        vec.append(object.get_value())

    # Arithmetic operations.
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result = arithmetic_operations(i, j, k, i + j + k)
                vec.append(result)

    # Bitwise operations.
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result = bitwise_operations(i, j, k)
                vec.append(result)

    # Comparison operations.
    for i in range(33):
        for j in range(33):
            result = comparison_operations(i, j)
            vec.append(result)

    # String operations.
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result = string_operations(str(i), str(j), str(k))
                vec.append(result)

    # Closures.
    for i in range(1000):
        adder = make_adder_closure(i)
        vec.append(adder)
        vec.append(adder(i))

    # String concatenation.
    for i in range(1000):
        s1 = "foo";
        s2 = "bar";
        s3 = "baz";
        result = s1 + str(i) + s2 + str(i) + s3
        map[result] = result;

if __name__ == "__main__":
    main()

