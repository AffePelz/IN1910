import numpy as np
import pytest
import unittest
from double_pendulum import DoublePendulum

G = 9.81
M1 = 1
M2 = 1
L1 = 1
L2 = 1
omega1 = 0.15
omega2 = 0.15


def delta(theta1, theta2):
    return theta2 - theta1


def domega1_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    del_theta = delta(theta1, theta2)

    A1 = M2*L1*omega1**2*np.sin(del_theta)*np.cos(del_theta)
    B1 = M2*G*np.sin(theta2)*np.cos(del_theta)
    C1 = M2*L2*omega2**2*np.sin(del_theta)
    D1 = (M1+M2)*G*np.sin(theta1)
    E1 = (M1+M2)*L1
    F1 = M2*L1*np.cos(del_theta)**2

    domega1_dt = (A1 + B1 + C1 - D1)/(E1-F1)
    return domega1_dt


def domega2_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    del_theta = delta(theta1, theta2)

    A2 = M2*L2*omega2**2*np.sin(del_theta)*np.cos(del_theta)
    B2 = (M1+M2)*G*np.sin(theta1)*np.cos(del_theta)
    C2 = (M1+M2)*L1*omega1**2*np.sin(del_theta)
    D2 = (M1+M2)*G*np.sin(theta2)
    E2 = (M1+M2)*L2
    F2 = M2*L2*np.cos(del_theta)**2

    domega2_dt = (-A2+B2-C2-D2)/(E2-F2)
    return domega2_dt


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5235987755982988, 0.5235987755982988),
        (0.5235987755982988, 0, -0.5235987755982988),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_delta(theta1, theta2, expected):
    assert abs(delta(theta1, theta2) - expected) < 1e-10


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, 3.4150779130841977),
        (0.5235987755982988, 0, -7.864794228634059),
        (0.5235987755982988, 0.5235987755982988, -4.904999999999999),
    ],
)
def test_domega1_dt(theta1, theta2, expected):
    assert (
        abs(domega1_dt(M1, M2, L1, L2,
                       theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )


# 2 of these tests keep failing :(
@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, -7.8737942286340585),
        (0.5235987755982988, 0, 6.822361597534335),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    assert (
        abs(domega2_dt(M1, M2, L1, L2,
                       theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )


class TestPendulum(unittest.TestCase):
    def test_DoublePendulumrest(self):
        expected_theta1 = 0
        expected_omega1 = 0
        expected_theta2 = 0
        expected_omega2 = 0

        instance = DoublePendulum()
        theta1, omega1, theta2, omega2 = (0, 0, 0, 0)
        y = (theta1, omega1, theta2, omega2)
        d_theta1, d_omega1, d_theta2, d_omega2 = instance(99, y)
        computed_theta1 = d_theta1
        computed_omega1 = d_omega1
        computed_theta2 = d_theta2
        computed_omega2 = d_omega2

        self.assertAlmostEqual(expected_theta1, computed_theta1)
        self.assertAlmostEqual(expected_omega1, computed_omega1)
        self.assertAlmostEqual(expected_theta2, computed_theta2)
        self.assertAlmostEqual(expected_omega2, computed_omega2)

    def test_quarter_position(self):
        expected_theta1 = 0
        expected_omega1 = -9.81
        expected_theta2 = 0
        expected_omega2 = 0

        instance = DoublePendulum()
        theta1, omega1, theta2, omega2 = (np.pi/2, 0, np.pi/2, 0)
        y = (theta1, omega1, theta2, omega2)
        d_theta1, d_omega1, d_theta2, d_omega2 = instance(99, y)
        computed_theta1 = d_theta1
        computed_omega1 = d_omega1
        computed_theta2 = d_theta2
        computed_omega2 = d_omega2

        self.assertAlmostEqual(expected_theta1, computed_theta1)
        self.assertAlmostEqual(expected_omega1, computed_omega1)
        self.assertAlmostEqual(expected_theta2, computed_theta2)
        self.assertAlmostEqual(expected_omega2, computed_omega2)

    def test_length_equal_radius(self):
        u = DoublePendulum(L1=3.9, L2=9.66)
        L1 = 3.9
        L2 = 9.66
        u.solve((1, 1, 1, 1), 10, 1)
        x1 = u.x1
        y1 = u.y1
        x2 = u.x2
        y2 = u.y2
        for i in range(len(x1)):
            R1power2 = (x1[i])**2 + (y1[i])**2
            R2power2 = (x2[i] - x1[i])**2 + (y2[i] - y1[i])**2
            self.assertAlmostEqual(L1**2, R1power2)
            self.assertAlmostEqual(L2**2, R2power2)


if __name__ == '__main__':
    unittest.main()
