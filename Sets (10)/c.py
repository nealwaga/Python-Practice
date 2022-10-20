# Join Two Sets. Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print (set3)


# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"strawberry", "cherry", "blueberry"}
y = {"microsoft", "google", "strawberry"}
x.intersection_update(y)
print (x)


# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
a = {"strawberry", "cherry", "blueberry"}
b = {"microsoft", "google", "strawberry"}
a.symmetric_difference_update(b)
print (a)