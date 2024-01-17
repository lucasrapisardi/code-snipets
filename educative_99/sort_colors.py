# Declare 3 ponteiros: vermelho e branco no indice 0. Azul no último índice
# Se colors[white] for 0 troca os valores de color[white] e color[red].
# Incrementa ambos os ponteiros em 1

# Senão, se colors[white] é 1, a posição é correta, nenhuma troca é necessária. Incremente white em 1
# Senão, colors[white] = 2, troca colors[white] e colors[blue] e decrementamos blue em 1

def sort_colors(colors):
  red, white, blue = 0, 0, len(colors) - 1

  while white <= blue:
    if colors[white] == 0:
      if colors[red] != 0:
        colors[red], colors[white] = colors[white], colors[red]

      white += 1
      red += 1
      
    elif colors[white] == 1:
      white += 1
    
    else:
      if colors[blue] != 2:
        colors[blue], colors[white] = colors[white], colors[blue]
      blue -= 1
  return colors

lista1 = [0,1,0]
lista2 = [1]
lista3 = [2, 2]
lista4 = [1, 1, 0, 2]
lista5 = [2, 1, 1, 0, 0]

print(sort_colors(lista1))
print(sort_colors(lista2))
print(sort_colors(lista3))
print(sort_colors(lista4))
print(sort_colors(lista5))
