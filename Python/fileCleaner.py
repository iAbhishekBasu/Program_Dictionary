import os


def func(base_address='/')->None:
    """
    Cleans the content of all files in the provided directory
    """
    walk = list(os.walk(base_address))
    for x in walk:
        address = x[0]
        files = x[2]
        full_addresses = list(map(lambda i: os.path.join(address, i), files))
        for file in full_addresses:
            with open(file, 'w') as f:
                print('cleaning: {}'.format(file))
        print('-' * 25)
