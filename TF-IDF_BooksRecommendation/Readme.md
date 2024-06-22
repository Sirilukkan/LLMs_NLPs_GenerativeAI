# TF-IDF Book Recommendation System

This project aims to build a book recommendation system using Term Frequency-Inverse Document Frequency (TF-IDF) and cosine similarity. The system recommends books based on the content similarity of book descriptions.

## Goals

The primary goal of this project is to create a recommendation engine that suggests books to users based on the content of books they have liked or shown interest in. This is achieved using TF-IDF to vectorize book descriptions and cosine similarity to find books with similar content.

## Data

The dataset used in this project is the Book Recommendation Dataset from Kaggle. The dataset includes three CSV files:

- `Books.csv`: Contains information about books.
- `Ratings.csv`: Contains user ratings for books.
- `Users.csv`: Contains information about users.

### Data Preparation

1. **Data Loading**:
    - Load the `Books.csv`, `Ratings.csv`, and `Users.csv` files into Pandas DataFrames.
    - Merge these DataFrames to create a consolidated dataset.

2. **Data Cleaning**:
    - Remove duplicates and handle incorrect data entries.
    - Clean specific columns to ensure data integrity.

3. **Feature Engineering**:
    - Combine relevant text features to create a single text feature for TF-IDF vectorization.

## Methodology

1. **TF-IDF Vectorization**:
    - Use `TfidfVectorizer` from scikit-learn to convert the text data into TF-IDF feature vectors.
    - This step transforms the textual data into a numerical format that can be used to compute similarities.

2. **Cosine Similarity**:
    - Calculate the cosine similarity between the TF-IDF vectors to measure the content similarity between books.
    - Higher cosine similarity values indicate greater similarity between book descriptions.

3. **Recommendation Generation**:
    - For a given book, find the top N books with the highest cosine similarity scores.
    - Exclude the book itself from the recommendation list.

## Analysis

- **Exploratory Data Analysis (EDA)**:
    - Examine the structure and content of the data.
    - Visualize the distribution of ratings and other relevant features.
  
- **Model Evaluation**:
    - Test the recommendation system by providing sample book titles and evaluating the relevance of the recommended books.

## How to Use

### Prerequisites

- Python 3.10.12
- Required libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the dataset**:
    - Set up Kaggle API to download the dataset.
    - Place the `kaggle.json` file in the appropriate directory and run the following commands:
    ```bash
    mkdir ~/.kaggle
    cp kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    kaggle datasets download arashnic/book-recommendation-dataset
    unzip book-recommendation-dataset
    ```

4. **Run the notebook**:
    - Open and run the Jupyter notebook `TF_IDF_book_recommendation.ipynb` to generate book recommendations.

### Example

To get book recommendations, use the `recommend_book` function:

```python
recommendations = recommend_book("classical mythology")
print("Recommendations for classical mythology:")
print(recommendations)
```

## Conclusion

This project demonstrates how to build a simple yet effective book recommendation system using TF-IDF and cosine similarity. The approach can be extended to include more sophisticated techniques for improved recommendations.
