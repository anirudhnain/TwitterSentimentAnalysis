# TwitterSentimentAnalysis

<p>The following tool performs sentiment analysis based on lexicon-based approach. The sample tweets are extracted for three recently released english movies (Soutpaw,The Maze Runner and Black Mass). The tweets are classified as positive,negative or neutral based on their predicted score. For detailed description of scoring and prediction refer Report.</p>


# Dependencies
<ol>
<li> Install Python (2.7 or greater) </li>
<li> Set pip to path variable (setx PATH "%PATH%;C:\Python27\Scripts") </li>
<li> Install Tweepy (pip install tweepy) </li>
<li> Install NLTK (pip install nltk) </li>
<li> Download NLTK Data ( python -m nltk.downloader all) </li>
<li> Install ARKNLPTWeet </li>
</ol>

<p>**Note : Install Cygwin in windows to run bash file (runTagger.sh.)</p>

# Execution Sequence
<ol>
<li> Run Tweet_extraction.py</li>
  <ol>
  <li> Specify your Consumer Keys and Access Tokens for OAuth </li>
  <li> Can use your own extraction words by specifying them in tweet_extraction.py track list </li>
  </ol>
<li> Run tweet_text.py </li> 
  <ol>
  <li> Replace the name of the file in tweet_text.py with the name of the extracted tweet.
  <li> Redirect the extracted tweet to a file
  </ol>
<li> Run clean.py (Removes links from extracted tweets)
<li> Run pre_processing.py 
  <ol>
  <li> Does POS Tagging, Stemming, Negation Handling, Stop words removal
  <li> Outputs the Tweet along with its polarity.
  </ol>
</ol>