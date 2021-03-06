# Text-Similarity
## Table of contents
* [General info](#general-info)
* [Folder Structure](#folder-structure)
* [Important Notes](#important-notes)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
This project is a simple program designed to check the similarity between two bodies of text. While the use of NLP modules would be extremely helpful, this program is written in python alone and deployed via flask.

The ```text_similarity()``` class has several methods that you may find useful for comparing text samples.
* The .score() method returns the number of words similar between the two samples, and divides that number by the length of the longer of the two text samples.
* The .similarities() method returns a list of words that are similar to both text samples.
* The .dissimilarities_1() method returns a list of words that are unique to the first text sample.
* The .dissimilarities_2() method returns a list of words that are unique to the second text sample.
	
## Folder Structure
This git repository contains a stand-alone python file that just performs the text similarity comparison, without deploying it via flask ([Text_Similarity.py](https://github.com/jkiefn1/Text-Similarity/blob/main/Text_Similarity.py)), and a separate folder structure with the necessary .py file and .html template for deployment via flask ([Text_Sim_App](https://github.com/jkiefn1/Text-Similarity/tree/main/Text_Sim_App)).	

## Important Notes
This program utilizes the removal of stopwords, as outlined by [NLTK's list of English Stopwords](https://gist.github.com/sebleier/554280). 
This program also attempts to handle contractions by separating them into their originating words.

## Technologies
Project is created with:
* Python 3.9.1
* Flask 1.1.2
* Werkzeug 1.0.1
	
## Setup
To run this project, download the folder structure and run via your preferred Python environment. The below steps may assist you:

```
https://github.com/jkiefn1/Text-Similarity.git
cd Text-Similarity
$ python3 Web_App_Text_Similarity.py
```
