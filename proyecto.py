import telebot
import speech_recognition as sr
import subprocess


WORDS = ['triste', 'mal', 'deprimido']

r = sr.Recognizer()

bot = telebot.TeleBot('1938055206:AAGQxTzxEAXXuQ6_sxEKp3eiR2jZmHYKJCE')


@bot.message_handler(content_types=['voice'])
def handel(message):
    fileID = message.voice.file_id
    file = bot.get_file(fileID)
    down_file = bot.download_file(file.file_path)
    with open('audio.ogg', 'wb') as f:
        f.write(down_file)

    src_filename = 'audio.ogg'
    dest_filename = 'audio.wav'

    process = subprocess.run(['C:\\webem\\bin\\ffmpeg.exe', '-i', src_filename, dest_filename, '-y'])
    if process.returncode != 0:
        raise Exception("Error")

    file = sr.AudioFile('audio.wav')
    with file as source:
        try:
            audio = r.record(source)        
            text = r.recognize_google(audio, language='es_MX')
            bot.send_message(message.chat.id,text)

            if "amor" in text:
                bot.send_message(message.chat.id, "Estas enamorado?")            

            elif "triste" in text:
                bot.send_message(message.chat.id, "Noto que estas muy triste \n¡Animo!") 

            elif "feliz" in text:
                bot.send_message(message.chat.id, "Noto que estas feliz \n¡Me alegra escucharlo mantente asi!") 

            elif "enojado" in text:
                bot.send_message(message.chat.id, "Noto que estas enojado \n¡Calma, descansa y relajate!")    

            elif "emocionado" in text:
                bot.send_message(message.chat.id, "Noto que estas emocionado \nCuentame ¿Qué es lo que te emociona?")
             
            elif "asustado" in text:
                bot.send_message(message.chat.id, "Noto que estas asustado \nCuentame ¿Qué es lo que te asusta?")   

            elif "aburrido" in text:
                bot.send_message(message.chat.id, "Noto que estas aburrido \nMira una pelicula")

            elif "animado" in text:
                bot.send_message(message.chat.id, "bien portate asi")
            else:
                bot.send_message(message.chat.id, "Hola como estas?")
        except:
            bot.send_message(message.chat.id, "No te he entiendo")
        


bot.polling(none_stop=True)
