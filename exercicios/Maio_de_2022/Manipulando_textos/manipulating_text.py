import time

students = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('students.txt', 'w') as the_text_exercise:
        for key, value in students.items():
            the_text_exercise.write(f'{key}: {value}\n')

time.sleep(0.1)

with open('students.txt', 'r') as the_text_exercise:
        for linha in the_text_exercise:
            print(linha)