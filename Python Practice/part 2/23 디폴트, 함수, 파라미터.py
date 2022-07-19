# 23 디폴트, 함수, 파라미터
#부가세 계산기

def calc_tax( price, operator = 1.1):
    supply_value = round(price / operator)
    vat = price - supply_value
    return supply_value, vat

result = calc_tax(110000)
print(result)
#(100000, 10000)
'''
operator - 디폴트 파라미터
 -> 디폴트 파라미터 자리에 함수 호출시 파라미터값을 전달해주면 그 값으로 변경
round() - 반올림 함수
'''

