height = float(input("Введите ваш рост: "))
weight = float(input("Введите ваш вес: "))

bmi = round(weight/(height ** 2)*10000)

print("Ваш индекс массы тела:",bmi)

bmi_place = int((bmi-20)/(50-20)*30)

string = "20" + "=" * 30 + "50"

string = string[:bmi_place+2] + "|" + string[bmi_place+3:]
print(string)
