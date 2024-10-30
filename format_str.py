
# % format

team1_num = 5
print("В команде Мастера кода участников: %d !" % 5)
team2_num = 6

print("Итого сегодня в командах участников: %d и %d !" % (5, 6))

# format()

score_1 = 45
score_2 = 40

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Команда Мастера кода решила задач: {} !".format(score_1))

team1_time = 1552.512
team2_time = 1551.0

print("Волшебники данных решили задачи за {} с !".format(team2_time))

# f строка

print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 >= score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 <= score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = "Ничья!"

challenge_result = f"{result}"

print(f"Результат битвы: {challenge_result}")