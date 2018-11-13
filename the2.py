def inside(x, y, points):

    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside



def calculateActuator(p1,p2):
	ipx = None
	ipy = None
	if p1[0][0] == p1[1][0]:
		if p2[0][0] == p2[1][0]:
			return 0
		else:
			ipx = p1[0][0]
		if p2[0][1] == p2[1][1]:
			ipy = p2[0][1]
		if(ipy == None):			
			m=(p2[1][1]-p2[0][1])/(p2[1][0]-p2[0][0])
			ipy = (ipx-p2[1][0])*m+p2[1][1]



	if p1[0][1] == p1[1][1]:
		if p2[0][1] == p2[1][1]:
			return 0
		else:
			ipy = p1[0][1]
		if p2[0][0] == p2[1][0]:
			ipx = p2[0][0]
		if(ipx == None):			
			m=(p2[1][1]-p2[0][1])/(p2[1][0]-p2[0][0])
			ipx=(ipy-p2[0][1])/m-p2[0][0]




	if p2[0][0] == p2[1][0]:
		if p1[0][0] == p1[1][0]:
			return 0
		else:
			ipx = p2[0][0]
		if p1[0][1] == p1[1][1]:
			ipy = p1[0][1]

		if(ipy == None):			
			m=(p1[1][1]-p1[0][1])/(p1[1][0]-p1[0][0])
			ipy = (ipx-p1[1][0])*m+p1[1][1]

	if p2[0][1] == p2[1][1]:
		if p1[0][1] == p1[1][1]:
			return 0
		else:
			ipy = p2[0][1]
		if p1[0][0] == p1[1][0]:
			ipx = p1[0][0]

		if(ipx == None):			
			m=(p1[1][1]-p1[0][1])/(p1[1][0]-p1[0][0])
			ipx=(ipy-p1[0][1])/m-p1[0][0] 
	if ipx == None and ipy == None:
		M_line0=(p1[1][1]-p1[0][1])/(p1[1][0]-p1[0][0])
		M_line1=(p2[1][1]-p2[0][1])/(p2[1][0]-p2[0][0])
		ipx=(M_line1*p2[0][0]-M_line0*p1[0][0]+p1[0][1]-p2[0][1])/(M_line1-M_line0)
		ipy=M_line0*ipx-p1[0][0]*M_line0+p1[0][1]
	return (ipx,ipy)	
	
def intersec(p1,p2):
	cl1=[min(p1[0][0],p1[1][0]),max(p1[1][0],p1[0][0])]
	cl2=[min(p2[0][0],p2[1][0]),max(p2[1][0],p2[0][0])]
	sum_cl=[max(cl1[0],cl2[0]),min(cl1[1],cl2[1])]
	cl3=[min(p1[0][1],p1[1][1]),max(p1[1][1],p1[0][1])]
	cl4=[min(p2[0][1],p2[1][1]),max(p2[1][1],p2[0][1])]
	sum_cl1=[max(cl3[0],cl4[0]),min(cl3[1],cl4[1])]
	
	if cl1[1]<cl2[0] or cl3[1]<cl4[0]:
		return 0

	x = calculateActuator(p1,p2) 

	if  x != 0:

		if ((x[0]<sum_cl[0] or x[0]>sum_cl[1])) or ((x[1]<sum_cl1[0] or x[1]>sum_cl1[1])):
			return 0
		return x
	else:
		return 0
		
def minority_shape_intersect(poly1,poly2):
	intersection_points=[]
	for i in range(len(poly1)):
		for j in range(len(poly2)):
			if i == len(poly1)-1:
				p1=[poly1[i],poly1[0]]
			else:
				p1=[poly1[i],poly1[i+1]]
			if j == len(poly2)-1:
				p2=[poly2[j],poly2[0]]
			else:
				p2=[poly2[j],poly2[j+1]]

			x=intersec([(p1[0][0]*1.0, p1[0][1]*1.0),(p1[1][0]*1.0,p1[1][1]*1.0)], \
				[(p2[0][0]*1.0, p2[0][1]*1.0),(p2[1][0]*1.0,p2[1][1]*1.0)])
			if x != 0:
				intersection_points.append(x)

	for i in range(len(poly1)):
		if inside(poly1[i][0], poly1[i][1], poly2):
			intersection_points.append(poly1[i])
	for j in range(len(poly2)):
		if inside(poly2[j][0], poly2[j][1], poly1):
			intersection_points.append(poly2[j])


	return intersection_points	
