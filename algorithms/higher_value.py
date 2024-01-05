def higher_value(list):
    if len(list) == 0:
        return 0
    else:
        maior = list[0]
        if list[1:] > maior:
            maior = higher_value(list)
    return maior

lista = [5, 3, 9]
print(higher_value(lista))