def powerMod(a: int, b: list, mod: int = 1337) -> int:
    def modPow(x, y, mod):
        res = 1
        x %= mod
        
        for _ in range(y):
            res = (res * x) % mod
        return res

    result = 1
    for digit in b:
        result = (modPow(result, 10, mod) * modPow(a, digit, mod)) % mod
    
    return result