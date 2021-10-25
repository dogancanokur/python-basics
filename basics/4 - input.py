age = input("Enter your age.")

print("Your age: ", age)

name = input("Enter your name")
surname = input("Enter your surname")

print(name + " " + surname)

# inputta aldığımız her değer string olarak görünür. int e çevirmemiz gerekir
a = input("give number")
b = input("give more number")
print(a + b)  # a=1 b=2 => 12
print(int(a) + int(b))  # 3

# type conversion
print(float("3.15"))
