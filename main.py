import time
import math
import matplotlib.pyplot as plt
from Matrix import Matrix


def residual_err(matrix, r, b):
    if not isinstance(matrix, Matrix) or not isinstance(b, list) or not isinstance(b, list):
        return "wrong parameters"
    # res(k) = M * r(k) − b
    res = matrix * r
    for i in range(len(res)):
        res[i] -= b[i]
    return res


def norm_2(vector):
    if not isinstance(vector, list):
        return "wrong parameters"
    norm = 0
    for i in range(len(vector)):
        norm += pow(vector[i], 2)
    return math.sqrt(norm)


def Jacobi(matrix, b, max_residual_err, max_iteration):
    if not isinstance(matrix, Matrix) or not isinstance(b, list):
        return "wrong parameters"
    h = matrix.get_heigth()
    x = [1] * h
    x_prev = [1] * h
    res_norm = norm_2(residual_err(matrix, b, x))
    res = [res_norm]
    iteration = 0

    start = time.time()
    while res_norm > max_residual_err:
        if iteration > max_iteration:
            end = time.time()
            return iteration, end - start, "seem to be math.inf", res
        for i in range(h):
            sum = 0
            for j in range(h):
                if i != j:
                    sum += matrix.matarr[i, j] * x_prev[j]

            x[i] = (b[i] - sum) / matrix.matarr[i, i]

        x_prev = x.copy()
        iteration = iteration + 1
        res_norm = norm_2(residual_err(matrix, x, b))
        res.append(res_norm)

    end = time.time()
    return iteration, end - start, res_norm, res


def Gauss_Seidl(matrix, b, max_residual_err, max_iteration):
    if not isinstance(matrix, Matrix) or not isinstance(b, list):
        return "wrong parameters"
    h = matrix.get_heigth()
    x = [1] * h
    x_prev = [1] * h
    res_norm = norm_2(residual_err(matrix, b, x))
    res = [res_norm]
    iteration = 0

    start = time.time()
    while res_norm > max_residual_err:
        if iteration > max_iteration:
            end = time.time()
            return iteration, end - start, "seem to be math.inf", res
        for i in range(h):
            sum = 0
            for j in range(i):
                sum += matrix.matarr[i, j] * x[j]
            for j in range(i+1, h):
                sum += matrix.matarr[i, j] * x_prev[j]

            x[i] = (b[i] - sum) / matrix.matarr[i, i]

        x_prev = x.copy()
        iteration = iteration + 1
        res_norm = norm_2(residual_err(matrix, x, b))
        res.append(res_norm)

    end = time.time()
    return iteration, end - start, res_norm, res


def LU_factorisation(matrix, b, with_speed_up=True):
    if not isinstance(matrix, Matrix) or not isinstance(b, list):
        return "wrong parameters"
    if matrix.get_width() != matrix.get_heigth():
        return "wrong matrix shape - width is not equal to height"
    m = matrix.get_heigth()
    U = Matrix(matrix.matarr.copy())
    L = Matrix.identity_matrix(m)

    start = time.time()
    for k in range(m-1):
        for j in range(k+1, m):
            L.matarr[j, k] = U.matarr[j, k] / U.matarr[k, k]
            if L.matarr[j, k] == 0 and with_speed_up:
                continue
            for i in range(k, m):
                U.matarr[j, i] = U.matarr[j, i] - L.matarr[j, k] * U.matarr[k, i]

    # Rozwiązujemy układ równań: Ly = b za pomocą podstawiania wprzód(O(n2))
    # Rozwiązujemy układ równań: Ux = y za pomocą podstawiania wstecz(O(n2))
    y = Matrix.forward_sub(L, b)
    x = Matrix.back_sub(U, y)

    end = time.time()
    return end - start, norm_2(residual_err(matrix, x, b))


def print_results_including_res_err(method, iteration, delta_time, res_err):
    print("metoda ", method)
    print("     liczba iteracji: ", iteration)
    print("     czas [s]: ", delta_time)
    print("     wartość błędu rezydualnego: ", res_err)


def print_results(method, delta_time, res_err):
    print("metoda ", method)
    print("     czas [s]: ", delta_time)
    print("     wartość błędu rezydualnego: ", res_err)


def residual_err_plot(method_0, method_1, res_arr, save_name):
    plt.title("Wykres wartości błędu rezydualnego dla kolejnych iteracji dla metody " + method_0)
    plt.xlabel("numer iteracji")
    plt.ylabel("wartość błędu rezydualnego")

    plt.plot(res_arr, label=method_1)
    plt.legend()
    plt.grid()
    plt.show()
    plt.savefig(save_name)

# ---- Zadanie A ----
N = 963
a1 = 13
a2 = -1
a3 = -1
A = Matrix.same_values_on_diagonal(N, N, [a3, a2, a1, a2, a3], -2)
b = [math.sin(i * 9) for i in range(N)]

print("---- Zadanie B ----")
[iteration, delta_time, res_err, res_arr] = Jacobi(A, b, pow(10, -9), pow(10, 2))
print_results_including_res_err("Jacobiego", iteration, delta_time, res_err)
residual_err_plot("Jacobiego", "Jacobi", res_arr, "J_res_err_b.png")
[iteration, delta_time, res_err, res_arr] = Gauss_Seidl(A, b, pow(10, -9), pow(10, 2))
print_results_including_res_err("Gauss-Seidla ", iteration, delta_time, res_err)
residual_err_plot("Gauss-Seidla", "Gauss-Seidl", res_arr, "GS_res_err_b.png")


print("---- Zadanie C ----")
a1 = 3
A = Matrix.same_values_on_diagonal(N, N, [a3, a2, a1, a2, a3], -2)
[iteration, delta_time, res_err, res_arr] = Jacobi(A, b, pow(10, -9), pow(10, 2))
print_results_including_res_err("Jacobiego", iteration, delta_time, res_err)
residual_err_plot("Jacobiego", "Jacobi", res_arr, "J_res_err_c.png")
[iteration, delta_time, res_err, res_arr] = Gauss_Seidl(A, b, pow(10, -9), pow(10, 2))
print_results_including_res_err("Gaussa-Seidla ", iteration, delta_time, res_err)
residual_err_plot("Gauss-Seidla", "Gauss-Seidl", res_arr, "GS_res_err_c.png")

print("---- Zadanie D ----")
[delta_time, res_err] = LU_factorisation(A, b)
print_results("Faktoryzacji LU", delta_time, res_err)

print("---- Zadanie E ----")
unknowns = [100, 500, 1000, 2000, 3000, 4000, 5000]
a1 = 13
a2 = -1
a3 = -1
times_Jacobi = [0] * len(unknowns)
times_Gauss_Seidl = [0] * len(unknowns)
times_LU_factorisation = [0] * len(unknowns)
max = 0
for u in unknowns:
    if max < u:
        max = u
b = [math.sin(i * 9) for i in range(max)]
for i in range(len(unknowns)):
    N = unknowns[i]
    A = Matrix.same_values_on_diagonal(N, N, [a3, a2, a1, a2, a3], -2)
    [iter_Jacobi, t_Jacobi, res_Jacobi] = Jacobi(A, b[:N], pow(10, -9), pow(10, 2))
    [iter_Gauss_Seidl, t_Gauss_Seidl, res_Gauss_Seidl] = Gauss_Seidl(A, b[:N], pow(10, -9), pow(10, 2))
    # jeżeli obliczenia mają być wykonane bez optymalizacji, to należy dodać jako ostatni argument wartość False
    [t_LU_factorisation, res_LU_factorisation] = LU_factorisation(A, b[:N])

    times_Jacobi[i] = t_Jacobi
    times_Gauss_Seidl[i] = t_Gauss_Seidl
    times_LU_factorisation[i] = t_LU_factorisation

plt.title("Wykres zależności czasu trwania poszczególnych algorytmów od liczby niewiadomych N")
plt.xlabel("Liczba niewiadomych N")
plt.ylabel("czas trwania [s]")

plt.plot(unknowns, times_Jacobi, label='Jacobi')
plt.plot(unknowns, times_Gauss_Seidl, label='Gauss-Seidl')
plt.plot(unknowns, times_LU_factorisation, label='Faktoryzacja LU')

plt.legend()
plt.grid()
plt.savefig("zadanie_e.png")