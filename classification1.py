import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
# داده‌های مربوط به ماشین‌های سواری (وزن، طول)
cars = np.array([
    [1000, 4], [1200, 4.2], [1300, 4.5], [1400, 4.3], [1100, 4.1],
    [1250, 4.4], [1350, 4.6], [1450, 4.7]
])

# داده‌های مربوط به ماشین‌های سنگین (وزن، طول)
trucks = np.array([
    [3000, 6], [3200, 6.5], [3500, 7], [3700, 7.2], [3300, 6.8],
    [3100, 6.3], [3400, 7.1], [3600, 7.5]
])

# ترکیب داده‌ها و ایجاد برچسب‌ها (0: سواری، 1: کامیون)
X = np.vstack((cars, trucks))  # داده‌های (وزن، طول)
y = np.hstack((np.zeros(len(cars)), np.ones(len(trucks))))  # برچسب‌ها

# ایجاد و آموزش مدل SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X, y)

# رسم داده‌ها
plt.scatter(cars[:, 1], cars[:, 0], color='blue', label="سواری‌ها")
plt.scatter(trucks[:, 1], trucks[:, 0], color='red', label="کامیون‌ها")

# رسم خط جداکننده SVM
w = svm_model.coef_[0]
b = svm_model.intercept_[0]

x_values = np.linspace(0, 10, 100)
y_values = (-w[1] / w[0]) * x_values - (b / w[0])  # معادله خط جداکننده

plt.plot(x_values, y_values, 'g--', label="مرز تصمیم‌گیری SVM")


# تولید مقادیر x در بازه مشخص
x_values = np.linspace(0, 10, 100)
y_values = 400 * x_values  # محاسبه y از معادله y = 0.25x

# رسم نمودار
plt.plot(x_values, y_values, 'r--', label="")  # خط سبز خط‌چین

# نمایش معادله خط روی نمودار
equation = f"y = {(-w[1] / w[0]):.2f} * x + {(-b / w[0]):.2f}"
plt.text(6, 2500, equation, fontsize=12, color='green', bbox=dict(facecolor='white', alpha=0.5))
plt.xlabel("length(meter)")
plt.ylabel("weight(kg)")
plt.legend()
plt.title("cars and trucks")

plt.show()