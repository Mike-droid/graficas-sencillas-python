import sys
import re
import time
import collections

print(sys.path)

text = 'Mi número de teléfono es 123 456 789. El código del pais es 52. Mi número de la suerte es el 77'

result = re.findall('\d+', text)
print(result)

# timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

numbers = [1,2,1,2,1,2,2,2,2,2,1,14,45,345,45]
counter = collections.Counter(numbers)
print(counter)