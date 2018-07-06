from nltk.tokenize import sent_tokenize, word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

data = "Sudah dari dua tahun lalu kami di komisi IX mengkritisi hal tersebut. Karena selain tidak mengandung susu sapi, ternyata produk susu kental manis ini mengandung lebih dari 40% gula, sehingga selain merusak gigi, produk ini juga tidak memiliki kandungan gizi susu. Karena yang dikandung hanya 8% lemak susu. Tentu ini dapat di kategorikan penipuan publik!"
factory = StopWordRemoverFactory()
stopwords = factory.get_stop_words()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
#print(stopwords)
#print(sent_tokenize(data))
#print(word_tokenize(data))

#Jadi per kata
words = word_tokenize(data)
wordsFiltered = []

# Hapus Stopwords
for w in words:
    if w not in stopwords:
        w = stemmer.stem(w)  #Stemming
        wordsFiltered.append(w)

print(wordsFiltered)



