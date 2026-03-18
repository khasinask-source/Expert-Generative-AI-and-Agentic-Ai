# spaCy & NLP Fundamentals – Practical Concept Summary

This repository demonstrates how spaCy and NLP techniques transform raw text into structured linguistic and numerical representations for intelligent processing.

## spaCy Library
spaCy is an industrial-strength NLP library designed for fast and efficient text processing and linguistic analysis.

## Language Model Loading
A spaCy language model (e.g., en_core_web_sm) is loaded to enable tokenization, tagging, parsing, and entity recognition.

## Document Object (Doc)
Text processed by spaCy is stored as a Doc object containing tokens and linguistic annotations.

## Tokenization
spaCy automatically splits text into tokens such as words, punctuation, and symbols.

## Token Attributes
Each token provides metadata like text, lemma, part of speech, shape, and stopword status.

## Lemma (Base Form)
Lemma represents the dictionary form of a word, enabling normalization of word variations.

## Part of Speech (POS)
POS tagging assigns grammatical roles such as noun, verb, adjective, or pronoun to tokens.

## Dependency Parsing
Dependency parsing identifies grammatical relationships between words in a sentence.

## Stopwords
Stopwords are common words automatically identified by spaCy that often carry limited semantic value.

## Built-in Stopword List
spaCy provides predefined stopword sets accessible via STOP_WORDS for text cleaning.

## Punctuation Handling
Punctuation symbols are treated as separate tokens and may be removed during preprocessing.

## Text Cleaning
Text normalization removes unwanted characters and ensures consistent token analysis.

## Word Frequency Calculation
Word frequency measures how often meaningful words appear within a document.

## Noise Reduction
Stopwords and punctuation are excluded to focus on semantically important terms.

## Normalized Frequencies
Word frequencies are scaled by the maximum frequency to compute weighted importance.

## Sentence Segmentation
spaCy divides text into sentences using statistical and rule-based boundary detection.

## Sentence Tokens
Each sentence is treated as a processing unit for scoring and summarization.

## Sentence Scoring
Sentences are scored by summing normalized word frequencies to estimate importance.

## Extractive Summarization
Top-scoring sentences are selected to generate a concise summary of the text.

## Heap-Based Selection
Largest sentence scores are chosen efficiently using priority-based selection logic.

## Summary Generation
Selected sentences are combined to produce a human-readable summary.

## NLP Pipeline Concept
spaCy processes text through sequential components like tokenizer, tagger, parser, and NER.

## Named Entity Recognition (NER)
NER identifies real-world entities such as names, locations, organizations, and numbers.

## Text → Structured Data
spaCy converts unstructured text into linguistically annotated data objects.

## Bag of Words (BoW)
BoW represents documents using word occurrence counts without considering word order.

## Binary BoW
Binary BoW captures only word presence or absence instead of frequency.

## TF-IDF Representation
TF-IDF weighs words based on importance by balancing frequency and uniqueness.

## Feature Vectors
Textual data is transformed into numerical vectors for machine learning models.

## Text → Numbers Conversion
Vectorization converts language into machine-understandable numeric matrices.

## Machine Learning Integration
Extracted features are used to train classifiers for prediction tasks.

## Model Training Flow
Text → Cleaning → Tokenization → Vectorization → Model → Prediction.

## Bias and Variance
Bias reflects training performance while variance indicates generalization ability.

## Practical Learning Outcome
This project builds intuition for real-world NLP, spaCy pipelines, vectorization, and summarization workflows.
