import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class DoublePendulum:
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2

    def __call__(self, t, y):
        M1 = self.M2
        L1 = self.L1
        M2 = self.M2
        L2 = self.L2

        g = 9.81

        theta_1 = y[0]
        omega_1 = y[1]
        theta_2 = y[2]
        omega_2 = y[3]

        del_theta = theta_2 - theta_1

        d_theta_1 = omega_1
        d_theta_2 = omega_2

        A1 = M2*L1*omega_1**2*np.sin(del_theta)*np.cos(del_theta)
        B1 = M2*g*np.sin(theta_2)*np.cos(del_theta)
        C1 = M2*L2*omega_2**2*np.sin(del_theta)
        D1 = (M1+M2)*g*np.sin(theta_1)
        E1 = (M1+M2)*L1
        F1 = M2*L1*np.cos(del_theta)**2

        d_omega_1 = (A1 + B1 + C1 - D1)/(E1-F1)

        A2 = M2*L2*omega_2**2*np.sin(del_theta)*np.cos(del_theta)
        B2 = D1*np.cos(del_theta)
        C2 = (M1+M2)*L1*omega_1**2*np.sin(del_theta)
        D2 = (M1+M2)*g*np.sin(theta_2)
        E2 = (M1+M2)*L2
        F2 = M2*L2*np.cos(del_theta)**2

        d_omega_2 = (-A2+B2-C2-D2)/(E2-F2)

        return (d_theta_1, d_omega_1, d_theta_2, d_omega_2)

    def solve(self, y0, T, dt, angles="rad"):

        self.dt = dt

        # option to convert
        # from radians to degrees
        for i in range(0, 4):
            if angles == "deg":
                y0[i] = 180/np.pi * y0[i]

        fun = self.__call__
        # time interval from 0 to T
        q = (0, T)

        steps = int(T/dt)
        eval = np.linspace(0, T, steps)

        a = scipy.integrate.solve_ivp(fun, q, y0, t_eval=eval, method="Radau")

        self.t_array = a.t
        self.theta_array1 = a.y[0]
        self.omega_array1 = a.y[1]
        self.theta_array2 = a.y[2]
        self.omega_array2 = a.y[3]

    @property
    def t(self):
        return self.t_array

    @property
    def theta1(self):
        return self.theta_array1

    @property
    def theta2(self):
        return self.theta_array2

    @property
    def x1(self):
        x1 = self.L1*np.sin(self.theta_array1)
        return x1

    @property
    def y1(self):
        y1 = -self.L1*np.cos(self.theta_array1)
        return y1

    @property
    def x2(self):
        x2 = self.x1 + self.L2*np.sin(self.theta_array2)
        return x2

    @property
    def y2(self):
        y2 = self.y1 - self.L2*np.cos(self.theta_array2)
        return y2

    @property
    def potential(self):
        g = 9.81
        P1 = self.M1*g*(self.y1 + self.L1)
        P2 = self.M2*g*(self.y2 + self.L1 + self.L2)
        return P1 + P2

    @property
    def vx1(self):
        return np.gradient(self.x1, self.t_array)

    @property
    def vy1(self):
        return np.gradient(self.y1, self.t_array)

    @property
    def vx2(self):
        return np.gradient(self.x2, self.t_array)

    @property
    def vy2(self):
        return np.gradient(self.y2, self.t_array)

    @property
    def kinetic(self):
        K1 = 1/2*self.M1*(self.vx1**2+self.vy1**2)
        K2 = 1/2*self.M2*(self.vx2**2+self.vy2**2)
        return K1 + K2

    def create_animation(self):

        # Create empty figure
        fig = plt.figure()

        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-', lw=2)

        # Call FuncAnimation
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)),
                                                 repeat=None,
                                                 interval=1000*self.dt,
                                                 blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        plt.show()

    def save_animation(self, filename):
        self.animation.save(filename, fps=60)


if __name__ == "__main__":
    u = DoublePendulum()
    u.solve((1, 1, 1, 1), 10, 1/60)
    u.create_animation()

    # u.save_animation("example_simulation.mp4")
    u.show_animation()

    # Plotting of chaotic
    # system of three
    # pendula
    v = DoublePendulum()
    w = DoublePendulum()

    v.solve((1, 1.2, 1, 1.2), 10, 0.01)
    w.solve((1, 1.4, 1, 1.4), 10, 0.01)

    fig = plt.figure()

    color = ["blue", "orange", "red"]
    pendula = [u, v, w]

    for i in range(3):
        ax1 = fig.add_subplot(221 + i)
        ax1.title.set_text(f"y0 = (1, {1+0.2*i}, 1, {1+0.2*i})")
        ax1.plot(pendula[i].x2, pendula[i].y2, color[i])

    fig.tight_layout(pad=3.0)
    plt.savefig("chaotic_pendulum.png")
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
    plt.title("Total Amount Energy")
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.show()
