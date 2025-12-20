#Part 1
# rows = []
# sum = 0

# while True:
#     line = input().strip()
#     if line.upper() == "END":
#         break
#     if line:
#         rows.append(line.split())

# operators = rows[-1]       
# data_numbers = rows[:-1]    

# for col_idx in range(len(operators)):
#     op = operators[col_idx]
    
#     current_col_values = []
    
#     if op == "*":
#         hasil = 1
#     else:
#         hasil = 0

#     for row_data in data_numbers:
#         val = int(row_data[col_idx])
#         current_col_values.append(str(val))
        
#         if op == "*":
#             hasil *= val
#         else:
#             hasil += val
#     sum += hasil

#     print(sum)

#Part 2
rows = []
result = 0

while True:
    line = input()
    if line.upper() == "END":
        break
    rows.append(line)

max_len = max(len(line) for line in rows)
grid = [line.ljust(max_len) for line in rows]

digit_rows = grid[:-1]
operator_row = grid[-1]

current_block_numbers = []
current_operator = None

for col in range(max_len - 1, -1, -1):
    
    col_content = "".join(digit_rows[row][col] for row in range(len(digit_rows))).replace(" ", "")
    op = operator_row[col].strip()
    if op:
        current_operator = op
    if col_content:
        current_block_numbers.append(int(col_content))
    
    is_empty_column = not col_content and not op
    is_start_of_grid = (col == 0)

    if (is_empty_column or is_start_of_grid) and current_block_numbers:
        if current_operator == "*":
            res = 1
            for n in current_block_numbers: res *= n
        else:
            res = sum(current_block_numbers)
        
        formula = f" {current_operator} ".join(map(str, current_block_numbers))
        print(f"{formula} = {res}")
        
        current_block_numbers = []
        current_operator = None
    
        result += res

print(result)