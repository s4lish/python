import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
# داده‌های مربوط به ماشین‌های سواری (وزن، طول)
carssample = np.array([
    [1000, 4], [1200, 4.2], [1300, 4.5], [1400, 4.3], [1100, 4.1],
    [1250, 4.4], [1350, 4.6], [1450, 4.7]
])

# داده‌های مربوط به ماشین‌های سنگین (وزن، طول)
truckssample = np.array([
    [3000, 6], [3200, 6.5], [3500, 7], [3700, 7.2], [3300, 6.8],
    [3100, 6.3], [3400, 7.1], [3600, 7.5],[3000,5],[3500,4.5],[3700,8]
])

num_samples = 100  # تعداد نمونه‌ها برای هر گروه

# ایجاد داده‌های جدید برای خودروهای سواری
cars_expanded = np.repeat(carssample, num_samples // len(carssample), axis=0)  # تکرار داده‌ها
cars_expanded = cars_expanded + np.random.normal(scale=[100, 0.15], size=cars_expanded.shape)  # افزودن نویز

# ایجاد داده‌های جدید برای کامیون‌ها
trucks_expanded = np.repeat(truckssample, num_samples // len(truckssample), axis=0)  # تکرار داده‌ها
trucks_expanded = trucks_expanded + np.random.normal(scale=[200, 0.2], size=trucks_expanded.shape)  # افزودن نویز

plt.scatter(cars_expanded[:, 1], cars_expanded[:, 0], color='blue', label="سواری‌ها")
plt.scatter(trucks_expanded[:, 1], trucks_expanded[:, 0], color='red', label="کامیون‌ها")

A = 2
L = 0.5
for car in cars_expanded:
    y = car[0] + 300
    x = car[1]
    calc_y = A * x
    E = y - calc_y
    Delta_A = L * (E // x)
    print(f"A : {A}")
    print(f"Error : {E}")
    print(f"Delta_A : {Delta_A}")
    A = A + Delta_A
    print(f"calcY : {calc_y}")
    print(f"new A :{A}")
    print("---------------")

    
for truck in trucks_expanded:
    y = truck[0] - 300
    x = truck[1]
    calc_y = A * x
    E = y - calc_y
    Delta_A = L * (E // x)
    print(f"A : {A}")
    print(f"Error : {E}")
    print(f"Delta_A : {Delta_A}")
    A = A + Delta_A
    print(f"calcY : {calc_y}")
    print(f"new A :{A}")
    print("---------------")


x_values = np.linspace(0, 10, 100)
y_values = A * x_values  # محاسبه y از معادله y = 0.25x
plt.plot(x_values, y_values, 'r--', label="")  # خط سبز خط‌چین

equation = f"y = {A} * x"
plt.text(6, 2500, equation, fontsize=12, color='green', bbox=dict(facecolor='white', alpha=0.5))

"""
print(vhicw)
# تولید مقادیر x در بازه مشخص
x_values = np.linspace(0, 10, 100)
y_values = 2 * x_values  # محاسبه y از معادله y = 0.25x

y_moredbazar = 250 * x_values
# رسم نمودار
plt.plot(x_values, y_values, 'r--', label="")  # خط سبز خط‌چین
plt.plot(x_values, y_moredbazar, 'g--', label="")  # خط سبز خط‌چین


y_new1 = 275 * x_values
plt.plot(x_values, y_new1, 'b--', label="n1")  # خط سبز خط‌چین
y_new2 = 483 * x_values
plt.plot(x_values, y_new2, 'b--', label="n2")  # خط سبز خط‌چین
"""
# نمایش معادله خط روی نمودار
plt.xlabel("length(meter)")
plt.ylabel("weight(kg)")
plt.legend()
plt.title("cars and trucks")

plt.show()