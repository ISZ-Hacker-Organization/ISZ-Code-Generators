import random
from multiprocessing import Pool, Lock

characters = "ABCDEF1234567890"
file_name = "Generated_IDs.txt"
batch_size = 100000

def generate_random_lines(batch_size):
    lines = []
    for _ in range(batch_size):
        line = ''.join(random.choice(characters) for _ in range(16))
        lines.append(line)
    return lines

def write_lines_to_file(lines, lock):
    with lock:
        with open(file_name, "a") as file:
            for line in lines:
                file.write(line + "\n")

if __name__ == "__main__":
    num_processes = 4

    pool = Pool(processes=num_processes)
    lock = Lock()

    num_lines = 2147483647
    num_batches = num_lines // batch_size

    for _ in range(num_batches):
        results = pool.map(generate_random_lines, [batch_size] * num_processes)

        for lines in zip(*results):
            write_lines_to_file(lines, lock)

    pool.close()
    pool.join()
