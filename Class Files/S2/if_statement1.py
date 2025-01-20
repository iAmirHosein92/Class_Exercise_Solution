weight = 84
height = 1.83
bmi = weight / (height ** 2)
normal_bmi = 24
normal_weight = normal_bmi * (height ** 2)


if bmi >= 25:
    print('overweight')
    print('Your overwight value is = ',
          weight - normal_weight,
          'and your bmi is',bmi)
    print(f'Your overwight value is {round(weight - normal_weight,2)} and your bmi is {bmi}')
    
print('done')

print(f'overwight value {round(weight - normal_weight,2)} bmi is {bmi}')
print('overwight value {0} bmi is {1}'.format(round(weight - normal_weight,2),bmi))
