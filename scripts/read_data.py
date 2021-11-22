import pydicom as dicom
import matplotlib.pylab as plt

# specify your image path
image_path = '../data/Anonymized_Set_1/Case-1/1.2.840.113619.2.327.3.279763341.513.1584337299.92/1.2.840.113619.2.327.3.279763341.513.1584337299.94.1.dcm'
ds = dicom.dcmread(image_path)

print(type(ds.pixel_array))
plt.imshow(ds.pixel_array)
plt.show()