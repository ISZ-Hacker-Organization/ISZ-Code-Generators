import secrets
from multiprocessing import Pool, Lock
# By Cracko298
characters = "ABCDEF1234567890"
file_name = "Generated_IDs.txt"
batch_size = 100000

def generate_random_lines(batch_size):
    lines = [''.join(secrets.choice(characters) for _ in range(16)) for _ in range(batch_size)]
    return lines

def write_lines_to_file(lines, lock):
    with lock:
        with open(file_name, "a") as file:
            file.write('\n'.join(lines) + '\n')

if __name__ == "__main__":
    num_processes = 4

    pool = Pool(processes=num_processes)
    lock = Lock()

    num_lines = 2147483647
    num_batches = num_lines // batch_size

    for _ in range(num_batches):
        results = pool.map(generate_random_lines, [batch_size] * num_processes)

        lines_to_write = ['\n'.join(batch) for batch in zip(*results)]
        write_lines_to_file(lines_to_write, lock)

    pool.close()
    pool.join()
