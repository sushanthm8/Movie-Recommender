import cmath
import numpy as np

def euclidean_distance(a,b,x,y):
    return abs(b-a)

def cosine_similarity(a,b,x,y):
    cos_theta = (a*x+b*y)/(abs(a)*abs(x))
    # print(cos_theta)
    # print(cos_theta)
    theta = np.arccos(cos_theta/2)
    return theta

def similarity(a,b,x,y):
    return cosine_similarity(a,b,x,y)*euclidean_distance(a,b,x,y)
