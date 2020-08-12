To set up the conda environment needed for HW6, please run the following:
	conda env create -f hw6_env.yml

To activate the environment, run
	conda activate hw6

If creating the environment above fails, please try the following:
	sh create_and_activate_hw6_env.sh
Note: this command will activate the installed environment


Using the python script in hw6.py, this homework walks through applying an unsupervised dimensionality a dimensionality reduction algorithm, PCA, to your data using scikit-learn. Using the dimensionality reduced representation of your data, you will then fit an unsupervised clustering model using scikit-learn. We will be using the K-Means Clustering algorithm for this task (https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html). Please fill in any sections marked "FillMe". For an example of how to run PCA and KMeans, please view the example notebooks from the lecture, pca_example.html and kmeans_example.html.


