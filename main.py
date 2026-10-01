import time
import matplotlib.pyplot as plt

# 1. СИМУЛЯЦИЯ В КОНСОЛИ
mass = 10.0
step = 1.0

masses_list = []
old_physics_list = []
my_model_list = []

print("=== СИМУЛЯЦИЯ ИСПАРЕНИЯ ЧЕРНОЙ ДЫРЫ ===")
print("Масса | Старая физика (1/M) | Твоя модель (Минус-фильтр)")
print("-" * 55)

while mass >= 0:
    masses_list.append(mass)

    if mass > 0:
        old_val = round(1 / mass, 2)
        old_physics_list.append(old_val)
    else:
        old_val = "ВЗРЫВ (1/0!)"
        old_physics_list.append(5.0)

    if mass > 0:
        my_val = round((1 / mass) - (1 / (mass + mass**2)), 2)
        my_model_list.append(my_val)
    else:
        my_val = 1.00
        my_model_list.append(1.00)

    print(f"{mass:<6} | {str(old_val):<19} | {my_val}")
    mass -= step
    time.sleep(0.2)

print("-" * 55)
print("Испарение завершено! Показываем график...")

# 2. ПОСТРОЕНИЕ И ПОКАЗ ГРАФИКА
plt.figure(figsize=(8, 5))
plt.plot(masses_list, old_physics_list, label="Старая физика (Деление на ноль)", color="red", linestyle="--", marker="x")
plt.plot(masses_list, my_model_list, label="Твоя модель (Квантовый кристалл)", color="green", linewidth=2, marker="o")

plt.xlabel("Масса черной дыры (M)")
plt.ylabel("Температура / Энергия")
plt.title("Сравнение испарения черной дыры")
plt.gca().invert_xaxis()
plt.legend()
plt.grid(True)

# Сохраняем картинку в ту же папку
plt.savefig("black_hole_plot.png")

# Открываем окно с графиком
plt.show()

# Задержка, чтобы чёрное окно консоли не закрывалось сразу
input("\nНажми Enter, чтобы завершить работу...")
