# NLP Fundamentals – Text to Numerical Representation

This repository demonstrates how Natural Language Processing (NLP) techniques convert raw text into machine-understandable numerical features for analysis and modeling.

## Text Data Representation
Raw textual data must be transformed into numeric form because machine learning models operate on numbers, not words.

## Bag of Words (BoW)
Bag of Words represents text by counting how many times each word appears, ignoring grammar and word order.

## Binary Bag of Words
Binary BoW records only the presence (1) or absence (0) of words instead of their frequencies.

## Word Frequency Vectors
Each sentence or document is converted into a vector based on word occurrence counts.

## Vocabulary Creation
A fixed list of unique words (features) is created from the dataset to build consistent vectors.

## Stopwords Removal
Common words like *is*, *the*, and *a* are removed to reduce noise and improve model quality.

## Text Cleaning
Regular expressions are used to remove punctuation, numbers, and special characters from text.

## Lowercasing
All text is converted to lowercase to ensure uniform processing and avoid duplicate features.

## Tokenization
Text is split into smaller units (words or sentences) for further linguistic analysis.

## Word Tokenization
Sentences are divided into individual words called tokens.

## Sentence Tokenization
Paragraphs are split into individual sentences for structured processing.

## Stemming
Words are reduced to their root form by trimming suffixes to normalize variations.

## Porter Stemmer
Porter Stemmer applies rule-based reductions to produce simplified root words.

## Lemmatization
Words are converted to their dictionary base form while preserving contextual meaning.

## WordNet Lemmatizer
WordNet Lemmatizer uses vocabulary knowledge to generate meaningful base words.

## Corpus Construction
Cleaned and processed text samples are stored in a corpus for feature extraction.

## Feature Extraction
Important textual patterns are converted into numeric features for modeling.

## CountVectorizer
CountVectorizer converts text into Bag of Words vectors using word frequency counts.

## TF-IDF (Term Frequency – Inverse Document Frequency)
TF-IDF measures word importance by balancing word frequency and uniqueness across documents.

## Term Frequency (TF)
TF calculates how often a word appears within a specific document.

## Inverse Document Frequency (IDF)
IDF reduces the weight of common words appearing across many documents.

## TF-IDF Vectorization
TF-IDF vectors emphasize meaningful words while suppressing overly common ones.

## Text to Numbers Conversion
NLP vectorization transforms language into numerical matrices suitable for machine learning.

## Model Training
Numerical feature vectors are used to train machine learning algorithms.

## Classification Workflow
Text → Cleaning → Tokenization → Vectorization → Model Training → Prediction.

## Bias and Variance
Bias measures training performance while variance evaluates generalization on unseen data.

## Model Evaluation
Accuracy and confusion matrix are used to assess classification effectiveness.

## Practical Learning Outcome
This project builds intuition for converting human language into structured numerical representations.
