import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


"""
- Description: Function to load TSV file from path as a dataframe
- Input:
	tsv_filepath: TSV filepath to the data
- Output: Pandas dataframe object
- Note: Input filepath is a tab-delimited TSV file; Index column
	must also be specified when loading the data
"""

def load_dataframe(tsv_filepath):
	# ** FILL ME **
	pass



"""
- Description: Function to initialize K-Nearest Neighbors Classifier model
- Input:
	K: the number of nearest neighbors the model should use
- Output:
	model: the scikit-learn K-Nearest Neighbors Classifier model object
- Note:
	- Please refer to https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
	- The only parameter you should be using to initialize the model is "n_neighbors"
"""
def initialize_knn_model(K):
	# ** FILL ME **
	pass


"""
- Description: Function used to quantify the fraction of
	incorrect cell type predictions given a numpy vector
	of ground truths and the predictions
- Input:
	Y: Numpy vector of true cell types
	Y_hat: Numpy vector of predicted cell types
- Output: fraction of incorrect predictions
"""
def compute_fraction_incorrect_predictions(Y,Y_hat):
	# ** FILL ME **
	pass


"""
- Description: Function used to visualize cell type labels
	of the input data
- Input:
	X: expression dataset
	Y: Numpy array object of cell type labels; [num_cells] 
	title: Title of the plot
- Output:
	None
"""
def viz_cell_type_labels(X, Y, title, xlabel = "Gene 1", ylabel = 'Gene 2'):
	
	# convert X and Y to numpy arrays if they were not already
	X = np.array(X)
	Y = np.array(Y)
	
	# make sure Y is a vector
	if len(np.array(Y).shape) == 2: 
		Y = Y[:,0]
	
	# make plot
	plt.clf()
	plt.scatter(X[:,0], X[:,1], c = Y, s = 1)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show() 
	 


def main():


	# --- INPUT VARIABLES TO FIT AND EVALUATE THE MODEL ---

	# ** data paths **
	X_path = "classification_X.tsv"
	Y_path = "classification_Y.tsv"

	# ** train fraction to use **
	train_fraction = 0.8

	# ** K number of neighbors value to use **
	K = 2

	# ** load the data **
	X_df = load_dataframe(X_path)
	Y_df = load_dataframe(Y_path)


	# --- CONVERT DATAFRAMES TO NUMPY ARRAYS THAT ARE APPROPRIATELY SHAPED ---

	# ** convert X_df dataframe to a numpy array **
	X = np.array(X_df) # [num_cells x num_genes] matrix

	# ** convert Y_df dataframe to a numpy array; reshape to be a vector instead of a matrix **
	Y = np.array(Y_df) # [num_cells x 1] matrix
	Y = Y[:,0] # [num_cells] vector



	# --- SPLIT THE DATA INTO A TRAINING AND TESTING DATASET ACCORDING TO THE PROPORTION SPECIFIED BY train_fraction ---
	# Please refer to https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

	# ** UNCOMMENT AND FILL ME **
	# X_train, X_test, Y_train, Y_test = 


	# --- INITIALIZE THE K-NEAREST NEIGHBORS MODEL ---
	model = initialize_knn_model(K)


	# --- FIT MODEL TO THE TRAINING DATA ---

	# ** FILL ME **


	# --- GET THE PREDICTIONS ON THE TRAINING AND TESTING SET ---

	# ** UNCOMMENT AND FILL ME **

	# Y_train_hat =
	# Y_test_hat =



	# --- COMPUTE THE MODEL PREDICTION ERROR ON TRAIN AND THE TEST SET ----
	train_error = compute_fraction_incorrect_predictions(Y_train, Y_train_hat)
	test_error = compute_fraction_incorrect_predictions(Y_test, Y_test_hat)

	print("Training loss: %s" % str(float(train_loss)))
	print("Testing loss: %s" % str(float(test_loss)))


	# --- VISUALIZE HOW PREDICTIONS COMPARE TO THE TRUTH ---

	# ** ground truth cell type labels **
	viz_cell_type_labels(X, Y, title = "True cell type labels")

	# ** viz train set predictions **
	viz_cell_type_labels(X = X_train, Y = Y_train_hat, title = "Train set cell type predictions")
	    
	# ** viz test set predictions **
	viz_cell_type_labels(X = X_test, Y = Y_test_hat, title = "Test set cell type predictions")
	    




if __name__ == "__main__":
	main()









