def exponent_mod(base, exp, mod):
    # expase modases 
    if base == 0:
        return 0
    if exp == 0:
        return 1

    # If exp is Even 
    y = 0
    if exp % 2 == 0:
        y = exponent_mod(base, exp / 2, mod)
        y = (y * y) % mod

        # If exp is Odd 
    else:
        y = base % mod
        y = (y * exponent_mod(base, exp - 1,
                             mod) % mod) % mod
    return (y + mod) % mod

if __name__ == '__main__':
    Base,Exp,Mod=151,4565,54
    ans=exponent_mod(Base,Exp,Mod)
    print(ans)