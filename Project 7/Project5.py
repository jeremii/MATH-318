# Michael Stoffel <mstoffe2@wvup.edu> and Jeremi Swann <jswann1@wvup.edu>
# WVUP Spring 2019 MATH318 Project 5

def irand(n,m): #Generate an array of length n made up of random integers between 0 and m without replacement
    import random
    b=list(range(n))
    b=random.sample(range(m),n)
    return b