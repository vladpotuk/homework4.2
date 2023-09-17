a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
operation = input("Введіть  'sum' або 'dob':")

if operation == 'sum':
    result = a+b+c
    print("Cума чисел дорівнює:", result)
elif operation == 'dob':
    result = a * b * c
    print("Добуток чисел дорівнює:", result)



