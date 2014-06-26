"""
This module adds n-dimensional vector definitions and operand support.
"""
from math import sqrt
    
class vector():
    """
    This vector class handles n-dimensional vectors.
    
    It also introduces the following methods for n-dimensional vector operands:
    """
    def __init__(self, *x):
        """
        Either input n integer or floating point args or an n length list to define an n-dimensional vector.
        """
        self.v = []
        if isinstance(x[0], list):
            for i in x[0]:
                self.v.append(i)
        elif isinstance(x[0], int) or isinstance(x[0], float):
            for i in x:
                self.v.append(i)
        self.dimension = len(self.v)
        
    def __str__(self):
        """
        Handles string outputs for the vector class allowing for print statments.
        """
        return str(self.v)
        
    def __add__(self,other):
        """
        Handles vector addition using the standard + operator.
        """
        self.o = []
        if len(self.v) == len(other.v):
            for i in range(0,len(self.v)):
                self.o.append(self.v[i]+other.v[i])
        else:
            raise ArithmeticError()
            
        return vector(self.o)       
        
    def __sub__(self,other):
        """
        Handles vector subtraction using the standard - operator.
        """
        self.o = []
        if len(self.v) == len(other.v):
            for i in range(0,len(self.v)):
                self.o.append(self.v[i]-other.v[i])
        else:
            raise ArithmeticError()
            
        return vector(self.o)
    
    def __mul__(self,other):  
        """
        Handles vector component multiplication with scalars or vectors using the standard * operator.
        """  
        if isinstance(other, int) or isinstance(other, float):
            self.o = []
            for i in range(0,len(self.v)):
                    self.o.append(self.v[i]*other)
            
        elif isinstance(other, vector):
            self.o = []
            if len(self.v) == len(other.v):
                for i in range(0,len(self.v)):
                    self.o.append(self.v[i]*other.v[i])
            else:
                raise ArithmeticError()
        else:
            raise TypeError()
        return vector(self.o)

    def __truediv__(self,other):
        """
        Handles vector division by scalars using the standard / operator.
        """
        if isinstance(other, int) or isinstance(other, float):
            self.o = []
            for i in range(0,len(self.v)):
                    self.o.append(self.v[i]/other)
        return vector(self.o)
    
    def compsum(self):
        """
        Returns the sum of the components of a vector.
        """
        self.sm = 0
        for i in self.v:
            self.sm += i
        return(self.sm)

    def __abs__(self):
        """
        Returns the magnitude of a vector using the standard abs() function.
        """
        self.prod = self*self
        return sqrt(self.prod.compsum())
        
    def dot(self,other):
        """
        Allows dot-product multiplication with another vector.
        """
        self.o = []
        if len(self.v) == len(other.v):
            for i in range(0,len(self.v)):
                self.o.append(self.v[i]*other.v[i])
        else:
            raise ArithmeticError()
        return sum(self.o)

    def cross(self,other):
        """
        Allows cross-product multiplication with another vector.
        """
        if self.dimension == 3 and other.dimension == 3:
            return vector((self.v[1]*other.v[2] - self.v[2]*other.v[1]), -(self.v[0]*other.v[2] - self.v[2]*other.v[0]),(self.v[0]*other.v[1] - self.v[1]*other.v[0]))
        else:
            raise ArithmeticError()

    def component(self,x):
        """
        Returns the value of a specific vector component.
        """
        if x <= len(self.v)-1:
            return(self.v[x])
        else:
            raise IndexError()

    def stp(self,other1,other2):
        """
        Allows scalar-triple-product multiplication with two other vectors.
        a.stp(b,c) is equivilent to 'a dot (b cross c)'.
        """
        return self.dot(other1.cross(other2))

    def vtp(self,other1,other2):
        """
        Allows vector-triple-product multiplication with two other vectors.
        a.stp(b,c) is equivilent to 'a cross (b cross c)'.
        """
        return self.cross(other1.cross(other2))

    def perpdot(self,other):
        """
        Allows perpendicular dot-product multiplication with another vector.
        This is equivilent to the dot product of two vectors, where the second vector has been rotated by 180 degrees.
        """
        return abs(self.cross(other))

    def normalize(self):
        """
        Returns a unit vector in the direction of the initial vector.
        """
        return self/abs(self)


