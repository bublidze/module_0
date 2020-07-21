#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
guess_number = np.random.randint(1,101)
print ("Загадано число от 1 до 100.")


def guessing_the_number(guess_number):
    '''Функция принимает загаданное значение рандомного числа, после чего 
    методом бинарного поиска отгадывает его значение и возвращает число 
    попыток.'''
    
    count_attempts = 0
    max_value = 100
    min_value = 0
    average = max_value
    
    if average == guess_number:
        count_attempts += 1
        
    while average != guess_number:
        count_attempts += 1
        average = int(np.average([max_value, min_value]))
        
        if guess_number <= average:
            max_value = average
            
        else:
            min_value = average
            
    return(count_attempts) # Число угадано, выход из цикла. Возврат кол-ва попыток.


def score_game(guessing_the_number):
    '''Запускаем игру 1000 раз, чтобы узнать среднее кол-во угадываний одного числа
    '''
    random_count_list = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, дабы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    
    for random_number in random_array:
        random_count_list.append(guessing_the_number(random_number))
    number_of_attempts = int(np.mean(random_count_list))
    
    print("Ваш алгоритм угадывает число в среднем за {} попыток.".format    (number_of_attempts))
    
    return(number_of_attempts)


function_response = score_game(guessing_the_number)
print(function_response)


# In[ ]:




