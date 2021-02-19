# This is a program to detect similarity between texts, deployed using Python.
# While libraries like NLTK, Scikit, etc. would be useful, this script does not require any imports

# To run the program, simply hit 'run' in this .py file
# ... or comment out this app's "run the program" lines, import this .py file and run text_similarity(sample_1,sample_2).score(), .dissimilarities(), or .similarities()

# Initialize the sample texts
sample_1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
sample_2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
sample_3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

# Initialize lists/dicts of punctuation, contractions, stop-words, etc. for the script
list_of_punctuations_for_splitting = ['.','?','!']
list_of_punctuations = ['.',',','?',';']
dict_of_contractions = {"'ll":" will", "n't":" not"}

# NLTK's list of English stopwords
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
              "you", "your", "yours", "yourself", "yourselves", "he", "him",
              "his", "himself", "she", "her", "hers", "herself", "it", "its",
              "itself", "they", "them", "their", "theirs", "themselves", "what",
              "which", "who", "whom", "this", "that", "these", "those", "am",
              "is", "are", "was", "were", "be", "been", "being", "have", "has",
              "had", "having", "do", "does", "did", "doing", "a", "an", "the",
              "and", "but", "if", "or", "because", "as", "until", "while", "of",
              "at", "by", "for", "with", "about", "against", "between", "into",
              "through", "during", "before", "after", "above", "below", "to",
              "from", "up", "down", "in", "out", "on", "off", "over", "under",
              "again", "further", "then", "once", "here", "there", "when",
              "where", "why", "how", "all", "any", "both", "each", "few",
              "more", "most", "other", "some", "such", "no", "nor", "not",
              "only", "own", "same", "so", "than", "too", "very"," can", 
              "will", "just", "don", "should", "now"]

###############################
###### BUILD THE PROGRAM ######
###############################

# Create a function to create a bag of words from each sample text, ignore stopwords
def tokenize_without_stopwords(sample):
    
    s = sample
    
    # Replace any sentence-ending punctuation into one type for ease of use
    for l in list_of_punctuations_for_splitting:
        s = s.replace(l+str(' '),'.')
    
    # Handle contractions
    for key in dict_of_contractions:
        s = s.replace(key,dict_of_contractions.get(key))

    # Lowercase the entire sample text, then split it.
    for l in list_of_punctuations:
        s = s.lower().replace(l,' ')
        
    # Create the bag of words
    word_list = s.split()
        
    # Remove stop-words
    for sw in stop_words:
        while sw in word_list:
            word_list.remove(sw)
            
    bag_of_words = []
            
    # Stem words that are plural
    for word in word_list:
        for suffix in ['s']:
            if word.endswith(suffix):
                bag_of_words.append(word[:-len(suffix)])
            else:
                bag_of_words.append(word)
    
    return bag_of_words

# Create a class, with two string arguments, for analyzing
class text_similarity():
    
    def __init__(self, sample1, sample2):
    
        # Tokenize the text samples
        s_1 = tokenize_without_stopwords(sample1)
        s_2 = tokenize_without_stopwords(sample2)

        # Initialize lists or counts
        similar_count = 0
        similar_words = []
        dissimilar_words1 = []
        dissimilar_words2 = []

        for a in s_1:
            if a in s_2:
                similar_count+=1
                similar_words.append(a)
            else:
                dissimilar_words1.append(a)

        dissimilar_words2 = list(set(s_2)-set(similar_words))

        # Construct the methods for calling
        self.scr = round(similar_count/max(len(s_1),len(s_2)),2)
        self.sims = similar_words
        self.dissims1 = dissimilar_words1
        self.dissims2 = dissimilar_words2

    # Create a method to return the score
    def score(self):
        return self.scr    
        
    # Create a method to return similar words
    def similarities(self):
        return self.sims
    
    # Create a method to return dissimilar words from text sample 1
    def dissimilarities_1(self):
        return self.dissims1

    # Create a method to return dissimilar words from text sample 2
    def dissimilarities_2(self):
        return self.dissims2
    
#############################
###### RUN THE PROGRAM ######
#############################

ts = text_similarity(sample_1,sample_2)

# Similarity score
# score = (number_of_similar_words / total_number_of_words)
score = ts.score()

# List of similar words
# if word in sample text A and sample text B then return word
sim = ts.similarities()

# Dict of dissimilar words
# if word in sample text A is not in sample text B, then return the word from sample text A as a key, and its position as a value
dis1 = ts.dissimilarities_1()
dis2 = ts.dissimilarities_2()

print(score)
print(sim)
print(dis1)
print(dis2)
