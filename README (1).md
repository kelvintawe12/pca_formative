# PCA Assignment: Waste Management in Africa
Peer Pair Number: [Your_Pair_Number]  
Student: [Your_Name]  
GitHub Repo: https://github.com/[Your_GitHub_Username]/pca-waste-assignment

This repository contains the implementation of Principal Component Analysis (PCA) on the What a Waste Global Dataset, filtered to African countries, focusing on waste management metrics (e.g., waste generation, % recycled, % landfilled).

## Installation
1. Clone the repo: `git clone https://github.com/[Your_GitHub_Username]/pca-waste-assignment`
2. Install dependencies: `pip install numpy pandas matplotlib`
3. The PCA library is in `mypca.py`.

## Usage
- Run `pca_assignment_kelvin.ipynb` in Google Colab or Jupyter.
- The notebook uses a locally loaded dataset (e.g., country_level_data_0.csv).
- Example PCA usage with the custom library:
```python
from mypca import MyPCA
import numpy as np
X = np.random.rand(100, 10)  # Sample data
pca = MyPCA()
pca.fit(X)
n_comp = pca.choose_n_components(threshold=0.95)
X_transformed = pca.transform(X)
print("Selected components:", n_comp, "Transformed shape:", X_transformed.shape)
