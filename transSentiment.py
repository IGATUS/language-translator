import streamlit as st 
import os
from textblob import TextBlob 
from googletrans import Translator
import speech_recognition as sr 
from gtts import gTTS 
import time
import playsound
def speak(text):
	tts= gTTS(text=text,lang='en')
	filename='myaudio.mp3'
	tts.save(filename)
	playsound.playsound(filename)
def main():
	st.title('Translator and Sentimental Analysis Apps')
	st.write('Built with streamlit and Python')
	activity=['Translator','Sentimental Analysis']
	choice=st.sidebar.selectbox('Select Activities: ',activity)
	if choice=='Translator':
		st.write('Translator')
		from_text=st.text_input('Enter a sentence')
		text_lang=st.text_input('Enter a language code')
		
		if st.button('Translate'):
			init=Translator()
			try:
				result=init.translate(from_text,dest=text_lang).text
				st.success(result)
			except Exception as e:
				a1=os.system('ping www.google.com')
				if a1==1:
					st.write('Please check your internet connection')
				else:
					st.write('Invalid language selected')
	elif choice=='Sentimental Analysis':
		st.write('Sentimental Analysis')
		from_text=st.text_input('Enter a sentence')
		if st.button('Analyse'):
			sent=TextBlob(from_text)
			r=sent.sentiment.polarity
			if r==0:
				st.success('This is a Neutral message!')
			elif r>0:
				st.info('This is a Positive Message')
			else:
				st.warning('This is a Negative Message')									
if __name__=='__main__':
	main()