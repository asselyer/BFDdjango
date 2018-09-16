
from math import sqrt


urlpatterns = (

                       )
ab=input("Введите два числа: ").strip().split(" ")
print("Гипотенуза: {}".format(sqrt(float(ab[0])**2+float(ab[1])**2)))