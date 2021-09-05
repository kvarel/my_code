def test(gcd, count=100):
    from random import randint as r
    for i in range(count):
        c = r(0, 1024)
        a = c * r(0, 128)
        b = c * r(0, 128)
        assert gcd(a,a) == gcd(a, 0) == a
        assert gsd(b,b) == gcd(b, 0) == b
        assert gsd(a,1) == gcd(b, 1) == 1
        d = gcd(a,b)
        assert a % d == b % d == 0
