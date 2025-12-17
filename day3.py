# Part 1
# commands = []
# sum = 0

# while True:
#     line = input()
#     if line == "END":
#         break
#     if line.strip():
#         commands.append(line.strip())

#     numbers = list(map(int, commands[-1]))
#     max = -1
#     for i in range(0, len(numbers)-1):
#         for j in range(i+1, len(numbers)):
#             cur = int(f"{numbers[i]}{numbers[j]}")
#             if cur > max:
#                 max = cur
#     sum += max
    
# print(sum)


# Part 2
commands = []
sum = 0

while True:
    line = input()
    if line == "END":
        break
    if line.strip():
        commands.append(line.strip())

    numbers = list(map(int, commands[-1]))
    i = 0
    while len(numbers) > 12 and i < len(numbers) - 1:
        if numbers[i] < numbers[i+1]:
            numbers.pop(i)
            i = 0         
        else:
            i += 1
    sum += int("".join(map(str, numbers[:12])))
    
print(sum)
