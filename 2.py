import random
def get_number_ticket():
    min_num=1
    max_num=55
    quantity=6
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= max_num):
        return []
    return sorted(random.sample(range(min_num, max_num +1), quantity ))
print(get_number_ticket())






