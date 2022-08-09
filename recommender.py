import cmath
import numpy as np

def euclidean_distance(a,b,x,y):
    return abs(b-a)

def cosine_similarity(a,b,x,y):
    cos_theta = a*x+b*y
    cos_theta /= (abs(a)*abs(x))
    theta = np.arccos(cos_theta)
    return theta

# print(np.arccos(0.5))
