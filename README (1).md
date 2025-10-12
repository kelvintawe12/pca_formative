# PCA Assignment: Waste Management in Africa

Student: kelvin tawe 
GitHub Repo: https://github.com/kelvintawe12/pca_formative.git

This repository contains the implementation of Principal Component Analysis (PCA) on the What a Waste Global Dataset, filtered to African countries, focusing on waste management metrics (e.g., waste generation, % recycled, % landfilled).
## collab notebook
collab notebook : https://colab.research.google.com/drive/1BJjG9CXMUPYclMx9j8SVAwhyzLPkB1xP?usp=sharing

### Installation
1. Clone the repo: `
2. Install dependencies: `pip install numpy pandas matplotlib`
3. The PCA library is in `mypca.py`.

### Usage
Open pca_assignment_kelvin.ipynb in Google Colab or Jupyter Notebook.
The notebook loads the dataset from:https://drive.google.com/file/d/1ClsvVfGvk8fJLtd_ZmLDDnl5uBzF0j9D/view?usp=sharing


Run all cells to preprocess the data, apply PCA, visualize results, and optimize for large datasets.
Example PCA usage with the custom library (mypca.py):from mypca import MyPCA
import numpy as np
X = np.random.rand(100, 10)  # Sample data
pca = MyPCA()
pca.fit(X)
n_comp = pca.choose_n_components(threshold=0.95)
pca.n_components = n_comp  # Set number of components
X_transformed = pca.transform(X)
print("Selected components:", n_comp, "Transformed shape:", X_transformed.shape)


For the African waste management dataset, the notebook selects 63 components to retain 95% variance, resulting in a transformed shape of (69, 63).

Source: https://drive.google.com/file/d/1ClsvVfGvk8fJLtd_ZmLDDnl5uBzF0j9D/view?usp=sharing
mypca_backup: since files are cleared when runtime closes 

mypca_backup : 
 Download mypca.py from Google Drive
import requests

file_id = '1juT_sMsQw34NOYVUAmMs2oFAyH7uF4lf'
url = f'https://drive.google.com/uc?export=download&id={file_id}'
filename = 'mypca.py'

try:
    response = requests.get(url)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")
except requests.exceptions.RequestException as e:
    print(f"Error downloading {filename}: {e}")

from mypca import MyPCA


Description: Country-level waste management data for African countries (SSF and MEA regions), with 51 columns (41 numeric, e.g., 'gdp', waste percentages; 10 categorical, e.g., 'region_id', 'country_name'). Contains missing values and >10 columns after preprocessing.
Preprocessing: Mean imputation for numeric columns, mode imputation for categorical columns, one-hot encoding for categorical data.

#### Files

pca_assignment_kelvin.ipynb: Jupyter notebook with PCA implementation, preprocessing, visualizations, and optimization.
mypca.py: Custom PCA class using SVD.
