import math

# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_neighbours =  find_k_nearest_neighbors(examples, features, k)
    k_nearest_neighbours_labels = [examples[pid][label_key] for pid in  k_nearest_neighbours]
    return round(sum(k_nearest_neighbours_labels)/k)
    


def find_k_nearest_neighbors(examples, features, k):
    distances = {}
    for pid, features_label_map in examples.items():
        distance = get_euclidian_distance(features, features_label_map["features"])
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]

def get_euclidian_distance(features, other_festures):
    squired_differences = []
    for i in range(len(features)):
        squired_differences.append((other_festures[i]-features[i])**2)
    return math.sqrt(sum(squired_differences))
                                   




