# Author: Spencer Mae-Croft
# Date 08/29/2020 

places = ["New York City", "Spain", "Italy", "Africa", "Canada", "Montana", "Texas"]

print("Destinations" + str(places))
print("Sorted Destinations: " + str(sorted(places)))
print("Original Destinations: " + str(places))
print("Reverse Sorted Destinations: " + str(sorted(places, reverse=True)))
print("Original Destinations: " + str(places))
places.reverse()
print("Reversed List: " + str(places))

places.reverse()
print("Reverse Back to Original: " + str(places)) 

places.sort()
print("Sorted List" + str(places))

places.sort(reverse=True)
print("Reverse Sorted List " + str(places)) 



























