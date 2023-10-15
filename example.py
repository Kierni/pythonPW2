def sweap_max(items) -> list:
    example = [];
    element = items[0]
    max_pos = items.index(max(items))
    items[0] , items[max_pos]= items[max_pos], items[0]
    return items
my_list = [ 2,3,4,5,6]
print(sweap_max(my_list))