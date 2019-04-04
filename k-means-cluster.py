from statistics import mean
from basic_decode import decodeMorse

def pointsCollector(content):
    storage = ""
    time_points = []
    for bit in content:
        if storage == "" or bit in storage:
            storage += bit
        else:
            time_points.append(len(storage))
            storage = bit
    time_points.append(len(storage))
    return time_points

def kmeans(content, centroids = 3):
    # Centroids should always equal 3, unless the message is less than one word
    # One-word messages require 2 centroids instead
    points = pointsCollector(content)
    lowest = sorted(points)[0]
    highest = sorted(points)[-1]

    if centroids == 3:
        centroid_1 = (3 * lowest + highest) / 4
        centroid_2 = (lowest + highest) / 2
        centroid_3 = highest
        # Originally used (3 * highest + lowest) / 4, but this created a bias
        # towards long-spaces (between words)

        cluster_1 = [point for point in points if abs(point - centroid_1) < abs(point - centroid_2) and abs(point - centroid_1) < abs(point - centroid_3)]
        cluster_2 = [point for point in points if abs(point - centroid_2) < abs(point - centroid_1) and abs(point - centroid_2) < abs(point - centroid_3)]
        cluster_3 = [point for point in points if abs(point - centroid_3) < abs(point - centroid_2) and abs(point - centroid_3) < abs(point - centroid_1)]

        while True:
            if centroid_1 == mean(cluster_1) and centroid_2 == mean(cluster_2):
                if centroid_3 == mean(cluster_3):
                    return [set(cluster_1), set(cluster_2), set(cluster_3)]
            centroid_1 = mean(cluster_1)
            centroid_2 = mean(cluster_2)
            centroid_3 = mean(cluster_3)

            cluster_1 = [point for point in points if abs(point - centroid_1) < abs(point - centroid_2) and abs(point - centroid_1) < abs(point - centroid_3)]
            cluster_2 = [point for point in points if abs(point - centroid_2) < abs(point - centroid_1) and abs(point - centroid_2) < abs(point - centroid_3)]
            cluster_3 = [point for point in points if abs(point - centroid_3) < abs(point - centroid_2) and abs(point - centroid_3) < abs(point - centroid_1)]

    if centroids == 2:
        centroid_1 = lowest
        centroid_2 = highest

        cluster_1 = [point for point in points if abs(point - centroid_1) < abs(point - centroid_2)]
        cluster_2 = [point for point in points if abs(point - centroid_2) < abs(point - centroid_1)]

        while True:
            if centroid_1 == mean(cluster_1) and centroid_2 == mean(cluster_2):
                    return [set(cluster_1), set(cluster_2)]
            centroid_1 = mean(cluster_1)
            centroid_2 = mean(cluster_2)

            cluster_1 = [point for point in points if abs(point - centroid_1) < abs(point - centroid_2)]
            cluster_2 = [point for point in points if abs(point - centroid_2) < abs(point - centroid_1)]


def decodeBitsAdvanced(contents):
    data = kmeans(contents, 3)
    output = ""
    dict = {}
    print(data[0], data[1], data[2])
    for num in data[0]:
        dict["0" * num] = ""
        dict["1" * num] = "."
    for num in data[1]:
        dict["0" * num] = " "
        dict["1" * num] = "-"
    for num in data[2]:
        dict["0" * num] = "   "
        dict["1" * num] = "-"

    storage = ""
    for bit in contents:
        if bit in storage or storage == "":
            storage += bit
        else:
            output += dict[storage]
            storage = bit
    output += dict[storage]
    return output

print(decodeMorse(decodeBitsAdvanced("0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000")))
