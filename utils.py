from sys import exit as nelxd
try: 
    import sys 
    import numpy as np
    import json
except ImportError as err: 
    nelxd(err)



class DetectColor: 

    def hsv_tostring(self,hsv): 
        ## Basically, if it is within a certain parameter of HSV values, 
        ## it will display a color name
        ## e.g. if HSV value is between (110,119,148) and (255,255,255) will display "orange"

     # Blue color
        high_blue = np.array([126, 255, 255])
        low_blue = np.array([94, 80, 2])   
    # Green color
        high_green = np.array([90, 255, 172])
        low_green = np.array([59, 91, 67])     
    # Red color
        high_red = np.array([255, 255, 185])
        low_red = np.array([157, 0, 0])
    # Yellow Color
        high_yellow = np.array([63,162,255])
        low_yellow = np.array([5,52,73])
        
    # Orange Color
        high_orange = np.array([255,255,255])
        low_orange = np.array([110,119,148])
        
    # White Color
        high_white = np.array([144,106,226])
        low_white = np.array([87,0,90])
        

        (h,s,v) = hsv 
        if (h> low_blue[0]) and (h<high_blue[0]) and (s>low_blue[1]) and (s<high_blue[1]) and (v>low_blue[2]) and (v<high_blue[2]): 
            return 'blue'
        elif (h> low_green[0]) and (h<high_green[0]) and (s>low_green[1]) and (s<high_green[1]) and (v>low_green[2]) and (v<high_green[2]):
            return 'green'
        elif (h> low_red[0]) and (h<high_red[0]) and (s>low_red[1]) and (s<high_red[1]) and (v>low_red[2]) and (v<high_red[2]):
            return 'red'
        elif(h> low_yellow[0]) and (h<high_yellow[0]) and (s>low_yellow[1]) and (s<high_yellow[1]) and (v>low_yellow[2]) and (v<high_yellow[2]):
            return 'yellow'
        elif (h> low_orange[0]) and (h<high_orange[0]) and (s>low_orange[1]) and (s<high_orange[1]) and (v>low_orange[2]) and (v<high_orange[2]):
            return 'orange' 
        else: 
            return 'white'

    def stringtoRGB(self,name): 
        ## From the string collected above, the correct rgb code is returned 
        color = {
            'red'    : (0,0,255), 
            'orange' : (0,165,255), 
            'blue'   : (255,0,0), 
            'green'  : (0,255,0), 
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
        }
        return color[name]
    def average_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        for y in range(len(roi)):
            if y % 2 == 0:
                for x in range(len(roi[y])):
                    if x % 2 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
        h /= num
        s /= num
        v /= num
        return (int(h), int(s), int(v))

detectColor = DetectColor()

class Combine:

    def sides(self, sides):
        combined = ''
        for face in 'URFDLB':
            combined += ''.join(sides[face])
        return combined

combine = Combine()

class Normalizer:

    def algorithm(self, alg, language):
        """
        Normalize an algorithm from the
        json-written manual.

        :param alg: The algorithm itself
        :returns: list
        """

        with open('solution-strings.json') as f:
            manual = json.load(f)

        solution = []
        for notation in alg.split(' '):
            solution.append(manual[language][notation])
        return solution

normalize = Normalizer()

