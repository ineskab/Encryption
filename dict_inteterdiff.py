def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d_intersect = {}
    d_diff = {}
    
    intersection = d1.keys() & d2.keys()
    
    for k in intersection:
        d_intersect[k] = f(d1[k], d2[k])
    
    diff1 = { k : d2[k] for k in set(d2) - set(d1) }
    diff2 = { k : d1[k] for k in set(d1) - set(d2) }


    d_diff = {**diff1, **diff2}
    
    return(d_intersect, d_diff)