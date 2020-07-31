from polygon_class import Polygon,Point,Segment
import math
import numpy as np
# find intersection Of points 
def find_intersection(line,segment):
    
    #Get line equations of both segments
    line_eqn=line.eqn_line()
    seg_eqn=segment.eqn_line()

    #Get A and B
    A = np.array([line_eqn[0],seg_eqn[0]])
    B = np.array([line_eqn[1],seg_eqn[1]])

    #solve the linear equations
    C = list(np.linalg.solve(A, B))
    intersection = Point(C[0],C[1])

    #Return point of intersection of the lines
    return intersection

# get proper coords from string
def input_to_coords(x):

    x = x.replace('[','')
    x = x.replace(']','')
    x = x.split(',')
    return [float(num) for num in x ]

# Calculate area under sunlight
def calculate_sun_lit_length(buildings,sun_coord):
    
    #Sort Buildings according to disttance form sun
    buildings = sort_bldg_by_distance(buildings,sun_coord)

    #Sort vertices according to angle made with sun
    ls = sorted( buildings[0].vertices ,key = lambda x: sun_coord.theta(x))

    #get the shadow region between the minimum and maximum angle of each vertices
    shadow_region = [ls[0],ls[-1]]

    #calculate lit length from the coordinates of vertices where the lit area resides
    length_in_light = ls[0].light_length(ls[-1])
 
    
    for building in buildings[1:] :
        
        building.vertices = sorted( building.vertices ,key = lambda x: x.theta(sun_coord))
        #if next building hides in shadow region completely of first building
        if building.vertices[0].theta(sun_coord)>shadow_region[0].theta(sun_coord) and building.vertices[-1].theta(sun_coord)<shadow_region[1].theta(sun_coord):
            continue
        # if building Doesnt hide in the shadow region of earlier building
        elif building.vertices[0].theta(sun_coord)>shadow_region[-1].theta(sun_coord) or building.vertices[-1].theta(sun_coord)<shadow_region[0].theta(sun_coord):
            
            #add lit area 
            length_in_light = building.vertices[0].light_length(building.vertices[-1])

            #change shadow region
            shadow_region[-1] = building.vertices[-1]
        # if building partially hides 
        elif building.vertices[-1].theta(sun_coord)>shadow_region[-1].theta(sun_coord):
            
            #Get segment which is intersecting with light ray
            segment = [x for x in building.segments if (x.point1.x == x.point2.x) and (x.point2.x== building.vertices[0].x) ][0]

            #Get Segment of light ray
            line= Segment(sun_coord,shadow_region[1])

            #find intersection of the two rays
            ray_intersection = find_intersection(line,segment)

            #find lit area between the intersection and the max angle vertice
            length_in_light += ray_intersection.light_length(building.vertices[-1])

            #change shadow region
            shadow_region[-1] = building.vertices[-1]

            #change shadow region
            shadow_region[0] = building.vertices[0]

        # if building Partially hides
        elif building.vertices[0].theta(sun_coord)<shadow_region[0].theta(sun_coord):
            
            #Get segment which is intersecting with light ray
            segment = [x for x in building.segments if (x.point1.x == x.point2.x) and (x.point2.x== building.vertices[-1].x) ][0]

            #Get Segment of light ray intersecting the segment
            line= Segment(sun_coord,shadow_region[0])


            #find intersection of the two rays
            ray_intersection = find_intersection(line,segment)

            #find lit area between the intersection and the min angle vertex
            length_in_light += ray_intersection.light_length(building.vertices[0])

            #change shadow region
            shadow_region[0] = building.vertices[0]

         
    return length_in_light

#sort buildings according to distance from sun coordinates
def sort_bldg_by_distance(buildings,sun_coord):
    ls=[]
    for building in buildings:
        distance = building.vertices[0].distance(sun_coord)
        ls.append((distance,building))
    ls = sorted(ls ,key = lambda x: x[0])
    ls = [bldg for (distance,bldg) in ls]
    return ls

        
     
if __name__ == "__main__":  

    #get coordinates of rectangular building
    x = input('Enter The Coordinates of polygon')
    coords_polygon= input_to_coords(x)

    #Checck if all 4 coordinates of rectangular building are given
    length = len(coords_polygon)
    if length%8:
        print('please enter proper building co-ordinates') 
        exit()

    #Create Polygon from coordinates
    buildings=[]
    i=0
    while i<length :
        
        buildings.append(Polygon(coords_polygon[i:i+8]))
        i+=8

    #Get coordinates of sun
    x = input('Enter the Coordinates of sun')
    sun_coord_flt=input_to_coords(x)
    sun_coord = Point(sun_coord_flt[0],sun_coord_flt[1])
    
    #calculate length under light
    length = calculate_sun_lit_length(buildings,sun_coord)
    print('the length is = ',length)

   





    

    