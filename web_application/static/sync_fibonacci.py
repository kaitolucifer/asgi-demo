import time
from functools import lru_cache


@lru_cache
def fibn(n):
    if n in (0, 1):
        return n
    return fibn(n - 2) + fibn(n - 1)


start = time.time()
c = fibn(100)
end = time.time()
print(f'{end-start} secs')
