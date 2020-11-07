def wrap(string, max_width):
    store =[]
    for i in range(0,len(string),max_width):
        a = string[i:i+max_width]
        store.append(a)
        # logic
    return '\n'.join(store) 