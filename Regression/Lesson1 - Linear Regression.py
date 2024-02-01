import numpy as np
import matplotlib.pyplot as plt

studyHours = np.array([2, 3, 4, 5, 6, 7, 8])
grades = np.array([21, 24, 27, 30, 33, 36, 39])
# Create plot for visual inspection
plt.scatter(studyHours, grades)
plt.xlabel('Study Hours')
plt.ylabel('Grades')
plt.title('Scatter plot of Grades vs Study Hours')
plt.savefig('Grades vs Hours.png')
# Get means
meanSH = sum(studyHours) / len(studyHours)
meanG = sum(grades) / len(grades)

# Calculate numerator and denominator
numerator = sum((x - meanSH) * (y - meanG) for x, y in zip(studyHours, grades))
denominator = (sum((x - meanSH)**2 for x in studyHours) *
               sum((y - meanG)**2 for y in grades)) ** 0.5
# Get correlation also known as Beta1
correlationCoeficient = numerator / denominator
# Get Beta0
beta0 = meanG - correlationCoeficient * meanSH
# Prediction
prediction = beta0 + correlationCoeficient * studyHours
# Residuals
residuals = grades - prediction
plt.scatter(prediction, residuals)
plt.xlabel('Predicted Grades')
plt.ylabel('Residuals')
plt.title('Scatter plot of Grades vs Residuals')
plt.savefig('Residuals.png')
# The residuals show that this is not a linear correlation despite the surface appeareances
