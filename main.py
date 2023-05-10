import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_input(input_text):
    # Токенизация - разделение текста на отдельные слова
    tokens = word_tokenize(input_text.lower())
    if 'no' in tokens or 'yes' in tokens:
        return tokens
    # Удаление стоп-слов - часто используемых слов, которые не несут смысловой нагрузки
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Лемматизация - приведение слов к их базовой форме
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


def generate_response(input_text, last_response):
    response = "I'm sorry, I didnt understand your message."
    # Предварительная обработка входного сообщения
    tokens = preprocess_input(input_text)
    print(tokens)
    # Определение правил для формирования ответов
    if 'hello' in tokens or 'hi' in tokens or 'yo' in tokens:
        response = 'Hello! How can I assist you?'
    elif 'goodbye' in tokens or 'bye' in tokens:
        response = 'Goodbye! Have a nice day.'
    elif 'book' in tokens and 'like' in tokens and '?' in tokens or 'favorite' in tokens:
        response = "My two favorites are 'We' by Evgeny Zamyatin and 'Gone with the Wind' by Margaret Mitchell. 'We' provides a glimpse into the future and see what life might look like in a society where individual freedom and individuality are suppressed for the greater good. I like 'Gone with the Wind' a lot because it's a great historical novel that describes the lives of people during the American Civil War. The book leaves an unforgettable impression and makes you think about life and values."
    elif 'recommend' in tokens and 'read' in tokens:
        response = "What genre of books do you like?"
    elif 'let' in tokens and 'talk' in tokens:
        response = "Of course! What genre of books do you like?"
    elif 'yes' in tokens:
        if "Utopia! " in last_response:
            response = "I am pleased to provide you with a list of the top five books in the utopian genre:\n"\
                        "1. Brave New World by Aldous Huxley is a classic book that tells the story of life in an ideal society where people live without disease or conflict but at a high price.\n"\
                        "2. '1984' by George Orwell is a novel that describes a totalitarian world where the government controls all aspects of people's lives. The book warns us against what can happen if the government becomes too powerful.\n"\
                        "3. 'Opium for the People' by Eugene Zamiatin is a book that describes the life of people in a single state, where every inhabitant has his own number, and the government controls all aspects of their lives.\n"\
                        "4. Plato's 'State' is an ancient book that describes an ideal society based on justice and reason. The book is the basis for many modern utopias.\n"\
                        "5. 'Return from the Future' by Robert Heinlein is a book that tells about a future society where human rights and freedoms are recognized as more important than any other values. This book is one of the most famous and popular in the genre."
    elif 'no' in tokens:
        if "Utopia! " in last_response:
            response = "Oh, okey.."
    elif last_response == "What genre of books do you like?" or last_response == "Of course! What genre of books do you like?":
        if 'utopia' in tokens:
            response = "Utopia! I also like to read books about utopian worlds because they give me the opportunity to imagine myself as a hero who helps create an ideal world. Do you want me to recommend the 5 best books in this genre?"
        if 'futurism' in tokens:
            response = "I also like books in the futuristic genre, because they give me the opportunity to immerse myself in an amazing world full of new technologies and unusual possibilities. I find inspiration in stories about fighting against technological challenges, about creating new worlds, and about how our technologies can help us overcome our real problems."
        if 'detective' in tokens:
            response = "The detective genre is an exciting and fascinating genre of literature that I love very much. Reading detectives, I plunge into the exciting world of mysteries, intrigues and investigations, which does not let me go until the very end of the book."
        if 'psychology' in tokens:
            response = "The genre of psychology is one of my favorite genres of literature, which I read with pleasure. Books of this genre usually reveal the theories and concepts of psychology, as well as give advice and practical recommendations on how to improve the psychological state."
        if 'fantastic' in tokens:
            response = "In fantasy books, I find many interesting ideas that can sometimes become a reality in the future. I love reading books that allow me to see the world from a different perspective, learn something new and unusual, and gain new knowledge about scientific and technological developments."
        if 'love story' in tokens:
            response = "A romance novel is a genre of literature in which a love story between two protagonists takes center stage. Usually such books have a complex plot, which includes many twists and turns and unexpected twists. However, in my opinion, romance novels are prone to hackneyed and clichéd plots that aren't particularly interesting. Often the characters in such books are endowed with idealized character traits, which makes them unrealistic and unnatural."


    return response


if __name__ == '__main__':
    input_message = "Yo"
    response = generate_response(input_message, last_response='')
    print(response)
