# PART 1
# input_line = input("Masukkan range ID: ").strip()

# # Parse ranges
# ranges = []
# for part in input_line.split(","):
#     start, end = map(int, part.split("-"))
#     ranges.append((start, end))


# def is_invalid_id(n: int) -> bool:
#     s = str(n)
#     if len(s) % 2 != 0:
#         return False
#     half = len(s) // 2
#     return s[:half] == s[half:]


# invalid_ids = []

# for start, end in ranges:
#     for i in range(start, end + 1):
#         if is_invalid_id(i):
#             invalid_ids.append(i)

# print("\nInvalid IDs:")
# print(invalid_ids)

# print("\nTotal sum:")
# print(sum(invalid_ids))

# PART 2
input_line = input("Masukkan range ID: ").strip()

ranges = []
for part in input_line.split(","):
    start, end = map(int, part.split("-"))
    ranges.append((start, end))


def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    for k in range(1, length // 2 + 1):
        if length % k == 0:
            if s[:k] * (length // k) == s:
                return True
    return False


invalid_ids = []

for start, end in ranges:
    for i in range(start, end + 1):
        if is_invalid_id(i):
            invalid_ids.append(i)

print("\nInvalid IDs:")
print(invalid_ids)

print("\nTotal sum:")
print(sum(invalid_ids))
