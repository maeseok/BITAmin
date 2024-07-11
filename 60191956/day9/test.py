def show_circle_area_1():
    r=1
    result = 3.14*r**2
    print(result)
def show_circle_area_10():
    r=10
    result = 3.14*r**2
    print(result)

def show_circle_area(radius):
    result = 3.14*radius**2
    print(result)
def show_circle_area(radius):
    result = 3.14*radius**2
    return result

def get_radius(prompt):
    radius = int(input(prompt))
    return radius
r = get_radius('넓이를 구하고자 하는 원의 반지름은?')
area = show_circle_area(r)
print(f'반지름 {r}인 원의 넓이: 3.14*{r}*{r} = {area}')

def sum_two_integer(num1, num2):
    return num1+num2

def fah_to_cel(fah):
    c=(fah-32)*9/5
    return c

def get_real(prompt):
    data = float(input(prompt))
    return data
def get_vol_cy(r,h):
    result = 3.14*r**2*h
    return result
