#!/usr/bin/env python
import random,string
def activation_code(count,length):
    base=string.ascii_letters+string.digits
    return [''.join(random.sample(base,length)) for i in range(count)]

print(activation_code(200,20))

