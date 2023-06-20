value = str(input('Введите Вашу строку: '))
to_right = str(value)
to_left_list = []
to_left = ''

for elem in value:
    to_left_list.append(elem)
to_left_list.reverse()

for elem in to_left_list:
    to_left = to_left + elem

if to_left == to_right:
    print(True)
else:
    print(False)

# Я не понял, где тут находится коммит (подскажите, пожалуйста), так что решение опишу тут
# Моё решение заключается в создании листа, состоящего из элементов строки, который потом переворачивается и переводится во вторую строку, и она сверяется с первый. Если это палиндром, то строки будут равны.
