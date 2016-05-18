
class KarastubaMethod(object):
    """ Recursive multiplication using Karatsuba method
    x = 10^n/2 * a + b
    y = 10^n/2 * c + d
    x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
    where (ad+bc) = (a+b)(c+d) - ac - bd
    """

    def multiplying(self, first_number, second_number):

        str_x, str_y = str(first_number), str(second_number)
        n = max(len(str_x), len(str_y))
        if n <= 1:
            return first_number*second_number
        if n % 2 == 0:
            n_2 = int(n/2)
        else:
            n_2 = int(n//2 + 1)
        x, y = str_x.rjust(n, '0'), str_y.rjust(n, '0')
        a, b = int(x[:n_2] or 0), int(x[n_2:] or 0)
        c, d = int(y[:n_2] or 0), int(y[n_2:] or 0)
        ac = self.multiplying(a, c)
        bd = self.multiplying(b, d)
        ab_cd = self.multiplying((a+b), (c+d))
        x_y = pow(10, n)*ac + pow(10, n//2)*(ab_cd - ac - bd) + bd

        print(x_y)
        return x_y

