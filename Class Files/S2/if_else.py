weight = float(input('please enter your weight: '))
height = float(input('please enter your height: '))
bmi = weight / (height ** 2)
print(f'Your bmi is {bmi}')

if 18.5 <= bmi < 25:
    print('normal')
elif bmi >= 25 and bmi < 30:
    print('overweight')
elif 30 <= bmi < 35:
    print('obesity 1')
elif 35 <= bmi < 40:
    print('obesity 2')
elif bmi >= 40:
    print('obesity 3')
else:
    print('underweight')


