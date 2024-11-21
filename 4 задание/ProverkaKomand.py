import re
def execution_command(command, array):
    if not isinstance(array, list):
        return "Аргумент не является массивом"
    
    index = re.match("Получить элемент по (\d+) индексу", command)
    if index:
        n = int(index.group(1))
        if 0 <= n < len(array):
            return array[n]
        else:
            return "Индекс выходит за пределы массива."
    
    
    interval = re.match("Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    if interval:
        n, b, v = map(int, interval.groups())
        if n < 0 or b > len(array) or v <= 0:
            return "Неправильное значение шага или интервала"
        return array[n:b:v]
    
    
    from_the_end = re.match("Получить (\d+)-й элемент с конца массива", command)
    if from_the_end:
        n = int(from_the_end.group(1))
        if 1 <= n <= len(array):
            return array[-n]
        else:
            return "Индекс выходит за пределы массива"
    
    return "Неверная команда"


arr = [6, 1, 90, 22, 39, 12, 3]
print(execution_command("Получить элемент по 5 индексу", arr))
print(execution_command("Получить элементы с 1 по 6 с шагом 2", arr))  
print(execution_command("Получить 4-й элемент с конца массива", arr))  
print(execution_command("Получить 1-ый четный элемент массива", arr))  
