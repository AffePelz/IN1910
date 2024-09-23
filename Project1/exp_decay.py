import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
    def __init__(self, a):
        self.a = a

    def __call__(self, t, u):
        return -self.a*u

    def solve(self, u0, T, dt):
        fun = self.__call__
        t_span = (0, T)
        y0 = (u0,)

        steps = int(T/dt)
        eval = np.linspace(0, T, steps+1)

        a = scipy.integrate.solve_ivp(fun, t_span, y0, t_eval=eval)
        return a.t, a.y[0]


if __name__ == "__main__":
    decay_model = ExponentialDecay(0.4)
    t, u = decay_model.solve(1, 10, 0.1)

    decay_model2 = ExponentialDecay(1)
    t2, u2 = decay_model2.solve(10, 10, 0.1)

    plt.plot(t, u)
    plt.plot(t2, u2)
    plt.title("Exponential Decay")
    plt.xlabel("Time [t]")
    plt.ylabel("Function u(t)")
    plt.show()
