from math import sqrt, pow

class Metrics():
   def euclidean_distance(self, X, Y):
       return  sqrt( sum( (pow(x- y, 2)) for x, y in zip(X,Y)) )

   def manhattan_distance(self, X, Y):
       return sum(abs(x-y) for x, y in zip(X,Y))

   def cosine_similarity(self, X, Y):
       
       numerator = sum((x*y) for x, y in zip(X,Y))
       denominator = sqrt(sum([x**2 for x in X])) *  sqrt(sum([y**2 for y in Y]))
       return numerator/denominator
       
   def jaccard_similarity(self, X, Y):
       inersection_cardinality = len(set.intersection(*[set(X), set(Y)]))
       union_cardinality = len(set.union(*[set(X), set(Y)]))

       print(inersection_cardinality, union_cardinality )
       return inersection_cardinality/union_cardinality


def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]


if __name__=="__main__":
    X = [1,3,4,5]
    Y = [7,6, 3,1]

    sol = distances_and_similarities(X, Y)
    print(sol)