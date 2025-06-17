def get_octet(cidr):
    # Determine the octet
    if cidr <= 8:
        octet = '1st'
    elif cidr <= 16:
        octet = '2nd'
    elif cidr <= 24:
        octet = '3rd'
    elif cidr <= 32:
        octet = '4th'
    
    return octet

def get_inc(cidr):
    # Determine the Increment
    _64i = (2,10,18,26)
    _32i = (3,11,19,27)
    _16i = (4,12,20,28)
    _8i = (5,13,21,29)
    _4i = (6,14,22,30)
    _2i = (7,15,23,31)
    _1i = (8,16,24,32)
    
    if cidr in _1i:
        increment = 1
    elif cidr in _2i:
        increment = 2
    elif cidr in _4i:
        increment = 4
    elif cidr in _8i:
        increment = 8
    elif cidr in _16i:
        increment = 16
    elif cidr in _32i:
        increment = 32
    elif cidr in _64i:
        increment = 64
    else:
        increment = 128
    
    return increment

def cidr_to_rivan(cidr):
    octet = get_octet(cidr)
    increment = get_inc(cidr)
        
    return f'({octet}, {str(increment)}i)'