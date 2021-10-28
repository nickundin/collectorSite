import concurrent.futures

num = 0


def adding(number):
    return number + 1

with concurrent.futures.ProcessPoolExecutor() as executor:
    d = executor.submit(adding, 5)
    print(d.result())

