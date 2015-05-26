import matplotlib.pyplot as plt


def Casteljau(a = [], b = [], c = [], d = []):
	# These values for a, b, c, and d are the inital points
    # Each point is given in the form (x,y)

    a_x = a[0]
    a_y = a[1]
    print "P_0 = ", (float(a_x), float(a_y))
    P_0 = [a_x, a_y]

    b_x = b[0]
    b_y = b[1]
    print "P_1 = ", (float(b_x), float(b_y))
    P_1 = [b_x, b_y]
    c_x = c[0]
    c_y = c[1]
    print "P_2 = ", (float(c_x), float(c_y))
    P_2 = [c_x, c_y]

    d_x = d[0]
    d_y = d[1]
    print "P_3 = ", (float(d_x), float(d_y))
    P_3 = [d_x, d_y]

 

    # The midpoint of P_0 and P_1 is M1

    M1_x = float((a_x + b_x))/2
    M1_y = float((a_y + b_y))/2
    print "M_1 = ", (float(M1_x), float(M1_y))
    M_1 = [M1_x, M1_y]

    # The midpoint of P_1 and P_2 is M2

    M2_x = float((b_x + c_x))/2
    M2_y = float((b_y + c_y))/2
    print "M_2 = ", (float(M2_x), float(M2_y))
    M_2 = [M2_x, M2_y]
    
    # The midpoint of P_2 and P_3 is M3

    M3_x = float((c_x + d_x))/2
    M3_y = float((c_y + d_y))/2
    print "M_3 = ", (float(M3_x), float(M3_y))
    M_3 = (M3_x, M3_y)



    # The midpoint of M_1 and M_2 is Q1

    Q1_x = float((M1_x + M2_x))/2
    Q1_y = float((M1_y + M2_y))/2
    print "Q_1 = ", (float(Q1_x), float(Q1_y))
    Q_1 = [Q1_x, Q1_y]

    # The midpoint of M_2 and M_3 is Q2

    Q2_x = float((M2_x + M3_x))/2
    Q2_y = float((M2_y + M3_y))/2
    print "Q_2 = ", (float(Q2_x), float(Q2_y))
    Q_2 = [Q2_x, Q2_y]



    # The midpoint of Q_1 and Q_2 is B1

    B1_x = float((Q1_x + Q2_x))/2
    B1_y = float((Q1_y + Q2_y))/2
    print "B_1 = ", (float(B1_x), float(B1_y))
    B_1 = [B1_x, B1_y]


    # Plots the control points
    plt.plot([P_0[0], P_1[0], P_2[0], P_3[0]], [P_0[1], P_1[1], P_2[1], P_3[1]], 'ro')
    # Plots the midpoints
    plt.plot([M_1[0], M_2[0], M_3[0]], [M_1[1], M_2[1], M_3[1]], 'go')
    # Plots the secondary midpoints
    plt.plot([Q_1[0], Q_2[0]], [Q_1[1], Q_2[1]], 'yo')
    # Plots the final midpoint
    plt.plot([B_1[0]], [B_1[1]], 'bo')

    # Plots the line between the P_0 and M_1
    plt.plot([P_0[0], M_1[0]], [P_0[1], M_1[1]], 'k')
    # Plots the line between the M_1 and Q_1
    plt.plot([P_0[0], Q_1[0]], [P_0[1], Q_1[1]], 'k')
    # Plots the line between the Q_1 and B_1
    plt.plot([Q_1[0], B_1[0]], [Q_1[1], B_1[1]], 'k')
    # Plots the line between the B_1 and Q_2
    plt.plot([B_1[0], Q_2[0]], [B_1[1], Q_2[1]], 'k')
    # Plots the line between the Q_2 and M_3
    plt.plot([Q_2[0], M_3[0]], [Q_2[1], M_3[1]], 'k')
    # Plots the line between the M_3 and P_3
    plt.plot([M_3[0], P_3[0]], [M_3[1], P_3[1]], 'k')
    
    # Axis
    plt.axis([-5, 7, -5, 7])

    plt.plot()
    plt.show()

Casteljau([1,3], [2,1], [2,4], [4,3])

