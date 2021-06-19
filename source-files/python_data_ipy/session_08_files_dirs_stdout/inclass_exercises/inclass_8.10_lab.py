# 8.10:  Write a function that raises an exception.

# The function below should detect if an incorrect state name
# is passed to it, and raise a ValueError exception if it is.

import runreport

def get_tristate_pop(state):
    states = {'ny': 19.45, 'nj': 8.88, 'ct': 3.57}

    # if state is not in the states dict, please
    # raise a ValueError exception with below message


    return states[state]


popny = get_tristate_pop('ny')       # 19.45
print(popny)

popca = get_tristate_pop('ca')       # ValueError:
                                     # state "ca" not found
print(popca)

