"""Игра угадай число"""

import numpy as np

number = np.random.randint(1,101) #загадываем число

#количество попыток

count = 0

while True:
    count += 1
    predict_number = int(input("Enter your number in range from 1 - 100 "))
    
    if predict_number > number:
        print("Choose less number")
    elif predict_number < number:
        print("Choose bigger number")
    else:
        print(f"Correct, you found number {number} by {count} tries!!")
        break