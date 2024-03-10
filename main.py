height = float(input('Enter your height in m : '))
weigth = float(input('Enter the weigth in kg : '))

bmi = round(weigth / height ** 2, 2)

if bmi < 18.5:
    print(f'Your bmi is {bmi}, You are underweight')
elif bmi < 25:
    print(f'Your bmi is {bmi}, You have normal weight')
elif bmi < 30:
    print(f'Your bmi is {bmi}, You are overweight')
elif bmi < 35:
    print(f'Your bmi is {bmi}, You are obese')
else:
    print(f'Your bmi is {bmi}, You are clinically obese')



