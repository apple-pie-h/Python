def replace_item(lst, old_item, new_item):
    for i in range(len(lst)):
        if lst[i]==old_item:
            lst[i]=new_item
    return lst
