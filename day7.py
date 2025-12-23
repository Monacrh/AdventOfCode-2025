# import sys

# def count_tachyon_splits():
#     # Membaca seluruh input dari terminal hingga EOF (End Of File)
#     manifold_map = sys.stdin.read()
    
#     if not manifold_map.strip():
#         return

#     # Pemrosesan grid
#     rows = [line for line in manifold_map.strip().split('\n') if line.strip()]
#     height = len(rows)
#     width = len(rows[0])

#     # Cari posisi awal 'S'
#     start_x = rows[0].find('S')
#     if start_x == -1:
#         return
    
#     active_beams = {start_x}
#     total_splits = 0

#     # Simulasi pergerakan beam
#     for y in range(height):
#         next_beams = set()
#         for x in active_beams:
#             # Pastikan x masih dalam batas lebar grid
#             if x < 0 or x >= width:
#                 continue
                
#             if rows[y][x] == '^':
#                 total_splits += 1
#                 # Split ke kiri dan kanan
#                 next_beams.add(x - 1)
#                 next_beams.add(x + 1)
#             else:
#                 # Lanjut lurus ke bawah
#                 next_beams.add(x)
        
#         active_beams = next_beams

#     print(total_splits)

# if __name__ == "__main__":
#     count_tachyon_splits()

import sys
from collections import Counter

def solve_quantum_manifold():
    
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    lines = [line for line in input_data.split('\n') if line.strip()]
    height = len(lines)
    
    start_x = lines[0].find('S')
    
    current_timelines = Counter({start_x: 1})

    for y in range(height):
        while any(lines[y][x] == '^' for x in current_timelines if 0 <= x < len(lines[y])):
            next_gen = Counter()
            for x, count in current_timelines.items():
                if 0 <= x < len(lines[y]) and lines[y][x] == '^':
                    next_gen[x - 1] += count
                    next_gen[x + 1] += count
                else:
                    next_gen[x] += count
            current_timelines = next_gen

    total_timelines = sum(current_timelines.values())
    
    print("-" * 30)
    print(f"Total Timeline Aktif: {total_timelines}")

if __name__ == "__main__":
    solve_quantum_manifold()