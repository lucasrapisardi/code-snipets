"""
    For sequence = [1, 3, 2, 1], the output should be
    solution(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    solution(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

# Verificar se existe uma sequencia, se sim retorna a propria lista

# Se existir um elemento quebrando a sequencia, remova-o
    # Existe sequencia?
        # True
    # False

def bad_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return i
    return - 1

def solution(sequence):
    j = bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing

sequence = [1, 3, 2, 1]
j = bad_pair(sequence)
print(sequence[j-1:j])