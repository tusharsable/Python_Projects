import numpy as np
import math

class Polygon():
    def __init__(self,coords_polygon):
        self.vertices=self.get_vertices(coords_polygon)
        
        self.segments = self.get_segments()

    #Get Segments from vertices
    def get_segments(self):

        seg_list=[] 
        point_list = [Segment(p[0],p[1]) for p in zip(self.vertices, self.vertices[1:])]
        seg_list.extend(point_list)
        seg_list.append(Segment(self.vertices[-1],self.vertices[0]))

        return seg_list
    
    #Get vertices of polygon from a list of coordinates
    def get_vertices(self,coords_polygon):   
        i=0
        vertices=[]
        while i< len(coords_polygon) :
            
            vertices.append(Point(coords_polygon[i],coords_polygon[i+1]))
            i+=2

        return vertices

    #Check If Point Within a Polygon
    def check_point_in_polygon(self,point):
        new_point = Point(1000000,point.y)
        new_seg = Segment(point,new_point)
        count=0

        for seg in self.segments:
            if seg.check_intersection(new_seg) :
                
                if seg.orientation(point) == 0:
                    return seg.point_on_segment(point)

            count+=1
        
        return count%2

class Segment():
    def __init__(self,p1,p2):
       
        self.point1=p1
        self.point2=p2
    
    #check intersection of segment with another
    def check_intersection(self,seg):

        o1 = self.orientation(seg.point1)
        o2 = self.orientation(seg.point2)
        o3 = seg.orientation(self.point1) 
        o4 = seg.orientation(self.point2)

        if ((o1 != o2) & (o3 != o4)):
            return True
  
        # Special Cases 
        ## self.point1, self.point2, seg.point1 are colinear and seg.point1  lies on segment self 
        if (o1 == 0 and self.point_on_segment(seg.point1)):
            return True
  
        # self.point1, self.point2, seg.point2 are colinear and seg.point2 lies on segment self 
        if (o2 == 0 and self.point_on_segment(seg.point2)):
            return True
  
        # seg.point1, seg.point2, self.point1 and self.point1 lies on segment seg 
        if (o3 == 0 and seg.point_on_segment(self.point1)):
            return True
  
        # seg.point1, seg.point2, self.point2 and self.point1 lies on segment seg  
        if (o4 == 0 and seg.point_on_segment(self.point2)):
            return True
  
        # If point Doesn't fall in any of the above cases 
        return False 
  
    def point_on_segment(self,r):
        
        if (r.x<= max(self.point1.x , self.point2.x) and  r.x>= min(self.point1.x,self.point2.x ) and 
            r.y<= max(self.point1.y, self.point2.y ) and  r.y>= min(self.point1.y, self.point2.y)) :
        
            return True
        return False


    def slope(self):
       

        return self.point1.theta(self.point2)

    #get orientation
    def orientation(self,r):
        segment_pq = self
        segment_qr = Segment(self.point2,r)
        
        orientation = segment_pq.slope() - segment_qr.slope()

        if orientation < 0:
            return -1
        elif orientation > 0:
            return +1
        elif orientation == 0:
            return 0

    #length of segment
    def length(self):
        self.point1.distance(self.point2)
    
    #get coefficients of x,y and constant c in equation of line Ax + By =C
    def eqn_line(self):
        x1 = self.point1.x
        x2 = self.point2.x
        y1 = self.point1.y
        y2 = self.point2.y

        coef_x_y=[(y1-y2),(x2-x1)]
        const=(y1*(x2-x1)-x1*(y2-y1))
        return[coef_x_y,const]
    

class Point():
    
    def __init__(self,x1,y1):

        self.x=x1
        self.y=y1

    #find distance between point2 and self
    def distance(self,point2):

        return math.sqrt((point2.x - self.x)**2 + (point2.y - self.y)**2)
    
    #find angle of point 2 w.r.t self
    def theta(self,point2):

        try:
             return math.atan((point2.y-self.y)/(point2.x-self.x))
        except ZeroDivisionError:
            return 1.5708
    
    #find length under light
    def light_length(self,point2):

        return abs(abs(point2.y-self.y) + abs(point2.x-self.x))