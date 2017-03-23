# Write a function 'kalman_filter' that implements a multi-
# dimensional Kalman Filter for the example given

import matrix

########################################

# Implement the filter function below

def kalman_filter(x, P):
    for n in range(len(measurements)):

        # measurement update
        y = matrix.Matrix([[measurements[n]]]) - H*x
        s = H * P * H.transpose() + R
        K = P * H.transpose() * s.inverse()
        x = x + K*y
        P = (I-K*H) * P


        # prediction

        x = F * x + u
        P = F * P * F.transpose()

        print 'x= '
        x.show()
        print 'P= '
        P.show()
        
    return x,P

############################################
### use the code below to test your filter!
############################################

measurements = [1, 2, 3]

x = matrix.Matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix.Matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix.Matrix([[0.], [0.]]) # external motion
F = matrix.Matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix.Matrix([[1., 0.]]) # measurement function
R = matrix.Matrix([[1.]]) # measurement uncertainty
I = matrix.Matrix([[1., 0.], [0., 1.]]) # identity matrix

print kalman_filter(x, P)
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]