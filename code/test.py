import requests
import time

URL = 'http://127.0.0.1:5000'

# test for 1000 random numbers between [0, 1)
def test_1k():
    start_time = time.perf_counter()
    params = {
        "count": 1000
    }
    r = requests.get(URL + '/', params=params)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Test: 1000 numbers between [0, 1)")
    print(r.text)
    print(f"Status code: {r.status_code}")
    print(f"Elapsed time: {elapsed_time}\n")

# test for 20 random integers between [0, 10)
def test_even():
    params = {
        "count": 20,
        "range": "0, 10",
        "bin_count": 10
    }
    r = requests.get(URL + '/', params=params)
    print("Test: 20 integers between (0, 10]")
    print(r.text)
    print(f"Status code: {r.status_code}\n")

# test for 20 random integers between [10, 20)
def test_even_2():
    params = {
        "count": 20,
        "range": "10, 20",
        "bin_type": 'int'
    }
    r = requests.get(URL + '/', params=params)
    print("Test: 20 integers between (10, 20]")
    print(r.text)
    print(f"Status code: {r.status_code}")

if __name__ == "__main__":
    test_1k()
    test_even()
    test_even_2()