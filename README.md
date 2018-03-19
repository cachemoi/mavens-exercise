# Mavens exercise

## Coding exercise

The `ExtractSentences.py` script will takes as input a file containing short pieces of text, one per line, UTF-8 encoded. 
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

Here we outline how we might implement a method able to guess if the sentiments expressed in a short snippet of text are positive or negative. 

#### Supervised machine learning (SML)

With a representative sample of negative and positive sentiment text snippets the first approach would be to use supervised machine learning (SML). The labelled dataset can be  used as training sets, and another curated dataset can be used as testing set to measure the model’s performance.

A straightforward approach would be to assign a sentiment score to each word and compute the resulting overall sentiment in each sentence of our training set. For example each word could be given a score between -5 and 5 where -5 expresses a negative sentiment and 5 a positive one. 

In addition, [SentiWordNet](http://sentiwordnet.isti.cnr.it/) provides a large labelled lexicon of words with associated positive and negative sentiment scores.

We would therefore use `[overall sentiment score]` as a feature and our predictive model would yield a binary label `[pos, neg]`

The algorithm I would use is Naive Bayes.

The Naive Bayes algorithm uses the training data set to create priors. It is one of the fastest machine learning technique, does not require much training data, and can yield good results, but it makes the “naive” assumption that every pair of features is independent. It is also a bad estimator, so the probabilities computed cannot be relied on. We would use the Bernoulli version of this method since it is designed for binary features.

The algorithm is available in scikit-learn:
- [`sklearn.naive_bayes.BernoulliNB`](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB)

#### Unsupervised machine learning

An alternative to using training data to generate the predictive model is to rely on clustering algorithms. In this case we provide unlabelled data and rely on the algorithm to assign labels to it. Since we have a labelled dataset this is not necessarily a good option. The problem of this approach is that it is computationally expensive. I therefore do not recommend this option.

#### Deep Learning

Some recent approaches to sentiment analysis are based on deep learning. Those techniques require vast datasets and are computationally expensive. Those requirements means that it would not be practical to implement it ourselves, and we should rely on existing SaaS services from larger companies if we choose to do so.

According the the literature, Convolutional neural networks (CNN) are so effective at language classification tasks that they can be considered as the standard technique in NLP classification. [[1]](https://arxiv.org/pdf/1408.5882v2.pdf)

#### Pitfalls

The main potential pitfall we will need to look out for is overfitting. This occurs when the predictive model ends up fitting too close to the the training data. This problem is especially potent in sentiment analysis since the source of the sentiment lexicon might yield a model unsuited to another domain. We can mitigate this problem by using data from more than one source for the training set.

#### SaaS solutions

The most efficient way to perform sentiment analysis uses deep learning, and the vast datasets and computing power required mean that it would be a waste of resources to do it ourselves. It’s therefore better to use an existing SaaS solution. The problem with using those APIs is that we must pay for them if used at high volumes. All of them use some form of deep learning. 

The [**Google Cloud Natural Language API**](https://cloud.google.com/natural-language/) seems to be the best one. This API will yield a detailed analysis of any snippets of text. As long as a single request does is not over 500 characters, the analysis is free.

#### Conclusions

I would recommend using existing solutions for this problem, and simply rely on already implemented sentiment analysis APIs. This is because training our own predictive models would expend unnecessary resources and we will never have access to the same amount of training data as companies like Google.

The completed method would take in an arbitrary number of sentences, assign them the positive or negative labels, and return the labelled data in a hash map. The pseudocode is as follows:
```
function analyseSentences (sentences) {
    
    for sentence in sentences:
        label = sentimentAPI.send(sentence)
        results[“sentence”] = label
    
    return results
}

```

The hypothetical sentimentAPI object in the above code represents the API solution we will choose.

