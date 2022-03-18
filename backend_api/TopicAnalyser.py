import logging

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation

class TopicAnalyser:
    def __init__(self, model_type = "nmf", data = None):
        self.model_type = model_type
        self.data = data

    # get the topic analysis of the whole text
    def display_topics(model, feature_names, no_top_words):
        for topic_idx, topic in enumerate(model.components_):
            return " ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]])

    def analyse(self):
        # TODO: participants should consider changing dataset to match the brief.
        if (self.data == None):
            dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
            documents = dataset.data

        # HYPERPARAMETERS: Consider tuning
        no_features = 1000
        no_topics = 20

        if self.model_type == "nmf":
            # NMF is able to use tf-idf
            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
            tfidf = tfidf_vectorizer.fit_transform(documents)
            tfidf_feature_names = tfidf_vectorizer.get_feature_names()
            # Run NMF
            model = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
        elif self.model_type == "lda":
            # LDA can only use raw term counts for LDA because it is a probabilistic graphical model
            tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
            tf = tf_vectorizer.fit_transform(documents)
            tf_feature_names = tf_vectorizer.get_feature_names()
            # Run LDA
            model = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online',
                                        learning_offset=50., random_state=0).fit(tf)
        else:
            logging.exception("Invalid model_type: {}".format(self.model_type))

        # HYPERPARAMETER: Consider tuning
        no_top_words = 10

        topics = self.display_topics(model, tfidf_feature_names, no_top_words)
        return topics