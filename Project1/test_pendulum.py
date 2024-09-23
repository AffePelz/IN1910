import unittest
import numpy as np
from pendulum import Pendulum


class TestPendulum(unittest.TestCase):
    def test_Pendulum(self):
        expected_theta = 0.15
        expected_omega = -(109/180)*np.pi

        instance = Pendulum(L=2.7)
        theta, omega = (np.pi/6, 0.15)
        d_theta, d_omega = instance(99, (theta, omega))
        computed_theta = d_theta
        computed_omega = d_omega

        self.assertAlmostEqual(expected_theta, computed_theta)
        self.assertAlmostEqual(expected_omega, computed_omega)

    def test_Pendulumrest(self):
        expected_theta = 0
        expected_omega = 0

        instance = Pendulum(L=2.7)
        theta, omega = (0, 0)
        d_theta, d_omega = instance(99, (theta, omega))
        computed_theta = d_theta
        computed_omega = d_omega

        self.assertAlmostEqual(expected_theta, computed_theta)
        self.assertAlmostEqual(expected_omega, computed_omega)

    def test_raiseError(self):
        u = Pendulum(L=3.4)
        with self.assertRaises(AttributeError):
            u.t
            u.theta
            u.omega

    def test_zeros(self):
        u = Pendulum(L=3.4)
        u.solve((0, 0), 10, 1)
        expected_theta_array = np.zeros(10)
        expected_omega_array = np.zeros(10)
        computed_theta_array = u.theta
        computed_omega_array = u.omega
        for i in range(10):
            self.assertAlmostEqual(expected_theta_array[i],
                                   computed_theta_array[i])
            self.assertAlmostEqual(expected_omega_array[i],
                                   computed_omega_array[i])

    def test_radius_and_length(self):
        u = Pendulum(L=3.4)
        L = 3.4
        u.solve((1, 1), 10, 1)
        x = u.x
        y = u.y
        for i in range(len(x)):
            radiuspower2 = (x[i])**2 + (y[i])**2
            self.assertAlmostEqual(L**2, radiuspower2)


if __name__ == '__main__':
    unittest.main()
