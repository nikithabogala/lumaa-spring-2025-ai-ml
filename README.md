# Content-Based Movie Recommendation System

## Overview
This project implements a simple content-based recommendation system that suggests movies based on a short text description of user preferences. The system combines IMDb and Wikipedia plot summaries, transforms the combined text into TF-IDF vectors, and uses cosine similarity to find the most similar movies.

---

## Dataset
- **Source:** (https://github.com/Nazareno95/Find-Movie-Similarity-from-Plot-Summaries)
- **Details:** The dataset contains the top 100 movies with plot summaries from IMDb and Wikipedia.
- **Loading:** Download the dataset. Ensure the main folder contains the `movies.csv` file.

---

## Demo

Video link:
 https://drive.google.com/file/d/1P0HxXriIA7KW9r3m3z7w4NGn91cddlPZ/view?usp=sharing

## Setup
- **Python Version:** 3.8 or higher.
- **Virtual Environment:**  
  Create and activate a virtual environment with:
  ```bash
  python -m venv lumaa
  source lumaa/bin/activate  
  ```
---
  ## Dependencies

  ```bash
  pip install -r requirements.txt
  ```

  ## Running the Code

  ```bash
  python similarMovies.py "YOUR_SHORT_CONTEXT_FOR_INTERESTED_MOVIES"
  ```

  ## Results

 For example,  given the input

  ```csharp
  I love thrilling action movies set in space, with a comedic twist.
  ```

  Output is

  ```mathematica
   2001: A Space Odyssey
   Pulp Fiction
   Star Wars
   The African Queen
   Sunset Blvd.
  ```

## Salary Expectations

   **3000$ - 5000$** 