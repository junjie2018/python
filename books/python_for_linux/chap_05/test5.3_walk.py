import os
import fnmatch

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("D:\\ProjectToDispose"):
    for extension in images:
        for filename in fnmatch.filter(filenames, extension):
            matches.append(os.path.join(root, filename))
print(matches)
