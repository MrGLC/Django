from osgeo import gdal

# Open the .img file
dataset = gdal.Open('path_to_your_image.img', gdal.GA_ReadOnly)

# Read the first band of the image
band = dataset.GetRasterBand(1)
band_data = band.ReadAsArray()

# Perform operations on band_data here
# For example, calculate the mean of the data
import numpy as np
mean_value = np.mean(band_data)
print("Mean Value:", mean_value)

# Close the dataset
dataset = None

