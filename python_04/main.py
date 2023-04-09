a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

print("Нет нулевых значений!!!" * (a != 0 and b != 0 and c != 0))
print(next((str(num) for num in [a, b, c] if num != 0), "Введены все нули!"))
print(a - b - c if a > b + c else b + c - a)

if a > 50 and (b > a or c > a):
    print("Вася")

if a > 5 or b == 7 or c == 7:
    print("Петя")
