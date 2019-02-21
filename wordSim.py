
def staticmethod(index):
    fullMatrix = False
    print("Load Similarity at index " + str(index))
    cs = []
    with open("matrix.mat") as f:
        for i, line in enumerate(f):
            if fullMatrix or i == index:
                tmp = []
                for string in line.split(' '):
                    tmp.append(float(string))
                cs.append(tmp)
                if not fullMatrix:
                    break

    z = []
    k = 5
    minMaxScore = 0.0
    threshold = 0.1
    # print("Find top-"+ str(k) + " candiates for: ")
    # print(documents[index])
    t = index
    if not fullMatrix:
        t = 0

    for i,score in enumerate(cs[t]):
        if not i == index and score > threshold:
            if len(z) < k:
                minMaxScore = min(minMaxScore, score)
                z.append((i,score))
                z = sorted(z, key=lambda x: x[1])
            else:
                #list full, remove lowest if score is higher
                if score > minMaxScore:
                    minMaxScore = score
                    z[0] = (i,score)
                    z = sorted(z, key=lambda x: x[1])

    sum = 0
    count = 0
    for i,score in z:
        sum += score
        count += 1
        if score > 0.7:
            sum += score
            count += 1

    if count < 1:
        return 0.0
    else:
        return sum/count


# documents=(sample_text,sample_text2)

# documents = [sample_text, sample_text2, sample_text3]
# documents = []
# de_stops = set(stopwords.words('german'))
# punction_stops = ['.', ',','(',')','-','_',' ', ':', ').','),']
#
# candidateIndices = []
#
# # dic = {}
# print("Load sentences:")
# with open("courtDecisionsPreprocessed.json") as f:
#     for line in f:
#         js = json.loads(line)
#         if 'fundstellen' in js:
#             objects = js['fundstellen']
#             for object in objects:
#                 #documents.append(object['sentencesBefore'])
#                 documents.append(object['sentencesRechtssatz'])
#                 if "§ 439" in object['sentencesRechtssatz']:
#                     candidateIndices.append(len(documents) - 1)
#                 #documents.append(object['sentencesAfter'])
#         # if 'sentencesSplitted' in js:
#         #     sentences = js['sentencesSplitted'].split('\n')
#         #     for sentence in sentences:
#         #         documents.append(sentence)
#                 # all_words = nltk.tokenize.WordPunctTokenizer().tokenize(sentence)
#                 # for word in all_words:
#                 #     if word not in de_stops and word not in punction_stops:
#                 #         if not re.search('[0-9]+', word):
#                 #             key = word.lower()
#                 #             if key in dic.keys():
#                 #                 dic[key]= dic[key] + 1
#                 #             else:
#                 #                 dic[key]=1
#
# #                key = ''.join(sorted(keywords))
# #                if key in dic.keys():
# #                    dic[key]= dic[key] + 1
# #                else:
# #                    dic[key]=1
# # 53476 (nice example for high scores)
# # [466, 467, 1063, 2864, 12003, 12004, 24418, 24419, 26046, 26050, 29075, 29077, 29080, 30893, 31086, 31088, 31089, 36138, 36139, 37564, 37566, 37567, 37571, 37575, 38001, 38002, 38004, 38234, 38498, 39836, 44045, 75337, 75339]
#
#
# print(candidateIndices)
# index = 2983
# fullMatrix = False
# print("loaded " + str(len(documents)) + " documents")
# print("Load Similarity at index " + str(index))
# cs = []
# with open("matrix.mat") as f:
#     for i, line in enumerate(f):
#         if fullMatrix or i == index:
#             tmp = []
#             for string in line.split(' '):
#                 tmp.append(float(string))
#             cs.append(tmp)
#             if not fullMatrix:
#                 break
#
# # maxSimilarity = 0.0
# # maxI = 0
# # maxJ = 0
# # with open("matrix.mat") as f:
# #     counter = 0
# #     for i, line in enumerate(f):
# #         for j, string in enumerate(line.split(' ')):
# #             if not i == j:
# #                 if float(string) > maxSimilarity:
# #                     maxSimilarity = float(string)
# #                     maxI = i
# #                     maxJ = j
# #         print('\r' + str(i), end = '\r')
#
# # print("Most similar sentences: ")
# # print(documents[i])
# # print("<---->")
# # print(documents[j])
#
# #print(cs)
#
#
# k = 5
# minMaxScore = 0.0
#
# threshold = 0.2
#
# print("Find top-"+ str(k) + " candiates for: ")
# print(documents[index])
#
# t = index
# if not fullMatrix:
#     t = 0
# print(z)
# print(len(z))
# for i,score in enumerate(cs[t]):
#     if not i == index and score > threshold:
#
#         if len(z) < k:
#             minMaxScore = min(minMaxScore, score)
#             z.append((i,score))
#             z = sorted(z, key=lambda x: x[1])
#         else:
#             #list full, remove lowest if score is higher
#             if score > minMaxScore:
#                 minMaxScore = score
#                 z[0] = (i,score)
#                 z = sorted(z, key=lambda x: x[1])
#
# print("Top candiates: ")
# sum = 0
# for i,score in z:
#     print("(" + documents[i] +","+ str(score) +")")
#     sum += score
#
# print("Average score: " + str(sum/len(z)))
#
# # topSentence = ""
# # topScore = 0
# # tfidf_vectorizer=TfidfVectorizer()
# # i=0
# # # while i < len(documents):
# # j = i+1
# # while j < len(documents):
# #     tmp = (documents[i], documents[j])
# #     tfidf_matrix=tfidf_vectorizer.fit_transform(tmp)
# #     cs=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)
# #     print(cs[0])
# #     if cs[0] > topScore:
# #         topSentence = documents[j]
# #         topScore = cs[0]
# #     j+=1
# #
# # print(topSentence)
# #print tfidf_matrix.shape
#
#
#
# # s = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]
# # for key, value in dic.items():
# #     print(key + " " + value)
#
# #
# # output_file = open("sentences.csv", "w")
# # counter = 0
# # for line in pd.read_csv("cases-texts.csv", sep=';', quotechar='"', encoding='utf-8', header=None, chunksize=1):
# #     print('\r'+str(counter), end = '\r')
# #     counter += 1
# #     try:
# #         keyphrases = summarizer.summarize(line.iloc[0][1], language='german', split=True)
# #         abstract = ""
# #         i = 0
# #         while i < len(keyphrases):
# #             output_file.write('"' + keyphrases[i] + '"\n')
# #             i+=1
# #
# #     except ValueError:
# #         print('Invalid value in line ' + str(counter))
# #
# #
# # output_file.close()
#
# #for chunk in pd.read_csv("cases-texts.csv", chunksize=1):
#     #print(chunk)
#
# #print(keywords.keywords(text, language='german', split=True))
# #keyphrases = summarizer.summarize(text, language='german', split=True, words=50)
# #print(keyphrases[0])
