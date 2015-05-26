import matplotlib.pyplot as plt

def Casteljau(points):

	main_list = []
	x_values = []
	y_values = []
	midpoints = []
	
	main_list.append(points)
	points = main_list[0]
	
	for i in range(0, len(points)):
		x = points[i][0]
		y = points[i][1]
		x_values.append(x)
		y_values.append(y)

		plt.plot(x, y, 'ro')



	for n in range(0, len(x_values) - 1):
		mid_x = float((x_values[n] + x_values[n + 1])) / 2
		mid_y = float((y_values[n] + y_values[n + 1])) / 2

		mid = [mid_x, mid_y]
		midpoints.append(mid)


		plt.plot(mid_x, mid_y, 'bo')
		plt.axis([-10, 10, -10, 10])
		plt.plot()
    	plt.show()
	
	print midpoints


Casteljau([[1,0], [1,1], [2,0], [3,4]])