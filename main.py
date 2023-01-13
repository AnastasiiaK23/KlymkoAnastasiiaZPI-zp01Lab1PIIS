import speech_recognition as sr
import sys
import webbrowser
import pyttsx3

# Функция, позволяющая проговаривать слова
def talk(words):
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()

talk("Привет!")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Слушаю вас?")
		r.pause_threshold = 0.5
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + zadanie)
	except sr.UnknownValueError:
		talk("Я вас не поняла, повторите")
		zadanie = command()

	return zadanie

def makeSomething(zadanie):
	if 'открой сайт' in zadanie:
		talk("Открываю")
		url = 'https://colab.research.google.com/drive/1phrg_YdRdF2r9lBCjHat7triz3dkg-7e#scrollTo=BMId2hi5h1FL'
		webbrowser.open(url)
	elif 'стоп' in zadanie:
		talk("ok, до встречи")
		sys.exit()
	elif 'как тебя зовут' in zadanie:
		talk("Меня зовут Сири")
while True:
	makeSomething(command())
