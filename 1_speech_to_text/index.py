import speech_recognition as sr_07_nvt
from pydub import AudioSegment as AudioSegment_07_nvt
from gtts import gTTS as gTTS_07_nvt
import playsound as playsound_07_nvt
import os as os_07_nvt

parent_dir_07_nvt = "1_speech_to_text/"
wav_file_07_nvt = "temp.wav"

def speak_choice_07_nvt(text):
    tts_07_nvt = gTTS_07_nvt(text=text, lang="en")
    filename_07_nvt = "choice.mp3"
    tts_07_nvt.save(filename_07_nvt)
    playsound_07_nvt.playsound(filename_07_nvt)

def mp3_to_wav_07_nvt(mp3_file_07_nvt):
    mp3_file_07_nvt = os_07_nvt.path.abspath(parent_dir_07_nvt + mp3_file_07_nvt)
    audio = AudioSegment_07_nvt.from_mp3(mp3_file_07_nvt)
    audio.export(wav_file_07_nvt, format="wav")

def speech_to_text_07_nvt(language = "en-US", waiting_time_07_nvt = 1, record_time_07_nvt = 5, is_voice_07_nvt = True):
    recognizer_07_nvt = sr_07_nvt.Recognizer()
    audio_data_07_nvt = None

    if is_voice_07_nvt:
        with sr_07_nvt.Microphone() as source:
            recognizer_07_nvt.adjust_for_ambient_noise(source, duration=waiting_time_07_nvt)
            print("Say something...")
            audio_data_07_nvt = recognizer_07_nvt.record(source, duration=record_time_07_nvt)
    else:
        with sr_07_nvt.AudioFile(wav_file_07_nvt) as source:
            audio_data_07_nvt = recognizer_07_nvt.record(source)

    try:
        text_07_nvt = recognizer_07_nvt.recognize_google(audio_data_07_nvt, language=language)
        return text_07_nvt
    except sr_07_nvt.UnknownValueError:
        print("Can not detect this voice.")
    finally:
        if os_07_nvt.path.exists(wav_file_07_nvt):
            os_07_nvt.remove(wav_file_07_nvt)
    return None

speak_choice_07_nvt("Please choose your origin source")
print("Please choose your origin source")
print("1. File")
print("2. Voice")
origin_input_07_nvt = int(input())
speak_choice_07_nvt("Please choose your language (2 code characters)")
language_07_nvt = input("Please choose your language (2 code characters): ")

result = "You said: "

if origin_input_07_nvt == 1:
    absolute_path = os_07_nvt.path.join(os_07_nvt.getcwd(), parent_dir_07_nvt + "sounds")
    files = [f for f in os_07_nvt.listdir(absolute_path) if os_07_nvt.path.isfile(os_07_nvt.path.join(absolute_path, f))]
    print("Please choose your file you want to process:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    position = int(input())
    
    audio_file_07_nvt = mp3_to_wav_07_nvt("sounds/" + files[position - 1])
    path_file = os_07_nvt.path.abspath(parent_dir_07_nvt + "sounds/" + files[position - 1])
    result += speech_to_text_07_nvt(language=language_07_nvt, is_voice_07_nvt=False)
else:
    waiting_time_07_nvt = int(input("Please input delay time record: "))
    record_time_07_nvt = int(input("Please input listen time: "))
    result += speech_to_text_07_nvt(language=language_07_nvt, waiting_time_07_nvt=waiting_time_07_nvt, record_time_07_nvt=record_time_07_nvt)

print(result)