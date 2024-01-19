# INICIALIZAR 2 PONTEIROS

# LENTO = INPUT

# RAPIDO = SOMA DOS QUADRADOS DOS DIGITOS

# SE RAPIDO != 1 E != LENTO, INCREMENTA 1 E 2

def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum

# def sum_of_squared_digits(number):
#     total_sum = 0
#     while number > 0:
#         number, digit = divmod(number, 10)
#         total_sum += digit ** 2
#     return total_sum

def is_happy_number(n):
    slow = n
    fast = sum_of_squared_digits(n)

    while fast != 1 and fast != slow:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
    
    if fast == 1:
        return True
    return False    

print(is_happy_number(8))
