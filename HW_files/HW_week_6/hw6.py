import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import scipy

# set random seed
np.random.seed(31415)





"""
- Description: Fit KMeans clustering algorithm to data X
given specified number of clustesr k
- Input:
	X: Numpy data matrix
	k: Integer; Number of clusters to find using KMeans
- Output: KMeans scikit-learn object
- Note:
	- For information on how to fit the object, and the methods / variables available to you,
	please view: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans
	- The only variable you should set when initializing the object is "n_clusters" (what we've
	been calling K) -- please leave the other parameters to their default values
"""

def fit_kmeans(X, k):
	pass




"""
- Description: Given a vector of variance explained per principal component,
	computes the cumulative variance explained by each principal component
		Example:
			Given an input numpy vector with the following entires: [0.4, 0.3, 0.2, 0.1],
			the function should return: [0.4, 0.7, 0.9, 1.0] 
- Input:
	fraction_variance_explained: Numpy vector, where entries are the fraction
	of  variance explained by each principle component
- Output:
	Numpy vector of the same length as fraction_variance_explained, where
	entries are the cumulative variance explained

"""
def compute_cumulative_variance_explained(fraction_variance_explained):
	pass



"""
- Description: Given a vector of the cumulative variance explained per principal component
	and a threshold fraction of variation that we want our principle components to
	explain, return the number of top principle components to keep
- Input:
	cumulative_variance_explained: Numpy vector, where entries are the cumulative fraction
	of  variance explained by each principle component
	threshold_fraction: Float in range [0,1]; Fraction of variance we want the 
	top principle componetns to explain
- Output:
	An integer, corresponding to the number of principle components
	that explain at least threshold_fraction of the total data variance

"""
def get_num_top_pcs_required(cumulative_variance_explained, threshold_fraction):
	pass



"""
- Description: Transform the data into principal components, and
	limit features to specified number of top principle components
- Input:
	pca: scikit-learn PCA object
	X: input data matrix
	num_top_pcs: number of top principle components to restrict the
	data to after transformed original data into principle component space
- Output:
	Numpy matrix with the same number of rows as X, and as many columns as num_top_pcs 

"""
def transform_and_keep_num_pcs(pca, X, num_top_pcs):
	pass



def main():


	# --- INPUT VARIABLES TO FIT AND EVALUATE THE MODEL ---

	# ** data paths **
	X_path = "X.npz"

	# ** K number of neighbors value to use **
	k_range = [2,3,4,5,6,7]

	# pca variance explained fraction
	pca_variance_explained_threshold = 0.8


	# --- LOAD THE DATA AS A NUMPY MATRIX ---

	# ** load as a sparse matrix **
	X_sparse = scipy.sparse.load_npz(X_path)

	# ** convert sparse matrix object to numpy array **
	X = np.array(X_sparse.todense())



	# --- INITIALIZE PCA MODEL ---

	# ** FillMe **
	# pca = ...

	# --- FIT PCA MODEL ON THE DATASET ---
	
	# ** FillMe **


	# --- COMPUTE THE CUMULATIVE VARIANCE EXPLAINED BY THE TOP PRINCIPLE COMPONENTS ----
	cumulative_variance_explained = compute_cumulative_variance_explained(pca.explained_variance_ratio_)


	# --- FIGURE OUT THE NUMBER OF PRINCIPLE COMPONENTS NEEDED TO SUMMARIZE 80% OF THE DATA VARIANCE ---
	num_top_pcs_required = get_num_top_pcs_required(cumulative_variance_explained, pca_variance_explained_threshold)


	# --- TRANSFORM THE DATA INTO PRINCIPLE COMPONENT SPACE AND KEEP ONLY THE TOP PC'S SUMMARIZING 80% OF THE DATA VARIANCE ---
	X_transformed = transform_and_keep_num_pcs(pca, X, num_top_pcs_required)


	# --- RUN K MEANS CLUSTERING ON THE TRANSFORMED DATA FOR EACH VALUE OF K AND STORE THE OBJECT ---
	kmeans_objects = []
	for k in k_range:
		kmeans_objects.append(fit_kmeans(X_transformed,k))



	# --- FOR EACH FIT OF KMEANS, GET PREDICTED CLUSTER LABELS AND THE SCORES ---

	# ** get labels **
	kmeans_labels = []
	for kmeans_obj in kmeans_objects:
		kmeans_labels.append(kmeans_obj.labels_)

	# ** get their respective scores **
	kmeans_scores = []
	for kmeans_obj in kmeans_objects:
		kmeans_scores.append(kmeans_obj.score(X_transformed))



	# --- VISUALIZE VARIANCE EXPLAINED BY TOP PC's ---

	plt.clf()
	plt.scatter(np.arange(0,cumulative_variance_explained.size) + 1,cumulative_variance_explained,s=4)
	plt.xlabel("Number of top principle components")
	plt.ylabel("Cumulative variance explained")
	plt.axhline(y = 0.8, c = 'r')
	plt.title("Variance explained by the number of top principle components")
	plt.show()




	# --- VISUALIZE THE SCORES FOR DIFFERENT VALUES OF K FOR K-MEANS ---

	plt.clf()
	plt.scatter(k_range, kmeans_scores)
	plt.xlabel("K value")
	plt.ylabel("Score (higher is better)")
	plt.title("K means scores for differing values of K")
	plt.show()




	# --- VISUALIZE THE CLUSTER ASSIGNMENTS IN 2 DIMENSIONS ---

	# ** transform to 2D **
	X_transformed_2d = transform_and_keep_num_pcs(pca, X, 2)


	for i, k in enumerate(k_range):
		
		plt.clf()
		plt.scatter(X_transformed_2d[:,0], X_transformed_2d[:,1], c = kmeans_labels[i])
		plt.xlabel("Principle Component 1")
		plt.ylabel("Principle Component 2")
		plt.title("Cells colored by cluster (k = %s)" % k)
		plt.show()







if __name__ == "__main__":
	main()









