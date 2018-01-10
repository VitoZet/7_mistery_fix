from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    try:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    except ValueError:
        return None, None

    if discriminant == 0:
        return root1, None

    else:
        return root1, root2
