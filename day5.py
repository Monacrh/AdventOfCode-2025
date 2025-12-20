# Part 1
# iRange = []
# Available = []
# sum = 0

# is_parsing_ranges = True

# print("Masukkan data (tekan Enter pada baris kosong untuk beralih, tekan Ctrl+D/Z atau ketik 'DONE' untuk selesai):")

# while True:
#     try:
#         line = input().strip()
        
#         if line.upper() == "DONE":
#             break
            
#         if not line:
#             is_parsing_ranges = False
#             continue
            
#         if is_parsing_ranges:
#             iRange.append(line)
#         else:
#             Available.append(line)
            
#     except EOFError:
#         break

# for i in range(0, len(Available)):
#     fresh = False
#     for j in range(0, len(iRange)):
#         range_parts = iRange[j].split('-')
#         start = int(range_parts[0])
#         end = int(range_parts[1])
#         avail_id = int(Available[i])
        
#         if start <= avail_id <= end:
#             fresh = True
#             sum += 1
#             break
# print(sum)

intervals = []

print("Masukkan data (ketik 'DONE' atau tekan Enter dua kali untuk selesai):")

while True:
    line = input().strip()
    
    if not line or line.upper() == "DONE":
        break
    
    try:
        start, end = map(int, line.split('-'))
        intervals.append([start, end])
    except ValueError:
        continue

intervals.sort()

if not intervals:
    print("Data kosong.")
else:
    merged = []
    curr_start, curr_end = intervals[0]

    for next_start, next_end in intervals[1:]:
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    
    merged.append((curr_start, curr_end))

    total_sum = 0
    for start, end in merged:
        total_sum += (end - start + 1)

    print("\n--- Hasil Perhitungan ---")
    print(f"Total Unique ID: {total_sum}")