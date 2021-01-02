import time

from tld import get_tld, get_fld
# from tld.utils_cy import get_tld as get_tld_cy, get_fld as get_fld_cy


number = 10

start = time.time()
get_tld('https://www.ai.google.com')
end = time.time()

py_time = end - start
print("Python time = {}".format(py_time))

start = time.time()
get_tld('https://www.ai.google.com')
end = time.time()

cy_time = end - start
print("Cython time = {}".format(cy_time))

print("Speedup = {}".format(py_time / cy_time))
