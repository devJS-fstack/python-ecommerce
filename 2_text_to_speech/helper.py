from gtts import gTTS as gTTS_07_nvt
import playsound as playsound_07_nvt
import datetime as datetime_07_nvt
import os as os_07_nvt
from googletrans import Translator as Translator_07_nvt
from pydub import AudioSegment as AudioSegment_07_nvt
import speech_recognition as sr_07_nvt


format_datetime_07_nvt = "%Y%m%d%H%M%S"
parent_dir_07_nvt = "2_text_to_speech/"
wav_file_07_nvt = "temp.wav"


class Helper:
    def preprocess_file_07_nvt(self, filename_07_nvt):
        filename_arr_07_nvt = filename_07_nvt.split(".")
        if filename_arr_07_nvt[-1] != "mp3":
            filename_07_nvt += ".mp3"
        absolute_path_07_nvt = os_07_nvt.path.join(
            os_07_nvt.getcwd(), parent_dir_07_nvt + "sounds")
        files_07_nvt = [f for f in os_07_nvt.listdir(absolute_path_07_nvt) if os_07_nvt.path.isfile(
            os_07_nvt.path.join(absolute_path_07_nvt, f))]
        if filename_07_nvt in files_07_nvt:
            print("File already existed. Please choose action..")
            print("1. Replace old file")
            print("2. Automatic rename new file")
            print("3. Automatic rename old file")
            action_07_nvt = int(input("Your choice: "))
            if action_07_nvt == 1:
                return filename_07_nvt
            elif action_07_nvt == 2:
                return filename_07_nvt.replace(".mp3", "") + "_" + datetime_07_nvt.datetime.now().strftime(format_datetime_07_nvt) + ".mp3"
            else:
                new_filename_07_nvt = filename_07_nvt.replace(
                    ".mp3", "") + "_" + datetime_07_nvt.datetime.now().strftime(format_datetime_07_nvt) + ".mp3"
                old_file_path_07_nvt = os_07_nvt.path.join(
                    absolute_path_07_nvt, filename_07_nvt)
                new_file_path_07_nvt = os_07_nvt.path.join(
                    absolute_path_07_nvt, new_filename_07_nvt)
                os_07_nvt.rename(old_file_path_07_nvt, new_file_path_07_nvt)
                print(
                    f"Old file '{filename_07_nvt}' has been renamed to '{new_filename_07_nvt}'")
                return filename_07_nvt
        else:
            return filename_07_nvt

    def translate_text_07_nvt(self, text_07_nvt, input_lang_07_nvt, output_lang_07_nvt):
        translator_07_nvt = Translator_07_nvt()
        translated_07_nvt = translator_07_nvt.translate(
            text_07_nvt, src=input_lang_07_nvt, dest=output_lang_07_nvt)
        return translated_07_nvt.text

    def speak_07_nvt(self, text_07_nvt, filename_07_nvt, input_lang_07_nvt, output_lang_07_nvt):
        script_directory_07_nvt = os_07_nvt.path.dirname(
            os_07_nvt.path.abspath(__file__))
        filename_07_nvt = self.preprocess_file_07_nvt(filename_07_nvt)
        print("Your file name is saving:", filename_07_nvt)
        filename_07_nvt = os_07_nvt.path.join(
            script_directory_07_nvt, "sounds/" + filename_07_nvt)
        text_07_nvt = self.translate_text_07_nvt(
            text_07_nvt, input_lang_07_nvt, output_lang_07_nvt)
        tts_07_nvt = gTTS_07_nvt(text=text_07_nvt, lang=output_lang_07_nvt)
        tts_07_nvt.save(filename_07_nvt)
        playsound_07_nvt.playsound(filename_07_nvt)


def mp3_to_wav_07_nvt(filename):
    audio = AudioSegment_07_nvt.from_mp3(filename)
    audio.export(wav_file_07_nvt, format="wav")


def speech_to_text_07_nvt(language, filename):
    mp3_to_wav_07_nvt(filename)
    recognizer_07_nvt = sr_07_nvt.Recognizer()

    with sr_07_nvt.AudioFile(wav_file_07_nvt) as source:
        audio_data_07_nvt = recognizer_07_nvt.record(source)

    try:
        text_07_nvt = recognizer_07_nvt.recognize_google(
            audio_data_07_nvt, language=language)
        return text_07_nvt
    except sr_07_nvt.UnknownValueError:
        print("Can not detect this voice.")
    finally:
        if os_07_nvt.path.exists(wav_file_07_nvt):
            os_07_nvt.remove(wav_file_07_nvt)
    return None


Helper().translate_text_07_nvt("how are you", "en", "vi")
