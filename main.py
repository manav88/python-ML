# class Car:
#     wheel = 4
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#
#     def get_car_info(self):
#         print(self.name,self.type,self.wheel)
#
# c1 = Car('BMW','SUV')
# c2 = Car('Audi','sedan')
#
# c1.get_car_info()
# c2.get_car_info()

# class Man:
#     def __init__(self, name,job):
#         self.name = name
#         self.job = job
#
#     def maninfo(self):
#          print(self.name)
#
# class nam(Man):
#             def __init__(self,name):
#                 self.name=name
#
#
# m1 = Man('maanv', 'md')
# m2=nam('rajesh')
# m1.maninfo()
# m2.maninfo()

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
x =np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)
mymodel = list(map(myfunc, x))
print(speed)

plt.scatter(10, myfunc(10))
plt.plot(x, mymodel)
plt.show()