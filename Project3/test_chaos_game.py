import pytest
import numpy as np
from chaos_game import ChaosGame


@pytest.mark.parametrize(
    "arg", [(3, 1), (3, 0), (1, 0.5)]
)
def test_init_error_exercise_2i(arg):
    """Tests error raise if n and r have illegal values.

    Parameters
    -----------
    arg: list
        contains values for n and r

    Warnings
    ---------
    At least one of n and r should have an illegal value
    """
    with pytest.raises(ValueError):
        ChaosGame(arg[0], arg[1])


@pytest.mark.parametrize(
    "arg", ["Picture.jpg", "Hello.pdf", "Unfinised."]
)
def test_savefig_error_exercise_2i(arg):
    """Tests error raise if file name/format is illegal.

    Parameters
    ---------
    arg: list
        contains file names, with specified format

    Warnings
    --------
    File name should have an illegal format
    """
    c = ChaosGame(3)
    c.iterate(10000)
    with pytest.raises(TypeError):
        c.savepng(arg)


@pytest.mark.parametrize(
    "arg, expect", [(3, [[0, 1], [np.sqrt(3)/2, -0.5], [-np.sqrt(3)/2, -0.5]])]
)
def test_corner_position_exercise_2i(arg, expect):
    """Tests if corners are in the right position.

    Parameters
    ----------
    arg: int
        Number of corners for n-gon
    expect: list
        Contains coordinates of corners
    """
    c = ChaosGame(arg)
    calculated = c.c
    for i in range(arg):
        for j in range(2):
            assert (calculated[i][j]-expect[i][j]) < 10**(-9)
