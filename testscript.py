#!/usr/bin/env python

"""
Program  : testscript.py
Language : python
Date     : 2024-02-09
Author   : Darrin T. Schultz
Email    : darrin.schultz@univie.ac.at
Github   : https://github.com/conchoecia/ncbigenomes
Support  : For issues or questions, please search if the topic has been discussed already
           on github and open a new issue if not: https://github.com/conchoecia/odp/issues
License  : GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007. See the LICENSE file.
Citation : There is currently no citation for this script.

Description:
  - This program is to test github actions. and its ability to dynamically plot data.

Usage instructions:
  - None currently.
"""

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def main():
    # Load iris dataset from scikit-learn
    iris = load_iris()
    colnames = ["sepal_length", "sepal_width",
               "petal_length", "petal_width"]
    iris_df = pd.DataFrame(data=iris.data,
                           columns=colnames)
    print(iris_df)

    # Plotting
    plt.figure(figsize=(8, 6))

    # Scatter plot of sepal length vs sepal width
    plt.scatter(iris_df['sepal_length'], iris_df['sepal_width'], c='blue', label='Sepal')

    # Scatter plot of petal length vs petal width
    plt.scatter(iris_df['petal_length'], iris_df['petal_width'], c='red', label='Petal')

    plt.xlabel('Length')
    plt.ylabel('Width')
    plt.title('Iris Dataset')
    plt.legend()
    plt.grid(True)

    # Save plot as a PDF file
    plt.savefig('iris_plot.pdf')

    # Close the plot to free memory (optional)
    plt.close()


if __name__ == "__main__":
    main()