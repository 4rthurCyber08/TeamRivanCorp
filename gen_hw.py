import random
import socket
import struct
import rivanformat

class GenerateItems:
    def __init__(self, total_items, item_type):
      self.total = total_items
      self.type = item_type
      
      self.gen_item()
      
    def gen_item():
        # CIDR
        random_cidr = random.randint(1,32)
        cidr_value = f'/{str(random_cidr)}'
        
        print(cidr_value)
        
        # NETMASK
        net_bits = 32 - random_cidr
        netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << net_bits)))

        print(netmask)


        # RIVANFORMAT
        rivan = rivanformat.cidr_to_rivan(random_cidr)

        print(rivan)
                
        # BINARY FORMAT
        per_octet = netmask.split('.')
        bin_value = []
        
        for decimal in per_octet:
            bin_form = format(int(decimal), f'0{8}b')
            bin_value.append(bin_form)
            
        to_bits = f'{bin_value[0]} . {bin_value[1]} . {bin_value[2]} . {bin_value[3]}'
        
        print(to_bits)
        
        bin_value = []
        
        # WILDCARD
        for decimal in per_octet:
            difference = 255 - int(decimal)
            bin_value.append(difference)
    



def total_items():
    total = None
    
    while True:
        total = input('How many items for the exercise? ')
        try:
            int(total)
            break
        except ValueError:
            print('Invalid Input. Enter a number. ')
    
    return total

def item_types():
    cidr_type = 1
    netmask_type = 2
    rivan_type = 3
    wildmask_type = 4
    mixed_type = 5
    
    while True:
        item_type = input('''
What will be the given value for the exercise? 
    CIDR = 1
    Subnet Mask = 2
    Rivan Format = 3
    Wildcard = 4
    Mixed Values = 5

> ''')
        try:
            int(item_type)
            break
        except ValueError:
            print('Invalid Input. Enter a number. ')
        
    return item_type

if __name__ == '__main__':    
    GenerateItems(total_items(), item_types())