# Mavens exercise
=========

## Coding exercise
==========

The ExtractSentence script will takes as input a file containing short pieces of text, one per line, UTF-8 encoded. 
The code reads the texts from the file and computes
all the 5-word sequences which occur in any line of
text. The output is written to a UTF-8-encoded CSV file, 
giving the ten most commonly-occurring sequences and how often each occurs.

You can run the script by replacing the filepaths with the ones to your own data

#### Assumptions for this script:
- python 3 is used
- input is utf-8 encoded
- input lines are split by newline characters ('\n')

## Data exercise
===============

### Sentiment analysis method implementation proposal

In this proposal, we outline how we might implement a method able to guess if the sentiments expressed in a short snippet of text are positive or negative. 

To do this we use techniques prevalent to the field of sentiment analysis, a form of natural language processing (NLP).

#### Supervised machine learning (SML)

With a representative sample of negative and positive sentiment text snippets the first approach would be to use supervised machine learning (SML). The labelled dataset can be  used as training sets, and another curated dataset can be used as testing set to measure the model’s performance.

In this technique we need to come up with a numerical feature vector. A straightforward approach would be to assign a sentiment score to each word and compute the resulting overall sentiment in each sentence of our training set. For example each word could be given a score between -5 and 5 where -5 expresses a negative sentiment and 5 a positive one. 

In addition, [SentiWordNet](http://sentiwordnet.isti.cnr.it/) provides a large labelled lexicon of words with associated positive and negative sentiment scores.

The resulting feature vector we would use is therefore `[overall sentiment score, sentence]` and our predictive model would yield either one of two labels `[pos, neg]` or the probabilities associated for each value. (e.g `[0.5, 0.7]`)

Two potential SML algorithms we could use to train our model would be Naive Bayes or a Support Vector Machine (SVM).

The Naive Bayes algorithm uses the training data set to create priors. It is one of the fastest machine learning technique, does not require much training data, and can yield good results, but it makes the “naive” assumption that every pair of features is independent. It is also a bad estimator, so the probabilities computed cannot be relied on. We would use the Bernoulli version of this method since it is designed for binary features.

Support Vector Machines (SVM) have the advantage of being effective in high dimensional spaces. They constructs a hyper-plane or set of hyper-planes in a in a high or infinite dimensional space, and then use this resulting separation to classify data. The optimal hyper-plane is the one with the largest distance to the nearest data point of any class. We could use the basic implementation of this algorithm (SVC) or one which is more complex but less computationally expensive (LinearSVC).

all algorithms are available in scikit-learn:
- [`sklearn.naive_bayes.BernoulliNB`](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB)
- [`sklearn.naive_bayes.MultinomialNB`](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)
- [`sklearn.svm.SVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC)
- [`sklearn.svm.LinearSVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC)

#### Unsupervised machine learning

An alternative to using training data to generate the predictive model is to rely on clustering algorithms. In this case we provide unlabelled data and rely on the algorithm to assign labels to it. Since we have a labelled dataset this is not necessarily a good option. The problem of this approach is that it is computationally expensive.

If we had to use this method, we would use the Latent Dirichlet Allocation algorithm. This is a form of  Principal component analysis (PCA) meant to work well on text. It has already been successfully implemented for sentiment analysis. [1]

The relevant implementation in scikit-learn is

- [`sklearn.decomposition.LatentDirichletAllocation`](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)

#### Deep Learning

Some recent approaches to sentiment analysis are based on deep learning. Those techniques require vast datasets and are computationally expensive. Those requirements means that it would not be practical to implement it ourselves, and we should rely on existing SaaS services from larger companies if we choose to do so.

According the the literature, Convolutional neural networks (CNN) are so effective at language classification tasks that they can be considered as the standard technique in NLP classification. [[1]](https://arxiv.org/pdf/1408.5882v2.pdf)

#### Pitfalls

The main potential pitfall we will need to look out for is overfitting. This occurs when the predictive model ends up fitting too close to the the training data. This problem is especially potent in sentiment analysis since the source of the sentiment lexicon might yield a model unsuited to another domain. We can mitigate this problem by using data from more than one source for the training set.

#### SaaS solutions

Although we could spend time and resources training and optimising our own machine learning model, it would be much more practical to use existing models developed by large companies such as Google or Microsoft. The problem with using those APIs is that we must pay for them if used at high volumes. All of them are based on deep learning. (They leverage the large amount of data availables to those companies)

We can do this with the APIs they provide. Here’s a evaluation of the main ones:

[**Google Cloud Natural Language API**](https://cloud.google.com/natural-language/)

This API will yield a detailed analysis of any snippets of text. As long as a single request does is not over 500 characters, the analysis is free.

The API will yield a sentiment score between -1 and 1, where -1 signals a negative impression and +1 a positive one.

[**IBM Watson Natural Language Understanding**](https://www.ibm.com/watson/services/natural-language-understanding/)

As long as we do not process more than 30,000 characters in a month, the API is free.
The API also yields a sentiment score between -1 and 1.

[**Microsoft Cognitive Service Sentiment Analysis API**](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c9)

The API remains free if we do not make more than 5,000 calls to it in a month. It yields a sentiment score between 0 and 1, 0 being a negative expression.

#### Conclusions

I would recommend using existing solutions for this problem, and simply rely on already implemented sentiment analysis APIs. This is because training our own predictive models would expend unnecessary resources and we will never have access to the same amount of training data as companies such as google or microsoft.

The completed method would take in an arbitrary number of sentences, assign them the positive or negative labels, and return the labelled data in a dictionary. The pseudocode is as follows:
```
function analyseSentences (sentences) {
    
    for sentence in sentences:
        label = sentimentAPI.send(sentence)
        results[“sentence”] = label
    
    return results
}

```

The hypothetical sentimentAPI object in the above code represents the API solution we will choose.

