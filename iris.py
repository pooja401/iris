{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/pooja/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: Method .as_matrix will be removed in a future version. Use .values instead.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(150, 6)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "variable=pd.read_csv(\"Iris.csv\").as_matrix()\n",
    "variable.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import load_iris"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "var=load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'data': array([[5.1, 3.5, 1.4, 0.2],\n",
      "       [4.9, 3. , 1.4, 0.2],\n",
      "       [4.7, 3.2, 1.3, 0.2],\n",
      "       [4.6, 3.1, 1.5, 0.2],\n",
      "       [5. , 3.6, 1.4, 0.2],\n",
      "       [5.4, 3.9, 1.7, 0.4],\n",
      "       [4.6, 3.4, 1.4, 0.3],\n",
      "       [5. , 3.4, 1.5, 0.2],\n",
      "       [4.4, 2.9, 1.4, 0.2],\n",
      "       [4.9, 3.1, 1.5, 0.1],\n",
      "       [5.4, 3.7, 1.5, 0.2],\n",
      "       [4.8, 3.4, 1.6, 0.2],\n",
      "       [4.8, 3. , 1.4, 0.1],\n",
      "       [4.3, 3. , 1.1, 0.1],\n",
      "       [5.8, 4. , 1.2, 0.2],\n",
      "       [5.7, 4.4, 1.5, 0.4],\n",
      "       [5.4, 3.9, 1.3, 0.4],\n",
      "       [5.1, 3.5, 1.4, 0.3],\n",
      "       [5.7, 3.8, 1.7, 0.3],\n",
      "       [5.1, 3.8, 1.5, 0.3],\n",
      "       [5.4, 3.4, 1.7, 0.2],\n",
      "       [5.1, 3.7, 1.5, 0.4],\n",
      "       [4.6, 3.6, 1. , 0.2],\n",
      "       [5.1, 3.3, 1.7, 0.5],\n",
      "       [4.8, 3.4, 1.9, 0.2],\n",
      "       [5. , 3. , 1.6, 0.2],\n",
      "       [5. , 3.4, 1.6, 0.4],\n",
      "       [5.2, 3.5, 1.5, 0.2],\n",
      "       [5.2, 3.4, 1.4, 0.2],\n",
      "       [4.7, 3.2, 1.6, 0.2],\n",
      "       [4.8, 3.1, 1.6, 0.2],\n",
      "       [5.4, 3.4, 1.5, 0.4],\n",
      "       [5.2, 4.1, 1.5, 0.1],\n",
      "       [5.5, 4.2, 1.4, 0.2],\n",
      "       [4.9, 3.1, 1.5, 0.2],\n",
      "       [5. , 3.2, 1.2, 0.2],\n",
      "       [5.5, 3.5, 1.3, 0.2],\n",
      "       [4.9, 3.6, 1.4, 0.1],\n",
      "       [4.4, 3. , 1.3, 0.2],\n",
      "       [5.1, 3.4, 1.5, 0.2],\n",
      "       [5. , 3.5, 1.3, 0.3],\n",
      "       [4.5, 2.3, 1.3, 0.3],\n",
      "       [4.4, 3.2, 1.3, 0.2],\n",
      "       [5. , 3.5, 1.6, 0.6],\n",
      "       [5.1, 3.8, 1.9, 0.4],\n",
      "       [4.8, 3. , 1.4, 0.3],\n",
      "       [5.1, 3.8, 1.6, 0.2],\n",
      "       [4.6, 3.2, 1.4, 0.2],\n",
      "       [5.3, 3.7, 1.5, 0.2],\n",
      "       [5. , 3.3, 1.4, 0.2],\n",
      "       [7. , 3.2, 4.7, 1.4],\n",
      "       [6.4, 3.2, 4.5, 1.5],\n",
      "       [6.9, 3.1, 4.9, 1.5],\n",
      "       [5.5, 2.3, 4. , 1.3],\n",
      "       [6.5, 2.8, 4.6, 1.5],\n",
      "       [5.7, 2.8, 4.5, 1.3],\n",
      "       [6.3, 3.3, 4.7, 1.6],\n",
      "       [4.9, 2.4, 3.3, 1. ],\n",
      "       [6.6, 2.9, 4.6, 1.3],\n",
      "       [5.2, 2.7, 3.9, 1.4],\n",
      "       [5. , 2. , 3.5, 1. ],\n",
      "       [5.9, 3. , 4.2, 1.5],\n",
      "       [6. , 2.2, 4. , 1. ],\n",
      "       [6.1, 2.9, 4.7, 1.4],\n",
      "       [5.6, 2.9, 3.6, 1.3],\n",
      "       [6.7, 3.1, 4.4, 1.4],\n",
      "       [5.6, 3. , 4.5, 1.5],\n",
      "       [5.8, 2.7, 4.1, 1. ],\n",
      "       [6.2, 2.2, 4.5, 1.5],\n",
      "       [5.6, 2.5, 3.9, 1.1],\n",
      "       [5.9, 3.2, 4.8, 1.8],\n",
      "       [6.1, 2.8, 4. , 1.3],\n",
      "       [6.3, 2.5, 4.9, 1.5],\n",
      "       [6.1, 2.8, 4.7, 1.2],\n",
      "       [6.4, 2.9, 4.3, 1.3],\n",
      "       [6.6, 3. , 4.4, 1.4],\n",
      "       [6.8, 2.8, 4.8, 1.4],\n",
      "       [6.7, 3. , 5. , 1.7],\n",
      "       [6. , 2.9, 4.5, 1.5],\n",
      "       [5.7, 2.6, 3.5, 1. ],\n",
      "       [5.5, 2.4, 3.8, 1.1],\n",
      "       [5.5, 2.4, 3.7, 1. ],\n",
      "       [5.8, 2.7, 3.9, 1.2],\n",
      "       [6. , 2.7, 5.1, 1.6],\n",
      "       [5.4, 3. , 4.5, 1.5],\n",
      "       [6. , 3.4, 4.5, 1.6],\n",
      "       [6.7, 3.1, 4.7, 1.5],\n",
      "       [6.3, 2.3, 4.4, 1.3],\n",
      "       [5.6, 3. , 4.1, 1.3],\n",
      "       [5.5, 2.5, 4. , 1.3],\n",
      "       [5.5, 2.6, 4.4, 1.2],\n",
      "       [6.1, 3. , 4.6, 1.4],\n",
      "       [5.8, 2.6, 4. , 1.2],\n",
      "       [5. , 2.3, 3.3, 1. ],\n",
      "       [5.6, 2.7, 4.2, 1.3],\n",
      "       [5.7, 3. , 4.2, 1.2],\n",
      "       [5.7, 2.9, 4.2, 1.3],\n",
      "       [6.2, 2.9, 4.3, 1.3],\n",
      "       [5.1, 2.5, 3. , 1.1],\n",
      "       [5.7, 2.8, 4.1, 1.3],\n",
      "       [6.3, 3.3, 6. , 2.5],\n",
      "       [5.8, 2.7, 5.1, 1.9],\n",
      "       [7.1, 3. , 5.9, 2.1],\n",
      "       [6.3, 2.9, 5.6, 1.8],\n",
      "       [6.5, 3. , 5.8, 2.2],\n",
      "       [7.6, 3. , 6.6, 2.1],\n",
      "       [4.9, 2.5, 4.5, 1.7],\n",
      "       [7.3, 2.9, 6.3, 1.8],\n",
      "       [6.7, 2.5, 5.8, 1.8],\n",
      "       [7.2, 3.6, 6.1, 2.5],\n",
      "       [6.5, 3.2, 5.1, 2. ],\n",
      "       [6.4, 2.7, 5.3, 1.9],\n",
      "       [6.8, 3. , 5.5, 2.1],\n",
      "       [5.7, 2.5, 5. , 2. ],\n",
      "       [5.8, 2.8, 5.1, 2.4],\n",
      "       [6.4, 3.2, 5.3, 2.3],\n",
      "       [6.5, 3. , 5.5, 1.8],\n",
      "       [7.7, 3.8, 6.7, 2.2],\n",
      "       [7.7, 2.6, 6.9, 2.3],\n",
      "       [6. , 2.2, 5. , 1.5],\n",
      "       [6.9, 3.2, 5.7, 2.3],\n",
      "       [5.6, 2.8, 4.9, 2. ],\n",
      "       [7.7, 2.8, 6.7, 2. ],\n",
      "       [6.3, 2.7, 4.9, 1.8],\n",
      "       [6.7, 3.3, 5.7, 2.1],\n",
      "       [7.2, 3.2, 6. , 1.8],\n",
      "       [6.2, 2.8, 4.8, 1.8],\n",
      "       [6.1, 3. , 4.9, 1.8],\n",
      "       [6.4, 2.8, 5.6, 2.1],\n",
      "       [7.2, 3. , 5.8, 1.6],\n",
      "       [7.4, 2.8, 6.1, 1.9],\n",
      "       [7.9, 3.8, 6.4, 2. ],\n",
      "       [6.4, 2.8, 5.6, 2.2],\n",
      "       [6.3, 2.8, 5.1, 1.5],\n",
      "       [6.1, 2.6, 5.6, 1.4],\n",
      "       [7.7, 3. , 6.1, 2.3],\n",
      "       [6.3, 3.4, 5.6, 2.4],\n",
      "       [6.4, 3.1, 5.5, 1.8],\n",
      "       [6. , 3. , 4.8, 1.8],\n",
      "       [6.9, 3.1, 5.4, 2.1],\n",
      "       [6.7, 3.1, 5.6, 2.4],\n",
      "       [6.9, 3.1, 5.1, 2.3],\n",
      "       [5.8, 2.7, 5.1, 1.9],\n",
      "       [6.8, 3.2, 5.9, 2.3],\n",
      "       [6.7, 3.3, 5.7, 2.5],\n",
      "       [6.7, 3. , 5.2, 2.3],\n",
      "       [6.3, 2.5, 5. , 1.9],\n",
      "       [6.5, 3. , 5.2, 2. ],\n",
      "       [6.2, 3.4, 5.4, 2.3],\n",
      "       [5.9, 3. , 5.1, 1.8]]), 'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
      "       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
      "       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
      "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
      "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
      "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
      "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), 'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'), 'DESCR': '.. _iris_dataset:\\n\\nIris plants dataset\\n--------------------\\n\\n**Data Set Characteristics:**\\n\\n    :Number of Instances: 150 (50 in each of three classes)\\n    :Number of Attributes: 4 numeric, predictive attributes and the class\\n    :Attribute Information:\\n        - sepal length in cm\\n        - sepal width in cm\\n        - petal length in cm\\n        - petal width in cm\\n        - class:\\n                - Iris-Setosa\\n                - Iris-Versicolour\\n                - Iris-Virginica\\n                \\n    :Summary Statistics:\\n\\n    ============== ==== ==== ======= ===== ====================\\n                    Min  Max   Mean    SD   Class Correlation\\n    ============== ==== ==== ======= ===== ====================\\n    sepal length:   4.3  7.9   5.84   0.83    0.7826\\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\\n    ============== ==== ==== ======= ===== ====================\\n\\n    :Missing Attribute Values: None\\n    :Class Distribution: 33.3% for each of 3 classes.\\n    :Creator: R.A. Fisher\\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\\n    :Date: July, 1988\\n\\nThe famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\\nfrom Fisher\\'s paper. Note that it\\'s the same as in R, but not as in the UCI\\nMachine Learning Repository, which has two wrong data points.\\n\\nThis is perhaps the best known database to be found in the\\npattern recognition literature.  Fisher\\'s paper is a classic in the field and\\nis referenced frequently to this day.  (See Duda & Hart, for example.)  The\\ndata set contains 3 classes of 50 instances each, where each class refers to a\\ntype of iris plant.  One class is linearly separable from the other 2; the\\nlatter are NOT linearly separable from each other.\\n\\n.. topic:: References\\n\\n   - Fisher, R.A. \"The use of multiple measurements in taxonomic problems\"\\n     Annual Eugenics, 7, Part II, 179-188 (1936); also in \"Contributions to\\n     Mathematical Statistics\" (John Wiley, NY, 1950).\\n   - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\\n     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\\n   - Dasarathy, B.V. (1980) \"Nosing Around the Neighborhood: A New System\\n     Structure and Classification Rule for Recognition in Partially Exposed\\n     Environments\".  IEEE Transactions on Pattern Analysis and Machine\\n     Intelligence, Vol. PAMI-2, No. 1, 67-71.\\n   - Gates, G.W. (1972) \"The Reduced Nearest Neighbor Rule\".  IEEE Transactions\\n     on Information Theory, May 1972, 431-433.\\n   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al\"s AUTOCLASS II\\n     conceptual clustering system finds 3 classes in the data.\\n   - Many, many more ...', 'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], 'filename': '/home/pooja/anaconda3/lib/python3.7/site-packages/sklearn/datasets/data/iris.csv'}\n"
     ]
    }
   ],
   "source": [
    "print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ".. _iris_dataset:\n",
      "\n",
      "Iris plants dataset\n",
      "--------------------\n",
      "\n",
      "**Data Set Characteristics:**\n",
      "\n",
      "    :Number of Instances: 150 (50 in each of three classes)\n",
      "    :Number of Attributes: 4 numeric, predictive attributes and the class\n",
      "    :Attribute Information:\n",
      "        - sepal length in cm\n",
      "        - sepal width in cm\n",
      "        - petal length in cm\n",
      "        - petal width in cm\n",
      "        - class:\n",
      "                - Iris-Setosa\n",
      "                - Iris-Versicolour\n",
      "                - Iris-Virginica\n",
      "                \n",
      "    :Summary Statistics:\n",
      "\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "                    Min  Max   Mean    SD   Class Correlation\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "    sepal length:   4.3  7.9   5.84   0.83    0.7826\n",
      "    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n",
      "    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n",
      "    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "\n",
      "    :Missing Attribute Values: None\n",
      "    :Class Distribution: 33.3% for each of 3 classes.\n",
      "    :Creator: R.A. Fisher\n",
      "    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n",
      "    :Date: July, 1988\n",
      "\n",
      "The famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\n",
      "from Fisher's paper. Note that it's the same as in R, but not as in the UCI\n",
      "Machine Learning Repository, which has two wrong data points.\n",
      "\n",
      "This is perhaps the best known database to be found in the\n",
      "pattern recognition literature.  Fisher's paper is a classic in the field and\n",
      "is referenced frequently to this day.  (See Duda & Hart, for example.)  The\n",
      "data set contains 3 classes of 50 instances each, where each class refers to a\n",
      "type of iris plant.  One class is linearly separable from the other 2; the\n",
      "latter are NOT linearly separable from each other.\n",
      "\n",
      ".. topic:: References\n",
      "\n",
      "   - Fisher, R.A. \"The use of multiple measurements in taxonomic problems\"\n",
      "     Annual Eugenics, 7, Part II, 179-188 (1936); also in \"Contributions to\n",
      "     Mathematical Statistics\" (John Wiley, NY, 1950).\n",
      "   - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\n",
      "     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\n",
      "   - Dasarathy, B.V. (1980) \"Nosing Around the Neighborhood: A New System\n",
      "     Structure and Classification Rule for Recognition in Partially Exposed\n",
      "     Environments\".  IEEE Transactions on Pattern Analysis and Machine\n",
      "     Intelligence, Vol. PAMI-2, No. 1, 67-71.\n",
      "   - Gates, G.W. (1972) \"The Reduced Nearest Neighbor Rule\".  IEEE Transactions\n",
      "     on Information Theory, May 1972, 431-433.\n",
      "   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al\"s AUTOCLASS II\n",
      "     conceptual clustering system finds 3 classes in the data.\n",
      "   - Many, many more ...\n"
     ]
    }
   ],
   "source": [
    "print(var.DESCR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.utils import shuffle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=var.data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "y=var.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.1 3.5 1.4 0.2]\n",
      " [4.9 3.  1.4 0.2]\n",
      " [4.7 3.2 1.3 0.2]\n",
      " [4.6 3.1 1.5 0.2]\n",
      " [5.  3.6 1.4 0.2]\n",
      " [5.4 3.9 1.7 0.4]\n",
      " [4.6 3.4 1.4 0.3]\n",
      " [5.  3.4 1.5 0.2]\n",
      " [4.4 2.9 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [5.4 3.7 1.5 0.2]\n",
      " [4.8 3.4 1.6 0.2]\n",
      " [4.8 3.  1.4 0.1]\n",
      " [4.3 3.  1.1 0.1]\n",
      " [5.8 4.  1.2 0.2]\n",
      " [5.7 4.4 1.5 0.4]\n",
      " [5.4 3.9 1.3 0.4]\n",
      " [5.1 3.5 1.4 0.3]\n",
      " [5.7 3.8 1.7 0.3]\n",
      " [5.1 3.8 1.5 0.3]\n",
      " [5.4 3.4 1.7 0.2]\n",
      " [5.1 3.7 1.5 0.4]\n",
      " [4.6 3.6 1.  0.2]\n",
      " [5.1 3.3 1.7 0.5]\n",
      " [4.8 3.4 1.9 0.2]\n",
      " [5.  3.  1.6 0.2]\n",
      " [5.  3.4 1.6 0.4]\n",
      " [5.2 3.5 1.5 0.2]\n",
      " [5.2 3.4 1.4 0.2]\n",
      " [4.7 3.2 1.6 0.2]\n",
      " [4.8 3.1 1.6 0.2]\n",
      " [5.4 3.4 1.5 0.4]\n",
      " [5.2 4.1 1.5 0.1]\n",
      " [5.5 4.2 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.2]\n",
      " [5.  3.2 1.2 0.2]\n",
      " [5.5 3.5 1.3 0.2]\n",
      " [4.9 3.6 1.4 0.1]\n",
      " [4.4 3.  1.3 0.2]\n",
      " [5.1 3.4 1.5 0.2]\n",
      " [5.  3.5 1.3 0.3]\n",
      " [4.5 2.3 1.3 0.3]\n",
      " [4.4 3.2 1.3 0.2]\n",
      " [5.  3.5 1.6 0.6]\n",
      " [5.1 3.8 1.9 0.4]\n",
      " [4.8 3.  1.4 0.3]\n",
      " [5.1 3.8 1.6 0.2]\n",
      " [4.6 3.2 1.4 0.2]\n",
      " [5.3 3.7 1.5 0.2]\n",
      " [5.  3.3 1.4 0.2]\n",
      " [7.  3.2 4.7 1.4]\n",
      " [6.4 3.2 4.5 1.5]\n",
      " [6.9 3.1 4.9 1.5]\n",
      " [5.5 2.3 4.  1.3]\n",
      " [6.5 2.8 4.6 1.5]\n",
      " [5.7 2.8 4.5 1.3]\n",
      " [6.3 3.3 4.7 1.6]\n",
      " [4.9 2.4 3.3 1. ]\n",
      " [6.6 2.9 4.6 1.3]\n",
      " [5.2 2.7 3.9 1.4]\n",
      " [5.  2.  3.5 1. ]\n",
      " [5.9 3.  4.2 1.5]\n",
      " [6.  2.2 4.  1. ]\n",
      " [6.1 2.9 4.7 1.4]\n",
      " [5.6 2.9 3.6 1.3]\n",
      " [6.7 3.1 4.4 1.4]\n",
      " [5.6 3.  4.5 1.5]\n",
      " [5.8 2.7 4.1 1. ]\n",
      " [6.2 2.2 4.5 1.5]\n",
      " [5.6 2.5 3.9 1.1]\n",
      " [5.9 3.2 4.8 1.8]\n",
      " [6.1 2.8 4.  1.3]\n",
      " [6.3 2.5 4.9 1.5]\n",
      " [6.1 2.8 4.7 1.2]\n",
      " [6.4 2.9 4.3 1.3]\n",
      " [6.6 3.  4.4 1.4]\n",
      " [6.8 2.8 4.8 1.4]\n",
      " [6.7 3.  5.  1.7]\n",
      " [6.  2.9 4.5 1.5]\n",
      " [5.7 2.6 3.5 1. ]\n",
      " [5.5 2.4 3.8 1.1]\n",
      " [5.5 2.4 3.7 1. ]\n",
      " [5.8 2.7 3.9 1.2]\n",
      " [6.  2.7 5.1 1.6]\n",
      " [5.4 3.  4.5 1.5]\n",
      " [6.  3.4 4.5 1.6]\n",
      " [6.7 3.1 4.7 1.5]\n",
      " [6.3 2.3 4.4 1.3]\n",
      " [5.6 3.  4.1 1.3]\n",
      " [5.5 2.5 4.  1.3]\n",
      " [5.5 2.6 4.4 1.2]\n",
      " [6.1 3.  4.6 1.4]\n",
      " [5.8 2.6 4.  1.2]\n",
      " [5.  2.3 3.3 1. ]\n",
      " [5.6 2.7 4.2 1.3]\n",
      " [5.7 3.  4.2 1.2]\n",
      " [5.7 2.9 4.2 1.3]\n",
      " [6.2 2.9 4.3 1.3]\n",
      " [5.1 2.5 3.  1.1]\n",
      " [5.7 2.8 4.1 1.3]\n",
      " [6.3 3.3 6.  2.5]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [7.1 3.  5.9 2.1]\n",
      " [6.3 2.9 5.6 1.8]\n",
      " [6.5 3.  5.8 2.2]\n",
      " [7.6 3.  6.6 2.1]\n",
      " [4.9 2.5 4.5 1.7]\n",
      " [7.3 2.9 6.3 1.8]\n",
      " [6.7 2.5 5.8 1.8]\n",
      " [7.2 3.6 6.1 2.5]\n",
      " [6.5 3.2 5.1 2. ]\n",
      " [6.4 2.7 5.3 1.9]\n",
      " [6.8 3.  5.5 2.1]\n",
      " [5.7 2.5 5.  2. ]\n",
      " [5.8 2.8 5.1 2.4]\n",
      " [6.4 3.2 5.3 2.3]\n",
      " [6.5 3.  5.5 1.8]\n",
      " [7.7 3.8 6.7 2.2]\n",
      " [7.7 2.6 6.9 2.3]\n",
      " [6.  2.2 5.  1.5]\n",
      " [6.9 3.2 5.7 2.3]\n",
      " [5.6 2.8 4.9 2. ]\n",
      " [7.7 2.8 6.7 2. ]\n",
      " [6.3 2.7 4.9 1.8]\n",
      " [6.7 3.3 5.7 2.1]\n",
      " [7.2 3.2 6.  1.8]\n",
      " [6.2 2.8 4.8 1.8]\n",
      " [6.1 3.  4.9 1.8]\n",
      " [6.4 2.8 5.6 2.1]\n",
      " [7.2 3.  5.8 1.6]\n",
      " [7.4 2.8 6.1 1.9]\n",
      " [7.9 3.8 6.4 2. ]\n",
      " [6.4 2.8 5.6 2.2]\n",
      " [6.3 2.8 5.1 1.5]\n",
      " [6.1 2.6 5.6 1.4]\n",
      " [7.7 3.  6.1 2.3]\n",
      " [6.3 3.4 5.6 2.4]\n",
      " [6.4 3.1 5.5 1.8]\n",
      " [6.  3.  4.8 1.8]\n",
      " [6.9 3.1 5.4 2.1]\n",
      " [6.7 3.1 5.6 2.4]\n",
      " [6.9 3.1 5.1 2.3]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [6.8 3.2 5.9 2.3]\n",
      " [6.7 3.3 5.7 2.5]\n",
      " [6.7 3.  5.2 2.3]\n",
      " [6.3 2.5 5.  1.9]\n",
      " [6.5 3.  5.2 2. ]\n",
      " [6.2 3.4 5.4 2.3]\n",
      " [5.9 3.  5.1 1.8]]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
      " 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2]\n"
     ]
    }
   ],
   "source": [
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "X,Y= shuffle(x,y,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0\n",
      " 1 1 1 2 0 2 0 0 1 2 2 2 2 1 2 1 1 2 2 2 2 1 2 1 0 2 1 1 1 1 2 0 0 2 1 0 0\n",
      " 1 0 2 1 0 1 2 1 0 2 2 2 2 0 0 2 2 0 2 0 2 2 0 0 2 0 0 0 1 2 2 0 0 0 1 1 0\n",
      " 0 1 0 2 1 2 1 0 2 0 2 0 0 2 0 2 1 1 1 2 2 1 1 0 1 2 2 0 1 1 1 1 0 0 0 2 1\n",
      " 2 0]\n"
     ]
    }
   ],
   "source": [
    "print(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.3,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(45, 4)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xtest.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "lr=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/pooja/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "/home/pooja/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:460: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
       "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
       "          tol=0.0001, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lr.fit(xtrain,ytrain)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "ypred=lr.predict(xtest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "acc=accuracy_score(ytest,ypred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9555555555555556\n"
     ]
    }
   ],
   "source": [
    "print(acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
