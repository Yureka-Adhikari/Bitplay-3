def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swapping using XOR a = {a} and b = {b} ")
    
def swap2(a,b):
    a = (a&b) + (a|b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print(f"After swapping a = {a} and b = {b}")

swap1(5, 10)
swap2(5, 10)    