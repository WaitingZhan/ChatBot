# ChatBot
<img src="https://github.com/WaitingZhan/ChatBot/blob/master/chat%20bot%20model.png" width="400" height="500"> <img src="https://github.com/WaitingZhan/ChatBot/blob/master/chat%20bot%20parameter.png" width="400" height="500">

This project explored the effect of the dataset and the learning rate and the number of hidden layers of the model on chatbot performance.  We trained our Chatbot on [Cornell Movie Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html), [Daily Dialog Corpus](http://yanran.li/dailydialog), and the mix of Cornell Movie Corpus and Daily Dialog Corpus. To improve the performance of the Chatbot, we trained a Dialog Act Classifier to label Cornell Movie Corpus. Then add the Dialog Act as a feature to train the Chatbot. We evaluated the performance of Chatbot in grammaticality, naturalness, and interestingness.

Sequence to Sequence model trained on cornell movie dataset and daily dialogue dataset.     
You: hi.    
ChatBot:  I am not sure I am not going to be aout.     
You: how are you.   
ChatBot:  I am not sure I am not sure.   
You: Where are you from?  
ChatBot:  I am not sure.  
You: What do you do for a living?  
ChatBot:  I am not sure I am not going to be aout.  
You:  Can you let me know what time it is?  
ChatBot:  I am not sure.  
You: Do you have time to go shopping tomorrow?  
ChatBot:  I am not sure I am a littleout.  
You: When is your birthday?  
ChatBot:  I am not sure I am not going to be able to be aout.  
You: Which one do you prefer, a dog or a cat?  
ChatBot:  I am not sure I am not going to be able to be aout.  
You: When is the next Olympic?  
ChatBot:  I am not sure.  
You: Can you recommend any country to go on a trip?  
ChatBot:  I am not sure.  
You: How is the weather today?  
ChatBot:  I am not sure I am not going to be aout.  
You: I miss my family.  
ChatBot:  I am not sure.  
You: have a good day.    
ChatBot:  I am not sure I am not sure I am not going to be able to be aout.  
You: happy new year.   
ChatBot:  I am not sure I am not going to be able to be able to be aout.  

