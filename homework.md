List and discuss few methods that are deployed in text analysis to
reduce the dimensions?

# Why
One of the common first steps in text analysis is boiling down the text to
bag of words and doing a TF-IDF analysis. Most TF-IDF analysis, especially for
real world data usually results in a matrix/vector which is highly dimensional.
But the problem with high dimensionality is that most of the dimensions are too
sparse. These sparse dimensions often contribute to noise in most algorithms
like clustering, often referred as `Curse of dimensionality`. Sparse dimensions
lead to overfitting models and over complicated target functions. So to increase
the performance and accuracy of the model most valuable dimensions need to be
extracted first. The following are some technique to reduce dimensions in
textual data.

# List of methods
- **Tokenization**
  First words in a sentence need to be extracted. Finally the goal for
  tokenization is to identifying related and meaningful keywords. All special
  characters like hyphens(-), brackets are removed. Note Punctation marks need
  to be dealt differently as they often tend to contribute intent. All the
  abbreviations and acronyms  which have to be transformed into a standard form.

- **Stemming**
   Also referred to as lemmatization. The goal is to reduce words into root
   forms. Verbal forms reduced to stem, ex. performing -> perform. Plurals or
   names are also reduced to just the Names ex. Tim's -> Tim. Some problems with
   stemming sometimes is that root words are incorrect, but there are useful all
   those words are consistently transformed into the same stem. Case sensitive
   systems could also see issues.
   Some stemming algorithms:
    * Porter Stemmer(most common) is based on suffixes are based on smaller
      suffixes, ex ing -> "" (typing - typ) or sses -> "ss" (caresses - caress).
      Problem is this algorithm doesn't always result in real words.
    * Lovins Stemmer, the longest suffix is reduced to stem and then into valid
      words. Its much more complex then Porter stemmer so much more time
      consuming.
    * Dawson Stemmer, it extends Lovins algorithm. But the suffixes are in
      reverse order and index is based on the length and last letter.
      But it is complex to implement.

- **Stopword elimination**
    Some words in english do contribute to the meaning of the document, but are
    present for grammatical reasons. Those words are called stopwords, they are
    articles, pro-nouns and prepositions. They usually do not contribute to
    text mining/analysis and can be eliminated. More words which do not
    contribute, can also be added to stopwords and removed. This process reduces
    the text and thereby contribute to improvement in the performance of the
    analysis algorithm.
- **Topic Modeling**
    This is to extract and discover abstract topics from the text being
    analyzed. LSA And LDA are often used for topic modeling. Topic modeling is
    powerful in identifying imported feature/ dimensions. Often is the best
    way to gain insights from huge amounts of textual data.

  - **Latent semantic indexing**
      This is based on a mathematical technique called Singular value
      decomposition(SVD). SVD is a concept from Liner algebra, its states that a
      rectangular matrix can be decomposed into a 3 smaller matrix
      components(A=SUV). SVD is applied to the highly dimensional vector model
      to convert to a lower dimensional space. SVD helps in reduces in the no of
      dimensions whilst keeping the original meaning intact. The basic
      assumption of LSA is that words which have similar meanings will occur in
      similar pieces of text. This is a computational very demanding, scaling
      this model can be very challenging.

  - **Latent dirichlet allocation**
      This is a generative model or in other word employees unsupervised
      learning. It based on a Bayesian probability model. The basic aim for LDA
      is to extract similar pieces of data/words from any given text/document.
      These  similar pieces of data can be collapsed thereby reducing the number
      of dimensions. The way LDA extracts topics is it starts by randomly
      assigning the words as topics. These topics are mapped to the documents.
      Then it moves to next set of random topic, and the process it repeated
      until it finally extracts topics that can mapped to most of the documents.
      LDA is not that suitable when dealing with short documents or documents
      that do not have common topics.

# Refs
- https://www.ijert.org/research/text-data-pre-processing-and-dimensionality-reduction-techniques-for-document-clustering-IJERTV1IS5278.pdf
- https://blog.exploratory.io/demystifying-text-analytics-part-4-dimensionality-reduction-and-clustering-in-r-cbc8c90e0b14
- https://papers.nips.cc/paper/3599-disclda-discriminative-learning-for-dimensionality-reduction-and-classification.pdf
