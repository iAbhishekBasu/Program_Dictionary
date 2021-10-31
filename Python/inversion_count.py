def inversion_count(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = inversion_count(a)
        b, bi = inversion_count(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

if __name__ == '__main__':
    arr=[50,1,2,30,4,5,6,7,8,90,10]
    inversions=inversion_count(arr)[1]
    print('Number of inversions = {}'.format(inversions))