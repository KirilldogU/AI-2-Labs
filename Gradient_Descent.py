import math


def equation1(x, y):
    return 4 * (x * x) - 3 * x * y + 2 * (y * y) + 24 * x - 20 * y


def equation1_xDer(x, y):
    return 8 * x - 3 * y + 24


def equation1_yDer(x, y):
    return 4 * (y - 5) - 3 * x


def equation2(x, y):
    return ((1 - y) ** 2) + 100 * ((x - (y ** 2)) ** 2)


def equation2_xDer(x, y):
    return 200 * (x - (y ** 2))


def equation2_yDer(x, y):
    return 2 * (-200 * x * y + 200 * (y ** 3) + y - 1)


error = .0000000001
lambo = 0.1


def gradient_descent1():
    x, y = 0, 0
    xDer = equation1_xDer(x, y)
    yDer = equation1_yDer(x, y)
    while (xDer > error) or (xDer < (-1 * error)) or (yDer > error) or (yDer < (-1 * error)):
        x -= xDer * lambo
        y -= yDer * lambo
        xDer = equation1_xDer(x, y)
        yDer = equation1_yDer(x, y)
    return (x, y)


# print("EQUATION 1 MINIMUM: " + str(gradient_descent1()))

def gradient_descent2():
    x, y = 0, 0
    xDer = equation2_xDer(x, y)
    yDer = equation2_yDer(x, y)
    while (xDer > error) or (xDer < (-1 * error)) or (yDer > error) or (yDer < (-1 * error)):
        x -= xDer * lambo
        y -= yDer * lambo
        xDer = equation2_xDer(x, y)
        yDer = equation2_yDer(x, y)
    return (x, y)


# print("EQUATION 2 MINIMUM: " + str(gradient_descent2()))

def one_d_minimize(f, left, right, tolerance):
    if right - left < tolerance:
        return (right + left) / 2
    x_13 = left + (right - left) / 3
    x_23 = left + 2 * (right - left) / 3
    f_13 = f(x_13)
    f_23 = f(x_23)
    if f_23 < f_13:
        return one_d_minimize(f, x_13, right, tolerance)
    if f_23 > f_13:
        return one_d_minimize(f, left, x_23, tolerance)
    return one_d_minimize(f, x_13, x_23, tolerance)


def make_func(f, location, direction):
    def func(lambo):
        return f([location[0] - lambo * direction[0], location[1] - lambo * direction[1]])

    return func


def func1(vector):
    x = vector[0]
    y = vector[1]
    return (4 * x * x) - 3 * x * y + 2 * y * y + 24 * x - 20 * y


def func2(vector):
    x = vector[0]
    y = vector[1]
    return ((1 - y) ** 2) + 100 * ((x - (y * y)) ** 2)


def deriv_func1(vector):
    x = vector[0]
    y = vector[1]
    x_deriv = 8 * x - 3 * y + 24
    y_deriv = 4 * (y - 5) - 3 * x
    return (x_deriv, y_deriv)


def deriv_func2(vector):
    x = vector[0]
    y = vector[1]
    x_deriv = 200 * (x - y ** 2)
    y_deriv = 2 * (-200 * x * y + 200 * (y ** 3) + y - 1)
    return (x_deriv, y_deriv)


def sin_func(x):
    return math.sin(x) + math.sin(3 * x) + math.sin(4 * x)


def magnitude(vectors):
    xVector = vectors[0]
    yVector = vectors[1]
    return ((xVector ** 2) + (yVector ** 2)) ** (.5)


def grad_desc_with_line_search(start, f, deriv_f, tolerance):
    location = start  # location is array [x, y]
    while magnitude(deriv_f(location)) > tolerance:
        direction = deriv_f(location)
        closed_f = make_func(f, location, direction)
        lambo = one_d_minimize(closed_f, 0, 1, 10 ** (-8))
        location[0] = location[0] - lambo * direction[0]
        location[1] = location[1] - lambo * direction[1]
    return location


# part 1
print(one_d_minimize(sin_func, -1, 0, 10 ** -8))

# part 2
start = [0, 0]
print(grad_desc_with_line_search(start, func1, deriv_func1, 10 ** -8))
print(grad_desc_with_line_search(start, func2, deriv_func2, 10 ** -8))