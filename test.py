import numpy as np
import pytest

x = np.zeros((3,3))
print(x)

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        capital_case(9)

        
test_raises_exception_on_non_string_arguments()
test_capital_case()