"""For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7"""

def solution(statues):
    count = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            count += 1
    return count

    
print(solution([6, 2, 3, 8]))
print(solution([0, 3]))
print(solution([5, 4, 6]))
print(solution([6, 3]))
print(solution([1]))