import scipy.integrate
import numpy as np

import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self, M=1, L=1, g=9.81):
        self.M = M  # mass [kg]
        self.L = L  # length [m]
        self.g = g  # gravity [m/s**2]

    def __call__(self, t, y):
        # y = (theta, omega)
        theta = y[0]
        omega = y[1]
        # returns y' = (theta', omega')
        return (omega, -self.g/self.L*np.sin(theta))

    def solve(self, y0, T, dt, angles="rad"):

        # option to convert
        # from radians to degrees
        if angles == "deg":
            y0[0] = 180/np.pi * y0[0]
            y0[1] = 180/np.pi * y0[1]

        # function = (theta', omega')
        fun = self.__call__
        # time interval from 0 to T
        t_span = (0, T)

        steps = int(T/dt)
        eval = np.linspace(0, T, steps)

        # y0 = (theta_start, omega_start)
        # eval specifies when to save values
        # a returns an instance of a class
        a = scipy.integrate.solve_ivp(fun, t_span, y0, t_eval=eval)

        self.t_array = a.t
        # a.y = (theta_array, omega_array)
        self.theta_array = a.y[0]
        self.omega_array = a.y[1]

    # properties returns the stored arrays
    # from solve, returns error if solve
    # method has not been called
    @property
    def t(self):
        try:
            return self.t_array
        except AttributeError:
            print("Solve must be called first")
            raise

    @property
    def theta(self):
        try:
            return self.theta_array
        except AttributeError:
            print("Solve must be called first")
            raise

    @property
    def omega(self):
        try:
            return self.omega_array
        except AttributeError:
            print("Solve must be called first")
            raise

    @property
    def x(self):
        x_value = self.L*np.sin(self.theta_array)
        return x_value

    @property
    def y(self):
        y_value = -self.L*np.cos(self.theta_array)
        return y_value

    @property
    def potential(self):
        return self.M*self.g*(self.y + self.L)

    @property
    def vx(self):
        return np.gradient(self.x, self.t_array)

    @property
    def vy(self):
        return np.gradient(self.y, self.t_array)

    @property
    def kinetic(self):
        return 1/2*self.M*(self.vx**2+self.vy**2)


class DamperedPendulum(Pendulum):
    def __init__(self, B, M=1, L=1, g=9.81):
        Pendulum.__init__(self, M, L, g)
        self.B = B

    def __call__(self, t, y):
        dtheta = Pendulum.__call__(self, t, y)[0]
        domega = Pendulum.__call__(self, t, y)[1]
        return (dtheta, domega - (self.B/self.M)*dtheta)


if __name__ == "__main__":
    u = Pendulum()
    u.solve((np.pi/2, 0), 10, 0.1)

    # theta
    plt.plot(u.t_array, u.theta_array)
    plt.title("Pendulum Angle")
    plt.xlabel("Time [t]")
    plt.ylabel("Theta [radians]")
    plt.show()

    # kinetic energy
    plt.plot(u.t_array, u.kinetic)
    plt.title("Kinetic Energy")
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.show()

    # potential energy
    plt.plot(u.t_array, u.potential)
    plt.title("Potential Energy")
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.show()

    # sum of potential and kinetic energy
    plt.plot(u.t_array, u.kinetic + u.potential)
    plt.title("Total Amount of Energy")
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.show()

    # total energy with dampered
    h = DamperedPendulum(B=0.2)
    h.solve((np.pi/2, 0), 10, 0.1)
    plt.plot(h.t_array, h.kinetic + h.potential)
    plt.title("Total Amount of Energy")
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.show()
