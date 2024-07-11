# 모듈 사용

import get_area
area = get_area.get_circle_area(10)
print(f'반지름이 10인 원의 넓이: {area}')

area = get_area.get_rect_area(10,20)
print(f'가로 세로가 10, 20인 사각형의 넓이: {area}')

area = get_area.get_trai_area(10, 20)
print(f'가로 세로가 10, 20인 삼각형의 넓이: {area}')