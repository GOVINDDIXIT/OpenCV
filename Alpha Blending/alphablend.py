# cv2 (OpenCV-Python) is a library of Python bindings designed to solve computer vision problems
import cv2

# Read the foreground image with alpha channel
foreGroundImage = cv2.imread("foreGroundAsset.png", -1)

# Split png foreground image into b,g,r,a
b,g,r,a = cv2.split(foreGroundImage)

# Save the foregroung RGB content into a single object
foreground = cv2.merge((b,g,r))

# Save the alpha information into a single Mat
alpha = cv2.merge((a,a,a))

# Read background image
background = cv2.imread("backgroundAsset.png")

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255

# Perform alpha blending
foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outputImage = cv2.add(foreground, background)

cv2.imwrite("outImgPy.png", outputImage)

cv2.imshow("outImg", outputImage/255)
cv2.waitKey(0)