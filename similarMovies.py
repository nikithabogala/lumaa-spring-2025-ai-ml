import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

# Load the movie dataset from a CSV file.
def load_data(filepath):
    
    df = pd.read_csv(filepath)
    return df


# Combine the IMDb and Wikipedia plot summaries into a single text column.
def combine_plots(df, imdb_col='imdb_plot', wiki_col='wiki_plot'):
    df['Combined_Plot'] = df[imdb_col].fillna('') + " " + df[wiki_col].fillna('')
    return df

# Preprocess the dataset by ensuring no missing text in the chosen column.
def preprocess_data(df, text_column):
    
    df[text_column] = df[text_column].fillna('')
    return df

# Convert text documents to TF-IDF vectors.
def vectorize_text(corpus):
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return tfidf_matrix, vectorizer

# Recommend top N movies based on the similarity between the user query and the combined plot summaries.
def recommend(query, df, tfidf_matrix, vectorizer, text_column, top_n=5):
   
    # Transform the user query into the TF-IDF space
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[::-1][:top_n]
    return df.iloc[top_indices]['title'].tolist()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python recommend.py 'Your movie preferences here'")
        sys.exit(1)
    
    user_query = sys.argv[1]
    data_file = 'movies.csv'  # Path to the movie dataset file

    # Load the dataset and combine the plot summaries
    df = load_data(data_file)
    df = combine_plots(df, imdb_col='imdb_plot', wiki_col='wiki_plot')
    
    # Use the combined plots for further processing
    combined_col = 'Combined_Plot'
    df = preprocess_data(df, combined_col)
    
    # Create TF-IDF matrix for the combined plot summaries
    tfidf_matrix, vectorizer = vectorize_text(df[combined_col])
    
    # Get and print the top recommended movie titles
    recommended_titles = recommend(user_query, df, tfidf_matrix, vectorizer, combined_col, top_n=5)
    for title in recommended_titles:
        print(title)
