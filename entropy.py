import math

p = 1
n = 3

t = p+n

print(f"-{p}/{t}log2({p}/{t}) - {n}/{t}log2({n}/{t}) = {(-1)*(p/t)*math.log2(p/t) - (n/t)*math.log2(n/t)}")
print(f"entropy={(-1)*(p/t)*math.log2(p/t) - (n/t)*math.log2(n/t)}")