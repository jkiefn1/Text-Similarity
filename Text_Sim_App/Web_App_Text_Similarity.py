# importing Flask and Flask-based modules
from flask import Flask, request, render_template, jsonify
  
####################################
### TEXT SIMILIARITY CODE BEGINS ###
####################################

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

##################################
### TEXT SIMILIARITY CODE ENDS ###
#### FLASK DEPLOYMENT BEGINS #####
##################################

# Flask constructor 
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('temp.html')

@app.route('/func', methods=['POST'])
def my_form_post():
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       sample1 = request.form.get("s1") 
       # getting input with name = lname in HTML form  
       sample2 = request.form.get("s2")
       
       # Get the pertinent similarity data
       flask_score = text_similarity(sample1,sample2).score()
       flask_sims = text_similarity(sample1,sample2).similarities()
       flask_dissims1 = text_similarity(sample1,sample2).dissimilarities_1()
       flask_dissims2 = text_similarity(sample1,sample2).dissimilarities_2()

       score = str(flask_score)
       sims = str(', '.join(list(flask_sims)))
       dis1 = str(', '.join(list(flask_dissims1)))
       dis2 = str(', '.join(list(flask_dissims2)))
       samples = [sample1, sample2]

       # Render the .html file, with relevant payload
       return render_template('temp.html', score=score, sims=sims, dis1=dis1, dis2=dis2, samples=samples)

@app.errorhandler(Exception)
def handle_exception(error):
    error = str(error)

    if error == 'division by zero':
        error_msg = 'Make sure both text boxes are filled out. Remember, stop words such as "a", "the" and "or" are not counted as words of importance.'
    return render_template('temp.html', error=error, error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)

    
