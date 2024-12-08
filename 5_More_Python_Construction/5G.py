# simple_oscillator.py
def F(y, t):
    """
    Return derivatives for second-order ODE y'' = -y.
    """
    dy = [0, 0]         # Create a list to store derivatives.
    dy[0] = y[1]        # Store first derivative of y(t).
    dy[1] = -y[0]       # Store second derivative of y(t).
    return dy
