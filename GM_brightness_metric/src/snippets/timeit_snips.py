import timeit

count_runtime_from_here = """
first = [x**2 for x in range(1,10,1)]
#print(f'{first}')
"""

elapsed_time = timeit.timeit(count_runtime_from_here, number=1000)/1000
print(elapsed_time)