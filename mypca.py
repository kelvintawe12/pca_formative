import numpy as np

class MyPCA:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.eig_vals = None
        self.eig_vecs = None
        self.explained_variance_ratio_ = None

    def fit(self, X):
        U, S, Vh = np.linalg.svd(X, full_matrices=False)
        self.eig_vals = S**2 / (X.shape[0] - 1)
        self.eig_vecs = Vh.T
        self.explained_variance_ratio_ = self.eig_vals / np.sum(self.eig_vals)

    def transform(self, X):
        if self.n_components is None:
            k = len(self.eig_vals)
        else:
            k = self.n_components
        return np.dot(X, self.eig_vecs[:, :k])

    def choose_n_components(self, threshold=0.95):
        if self.explained_variance_ratio_ is None:
            raise ValueError("Fit the model first.")
        cum_var = np.cumsum(self.explained_variance_ratio_)
        return np.argmax(cum_var >= threshold) + 1
