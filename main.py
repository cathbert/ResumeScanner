# Download required libraries
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# This function's argument is a .docx file type document path
def main(document):
    # Load data
    resume = docx2txt.process(document)

    # in this expression we use another .docx file type document against the one we want to score
    # this document has the required keywords
    job_description = docx2txt.process('job_description.docx')

    # creating a list of text
    texts_list = [resume, job_description]

    count_v = CountVectorizer()

    count_matrix = count_v.fit_transform(texts_list)

    # Print the similar scores
    print('Curriculum Vitae score:')
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100

    print(str(round(matchPercentage, 2)) + ' %')
    input()



if __name__ == '__main__':
    main('PyCharm')

