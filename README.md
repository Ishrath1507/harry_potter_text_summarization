# harry_potter_text_summarization


Huge amount data have been generated every day on various platforms such as Wikipedia, technical and non-technical blogs, social media, online news articles etc. Around five millions of articles are present in Wikipedia alone and every day thousands of new articles are added to it. Due to the huge amount data gathered every day, the users are bombarded with the large volume of data. For the human being, it is difficult to assimilate this huge amount of data. So, effective techniques are required to help the user to assimilate the data and make the data available for his use.



This research focuses on use of the text summarization and text sentiment analysis simultaneously on the text data. The summarization will reduce the amount of data and sentiment analysis helps the user to identify good, bad and other information in the documents. The summarization techniques produce a brief representation of the text and sentiment analysis will deduce the emotion expressed in the text. The BBC news articles related to sports are selected to demonstrate the research of document summarization and sentiment analysis. Basically, there are two types of summarization techniques: extractive and abstractive summarization. In the abstractive method, the semantic representation of the text is developed to produce a brief overview of the input text. The extraction method determines weightage of words, phrases, and sentences in the text. They produce the summary by selecting the most important words, sentence, and phrases from the text. In this research, the extractive summarization technique is applied on the BBC news articles as shown in figure 2.


Sentiment Analysis of News Documents

The sentiment analysis on the text document will make the user understand the emotional intend of the text. For a given text document, sentiment analysis can be carried out to word level, phrase level, sentence level or document level. The sentiment analyzer such as VADER produces the sentiment information such as positive, negative, neutral and compound score. It also gives the number of positive, the number of negative and number of neutral words in the text. BBC news documents are subjected to sentiment analysis using VADER and below table shows sentiment information for a few news articles. The frequency of noun occurrences in each BBC document is determined. The main topic of a BBC document is focused on the most frequent noun in that document. Various sentiment information collected using VADER has been displayed in the below table.



Summarization and Sentiment Analysis

The text summarization gives a brief representation of the original text. The sentiment analysis can be applied after the document is summarized to a briefer version. The following table shows the sentiment scores when a news article is subjected to the summarization ratio of 25%, 50%, and 75%. The original BBC news article consists of 16 sentences and is reduced to the brief summary of 4 sentences, 8 sentences, and 12 sentences. The compound score for the original article is 0.9726 which reduced to 0.9618 for 75% summary and 0.6908 for 50% summary. As the ratio of summarization increases, the compound score reduces gradually.



        



