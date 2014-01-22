from math import sin, cos, sqrt, atan2, radians
import Point

def distance(point1, point2):
	R = 6371.0 #rayon de la terre en km (source google)

	lat1 = radians(point1.latitude)
	lon1 = radians(point1.longitude)
	lat2 = radians(point2.latitude)
	lon2 = radians(point2.longitude)

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	distance = R * c

	return distance/1000

def vitesse(point1, point2):
	return distance(point1,point2)/abs((point1.timestamp-point2.timestamp)).total_seconds()

def init_listpoints(resrequete):
	listpoints = []

	for req in resrequete:
		listpoints.append(Point.point(req[0],req[1],req[2]))

	return listpoints	