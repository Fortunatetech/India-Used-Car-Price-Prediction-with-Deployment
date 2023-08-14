import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from six.moves import urllib

download_dir = "./data/"

download_url = "https://raw.githubusercontent.com/aravind9722/datasets-for-ML-projects/main/cardekho_dataset.csv"

os.makedirs(download_dir,exist_ok=True)

filename = os.path.basename(download_url)

download_file_path = os.path.join(download_dir, filename)

urllib.request.urlretrieve(download_url, download_file_path)

df = pd.read_csv(download_file_path, index_col=[0])

def show_explore_page():
    plt.subplots(figsize=(14, 7))
    sns.histplot(df.selling_price, bins=200, kde=True, color='b')
    plt.title("Selling Price Distribution", weight="bold", fontsize=20, pad=20)
    plt.ylabel("Count", weight="bold", fontsize=12)
    plt.xlabel("Selling price in millions", weight="bold", fontsize=12)
    plt.xlim(0, 3000000)
    plt.show()

    plt.subplots(figsize=(14, 7))
    sns.countplot(x="car_name", data=df, ec="black", palette="Set1", order=df['car_name'].value_counts().index)
    plt.title("Top 10 Most Sold Car", weight="bold", fontsize=20, pad=20)
    plt.ylabel("Count", weight="bold", fontsize=20)
    plt.xlabel("Car Name", weight="bold", fontsize=16)
    plt.xticks(rotation=45)
    plt.xlim(-1, 10.5)
    plt.show()