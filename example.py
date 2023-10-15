def sweap_max(items) -> list:
    example = [];
    element = items[0]
    max_pos = 0
    d = 123
    for x in range(len(items)):
        if element <= items[x]:
            element = items[x]
            max_pos = x;
            y = items[0]
            items[0] = items[max_pos]
            items[max_pos] = y
    return items
my_list = [ 2,3,4,5,6]
print(sweap_max(my_list))