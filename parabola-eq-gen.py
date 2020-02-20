def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return "%d" % (reduced_num)
    elif common_divisor == 1:
        return "%d/%d" % (numer, denom)
    else:
        return "%d/%d" % (reduced_num, reduced_den)

def parabola_vert(vx, vy, px, py):
    a = simplify_fraction((py - vy), ((px - vx)**2))
    vx = -vx

    if vx > 0:
        if vy > 0:
            return 'y = %s(x + %d)² + %d' % (a, vx, vy)
        elif vy < 0:
            return 'y = %s(x + %d)² %d' % (a, vx, vy)
        else:
            return 'y = %s(x + %d)²' % (a, vx)
    if vx < 0:
        if vy > 0:
            return 'y = %s(x %d)² + %d' % (a, vx, vy)
        elif vy < 0:
            return 'y = %s(x %d)² %d' % (a, vx, vy)
        else:
            return 'y = %s(x %d)²' % (a, vx)
    else:
        if vy > 0:
            return 'y = %sx² + %d' % (a, vy)
        elif vy < 0:
            return 'y = %sx² %d' % (a, vy)
        else:
            return 'y = %sx²' % (a)
    
def parabola_hori(vx, vy, px, py):
    a = simplify_fraction((px - vx), ((py - vy)**2))
    vy = -vy

    if vy > 0:
        if vx > 0:
            return 'x = %s(y + %d)² + %d' % (a, vy, vx)
        elif vx < 0:
            return 'x = %s(y + %d)² %d' % (a, vy, vx)
        else:
            return 'x = %s(y + %d)²' % (a, vy)
    if vy < 0:
        if vx > 0:
            return 'x = %s(y %d)² + %d' % (a, vy, vx)
        elif vx < 0:
            return 'x = %s(y %d)² %d' % (a, vy, vx)
        else:
            return 'x = %s(y %d)²' % (a, vy)
    else:
        if vx > 0:
            return 'x = %sy² + %d' % (a, vx)
        elif vx < 0:
            return 'x = %sy² %d' % (a, vx)
        else:
            return 'x = %sy²' % (a)

print('-----PARABOLA EQUATION GENERATOR-----')
while True:
    print('Horizontal or Vertical?')
    direction = input('Type H or V: ')
    while direction not in ('h', 'H', 'v', 'V'):
        print('Invalid Direction')
        direction = input('Type H or V: ')
    vx = int(input('Vertex X: '))
    vy = int(input('Vertex Y: '))
    px = int(input('Point X: '))
    py = int(input('Point Y: '))

    if direction in ('h', 'H'):
        print('\n' + parabola_hori(vx, vy, px, py) + '\n')
    elif direction in ('v', 'V'):
        print('\n' + parabola_vert(vx, vy, px, py) + '\n')
