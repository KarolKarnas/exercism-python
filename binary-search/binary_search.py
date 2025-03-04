def find(search_list, value):   
    if not search_list:
        raise ValueError("value not in array")
    
    middle = len(search_list) // 2
    
    if search_list[middle] == value:
        return middle
    
    if search_list[middle] > value:
        return find(search_list[:middle], value)
    
    if search_list[middle] < value:
        result = find(search_list[middle + 1:], value)
        return middle + 1 + result