import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = data.target

# Arrange Data into Features Matrix and Target  Vector
feature_names = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)',
]