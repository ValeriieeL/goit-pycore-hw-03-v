import random
def get_number_ticket():
    min_num=1
    max_num=55
    quantity=6
    return sorted(random.sample(range(min_num, max_num +1), quantity ))
print(get_number_ticket())

#Two ways of this example

import random
def get_number_ticket( min_num=1, max_num=100, quantity=5):
    return sorted(random.sample(range(min_num, max_num +1), quantity ))
print(get_number_ticket())
print(get_number_ticket())





