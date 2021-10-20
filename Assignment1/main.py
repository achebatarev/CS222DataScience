# My Name is Alexandr Chebatarev and this is my program that allows you to have some insights about Stack Overflow users using their data.
from collections import defaultdict
# This function completes task 1 by outputing all countires, and amount of people from each country


def countries():
    d = defaultdict(int)
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                d[line.split('|')[1]] += 1
    sorted_countries = sorted(d.items(), key=lambda map: map[1])
    data_list = [f'{country}: {people}'for country, people in sorted_countries]
    print("\n".join(data_list))

# This function completes task 2 by outputing top 10 most used languages


def top_languages():
    d = defaultdict(int)
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                languages = line.strip().split('|')[-1]
                for language in languages.split(';'):
                    d[language] += 1
    sorted_languages = sorted(d.items(), key=lambda map: map[1], reverse=True)
    data_list = [f'{index+1}) {language[0]}: {language[1]}' for index,
                 language in enumerate(sorted_languages) if index < 10]
    print("\n".join(data_list))

# This function outputs male average salary and female average salary


def average_gender_salary():
    d = defaultdict(int)
    male = 0
    female = 0
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                gender = line.split('|')[6]
                pay = float(line.split('|')[4])
                if gender == "Male":
                    male += 1
                else:
                    female += 1
                d[gender] += pay
    print('Male: {:,.2f}$'.format(d["Male"]/male))
    print('Female: {:,.2f}$'.format(d["Female"]/female))

# This function completes task 4 and outputs  countries maximum and average salary


def country_maximum_average():
    d = defaultdict(list)
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                country = line.split('|')[1]
                pay = float(line.split('|')[4])
                d[country].append(pay)
    country_max_sort = sorted(
        d.items(), key=lambda x: sum(x[1])/len(x[1]))
    print("\n".join(['{country}: Maximum Salary: {maximum:,.2f}$, Average Salary: {average:,.2f}$'.format(
        country=key, average=sum(value)/len(value), maximum=max(value)) for key, value in country_max_sort]))

# This function completes task 5 and outputs the top language among users who exercise 3-4 times per week


def top_language_exercise():
    d = defaultdict(int)
    exercise = '3 - 4 times per week'
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                if line.split('|')[5] == exercise:
                    languages = line.strip().split('|')[-1]
                    for language in languages.split(';'):
                        d[language] += 1
        print(
            f'The most popular langauge among people who exercise {exercise} is {max(d, key=d.get)}')

# Outputs job satisfaction among people who earn 6 figure salary or higher


def satisfaction_salary():
    d = defaultdict(int)
    with open('stackOverflowData.txt') as f:
        for i, line in enumerate(f.readlines()):
            if i != 0:
                salary = float(line.split('|')[4])
                if len(str(int(salary))) >= 6:
                    satisfaction = line.split('|')[2]
                    d[satisfaction] += 1

    data = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print('\n'.join([f'{key}: {value}'for key, value in data]))


# Runs the program
try:
    functions = {1: countries, 2: top_languages, 3: average_gender_salary,
                 4: country_maximum_average, 5: top_language_exercise, 6: satisfaction_salary}

    MAX_AMOUNT = len(functions)
    print("Welcome to the Alexandr Chebatarev's Stack Overflow data analysis program")
    print("We hold answers to the most important question in the universe, just pick one to see\n")
    while True:
        print(
            f'Type a digit between 1 and {MAX_AMOUNT} or type exit to quit the program')
        print('1.', 'How many people responded from each country?')
        print('2.', 'What are the ten most popular programming languages in the survey?')
        print('3.', 'What is the average salary for each gender?')
        print('4.', 'What is the the maximum and average salary for each country?')
        print('5.', 'What is the most popular programming language for people that exercise 3-4 times per week?')
        print(
            '6.', 'What is the job satisfaction among people who earn 6 figures or beyond')
        print('exit')
        n = input()
        if n.isdigit():
            if int(n) in functions:
                functions[int(n)]()
                print('Do you want to continue? Type y/n')
                continuation = input()
                if continuation == 'y':
                    pass
                elif continuation == 'n':
                    break
                else:
                    print('Please type y/n')
            else:
                print(f'Digits are supposed to be between 1 and {MAX_AMOUNT}')
        elif n == 'exit':
            break
        else:
            print("Enter a digit or type exit to quit the program")
    print('Thank you for using this program, come back for more')
except KeyboardInterrupt:
    print('\nSo that is how you decided to end this')
