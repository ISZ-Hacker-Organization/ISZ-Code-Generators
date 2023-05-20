from multiprocessing import Pool

ranges = [(0, 16, "0000000{}"), (15, 256, "000000{}"), (255, 4096, "00000{}"), 
          (4095, 65536, "0000{}"), (65535, 1048576, "000{}"), (1048575, 16777216, "00{}"), 
          (16777215, 268435456, "0{}"), (268435455, 4294967296, "{}")]

def process_chunk(chunk): # Spagetti Code Go Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    with open('cheats.txt', 'a') as f:
        for i in chunk:
            for start, end, format_str in ranges:
                if start <= i < end:
                    hp_txt = f"[Weather Freeze to {i}]"
                    hp_addr = "00483624"
                    hp_val = format_str.format(hex(i)[2:])
                    f.write(f"{hp_txt}\n{hp_addr} {hp_val}\n\n")
                    break

if __name__ == '__main__':
    chunk_size = 10000000
    num_processes = 4
    chunks = [range(i, i+chunk_size) for i in range(0, 4294967297, chunk_size)]
    with Pool(num_processes) as p:
        p.map(process_chunk, chunks) # Logic Map for Multiprocessing