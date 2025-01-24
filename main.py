import numpy as np
import matplotlib.pyplot as plt

x_0 = 1 # 初期位置
epsilon = 0.05 # ステップ幅
t_max = 20 # シミュレーション期間

def hamiltonian(x, p):
    return (x**2 + p**2) / 2

t = np.arange(0, t_max, epsilon)
N = len(t)

# a:解析解、e:オイラー法、s:シンプレクティック数値積分法
# 初期化処理
x_a = x_0*np.cos(t)
p_a = -x_0*np.sin(t)
x_e = np.zeros(N)
p_e = np.zeros(N)
x_s = np.zeros(N)
p_s = np.zeros(N)

# 初期値設定
x_e[0] = x_0
x_s[0] = x_0

# エネルギー初期化処理
E_a = hamiltonian(x_a, p_a)
E_e = np.full(N, hamiltonian(x_e[0], p_e[0]))
E_s = np.full(N, hamiltonian(x_s[0], p_s[0]))

for n in range(N-1):
    # オイラー法
    x_e[n+1] = x_e[n] + epsilon*p_e[n]
    p_e[n+1] = -epsilon*x_e[n] + p_e[n]
    E_e[n+1] = hamiltonian(x_e[n+1], p_e[n+1])

    # シンプレクティック数値積分法
    x_s[n+1] = x_s[n] + epsilon*p_s[n]
    p_s[n+1] = -epsilon*x_s[n+1] + p_s[n]
    E_s[n+1] = hamiltonian(x_s[n+1], p_s[n+1])

analytical_color = [1,0.3,0.3]
euler_color = [0,0,1]
symplectic_color = [0,1,0]

# 位置xシミュレーション結果
plt.subplots(figsize=(10, 4))
plt.xlabel('time (sec)')
plt.ylabel('x')
plt.plot(t, x_a, color=analytical_color, linewidth=6, label='analytical')
plt.plot(t, x_e, color=euler_color, linewidth=3,linestyle="dashed", label='euler')
plt.plot(t, x_s, color=symplectic_color, linewidth=3, linestyle="dashed" ,label='symplectic')
plt.legend()
plt.grid()

# 運動量pシミュレーション結果
plt.subplots(figsize=(10, 4))
plt.xlabel('time (sec)')
plt.ylabel('p')
plt.plot(t, p_a, color=analytical_color, linewidth=6, label='analytical')
plt.plot(t, p_e, color=euler_color, linewidth=3,linestyle="dashed", label='euler')
plt.plot(t, p_s, color=symplectic_color, linewidth=3, linestyle="dashed" ,label='symplectic')
plt.legend()
plt.grid()

# エネルギー評価
ymax = np.ceil(np.amax(E_e))
plt.subplots(figsize=(8, 5))
plt.xlabel('time (sec)')
plt.ylabel(r'Energy $\frac{1}{2}(x^{2} + p^{2})$')
plt.plot(t, E_a, color=analytical_color, linewidth=6, label='analytical')
plt.plot(t, E_e, color=euler_color, linewidth=3,linestyle="dashed", label='euler')
plt.plot(t, E_s, color=symplectic_color, linewidth=3, linestyle="dashed" ,label='symplectic')
plt.ylim(0, ymax)
plt.legend()
plt.grid()

# 相空間
plt.subplots(figsize=(5, 5))
plt.plot(x_a, p_a, color=analytical_color, linewidth=6, label='analytical')
plt.plot(x_e, p_e, color=euler_color, linewidth=3,linestyle="dashed", label='euler')
plt.plot(x_s, p_s, color=symplectic_color, linewidth=3, linestyle="dashed" ,label='symplectic')
plt.xlabel('x')
plt.ylabel('p')
plt.xlim(-1.6, 1.6)
plt.ylim(-1.6, 1.6)
plt.legend()
plt.grid()

plt.show()