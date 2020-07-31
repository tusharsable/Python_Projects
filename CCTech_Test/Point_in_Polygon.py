from polygon_class import Polygon,Point

# get proper coords from string
def input_to_coords(x):
 
    x = x.replace('[','')
    x = x.replace(']','')
    x = x.split(',')
    return [float(num) for num in x ]


if __name__ == "__main__":  

    #Get Coordinates Of polygon
    x = input('Enter The Coordinates of polygon')
    coords_polygon=input_to_coords(x)

    #Check If coordinates with x and y are given 
    length = len(coords_polygon)
    if length%2:
        print('Please enter proper co-ordinates') 
        exit()
    
    #Get Coordinates to check if within a polygon
    x = input('Enter The Coordinates of point to check if within polygon:')
    point_check=input_to_coords(x)
    point_check = Point(point_check[0],point_check[1])
   
    #create polygon
    my_polygon = Polygon(coords_polygon)
    
    #check point in
    if my_polygon.check_point_in_polygon(point_check):
        print('The Point lies in the polygon')
    else:
        print('The Point does not lies in the polygon')



         
        
     
    