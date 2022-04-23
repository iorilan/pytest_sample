import random
import math
import pytest
import time

def setup():
    print('Simulate setting up...')
    # do something
    time.sleep(random.randint(0, 3))
    print('Done')

@pytest.fixture
def rand():
    """
        return a random int in [0, 1000]
    """
    v = random.randint(0, 1000)
    print(v)
    return v

@pytest.fixture
def rand_div(n):
    """
        return a random number % n == 0
    """
    v = random.choice([x*n for x in range(0, 100)])
    return v

@pytest.fixture
def triangle(n1, n2):
    """
        return triangle hypotenuse
    """
    return math.sqrt(math.pow(n1, 2) + math.pow(n2, 2))

# <more test data> ...