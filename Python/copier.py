import os, shutil


def copier(toAddress='/', fromAddress='/') -> None:
    skipped = copied = 0
    base_address = toAddress
    temp_base_address = fromAddress

    walk = list(os.walk(base_address))
    sub_dirs = walk[0][1]
    for sub_dir in sub_dirs:
        flag = 1
        orig_dir = list(os.walk(os.path.join(walk[0][0], sub_dir)))
        for file_address in orig_dir[0][2]:
            orig_file_address = os.path.join(orig_dir[0][0], file_address)
            temp_file_address = os.path.join(temp_base_address, file_address)

            if os.path.getsize(orig_file_address) < 10:
                if flag:
                    flag = 0
                    print('Skipped ', orig_file_address)
                skipped += 1
                continue

            shutil.copy2(orig_file_address, temp_file_address)
            copied += 1
            print('Transfer {}/{}'.format(sub_dir, file_address), end='--->')
            with open(orig_file_address, 'w') as f:
                print('Cleaned')
        print('-' * 25)
    print('Skipped:{}\nCopied:{}'.format(skipped, copied))
    return


if __name__ == '__main__':
    copier()
