import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# set random seed
np.random.seed(31415)




"""
- Description: Function to load TSV file from path as a dataframe
- Input:
	tsv_filepath: TSV filepath to the data
- Output: Pandas dataframe object
- Note: Input filepath is a tab-delimited TSV file; Index column
	must also be specified when loading the data
"""

def load_dataframe(tsv_filepath):
	return pd.read_table(tsv_filepath, sep = '\t', index_col = 'cell_id')




"""
- Description: Function to initialize K-Nearest Neighbors Classifier model
- Input:
	K: the number of nearest neighbors the model should use
- Output:
	model: the scikit-learn K-Nearest Neighbors Classifier model object
"""
def initialize_knn_model(K):
	# ** define parameters to use to fit model **
	model_params = {
	    "n_neighbors" : K
	}

	# ** initialize model according to the parameters **
	model = KNeighborsClassifier(**model_params)

	return model




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
    # ** compute whether prediction was correct or not; 0 if correct, 1 if incorrect **
    incorrect_preds = np.abs(Y - Y_hat)
    
    # ** compute the fraction of predictions that were incorrect**
    fraction_incorrect = np.mean(incorrect_preds)
    
    return fraction_incorrect



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

	# ** K value to use **
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
	from sklearn.model_selection import train_test_split
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = train_fraction)


	# --- INITIALIZE THE K-NEAREST NEIGHBORS MODEL ---
	model = initialize_knn_model(K)


	# --- FIT MODEL TO THE TRAINING DATA ---
	model.fit(X_train,Y_train)


	# --- GET THE PREDICTIONS ON THE TRAINING AND TESTING SET ---
	Y_train_hat = model.predict(X_train)
	Y_test_hat = model.predict(X_test)



	# --- COMPUTE THE MODEL PREDICTION ERROR ON TRAIN AND THE TEST SET ----
	train_error = compute_fraction_incorrect_predictions(Y_train, Y_train_hat)
	test_error = compute_fraction_incorrect_predictions(Y_test, Y_test_hat)

	print("Training loss: %s" % str(float(train_error)))
	print("Testing loss: %s" % str(float(test_error)))


	# --- VISUALIZE HOW PREDICTIONS COMPARE TO THE TRUTH ---

	# ** ground truth cell type labels **
	viz_cell_type_labels(X, Y, title = "True cell type labels")

	# ** viz train set predictions **
	viz_cell_type_labels(X = X_train, Y = Y_train_hat, title = "Train set cell type predictions (error: %s)" % train_error)
	    
	# ** viz test set predictions **
	viz_cell_type_labels(X = X_test, Y = Y_test_hat, title = "Test set cell type predictions (error: %s)" % test_error)
	    




if __name__ == "__main__":
	main()









