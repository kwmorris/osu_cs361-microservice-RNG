import time

from rand import rand

def test_1k():
    start_time = time.perf_counter()
    rand(1000)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time}")

if __name__ == "__main__":
    test_1k()