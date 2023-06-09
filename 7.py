import os
from pathlib import Path
import subprocess
import re
import shutil

def make_mix(source, destination='', count=0, frame = 10, log=False, extended = False):
    out = open('log.txt', 'w') #Открываем файл для сохранения логов выполнения
    files = list(Path(source).glob("*.mp3")) #Собираем список файлов
    if destination == '': #Если destination не указан
        destination = source #Используем директорию source
    if count == 0: #Если кол-во файлов не указано
        count = len(files) #Используем все файлы

    #Создание фрагментов отдельных файлов
    if not(Path(source+r"\tmp").exists()): #Все фрагменты будем заносить в папку tmp
        os.mkdir(source + r"\tmp")
    for index in range(count):
        command = 'ffprobe.exe -i "'+str(files[index])+'" -hide_banner' #Задаем команду на получение длитеьлности файла
        text = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #Читаем вывод
        text = text.stdout.read().decode('cp866') #Декодируем вывод
        duration = re.compile('\d\d:\d\d:\d\d.\d\d').search(text).group() #Получаем строку Duration: 'время'
        minutes = int(duration.split(':')[1]) #Получаем количество полных минут длительности
        seconds = round(float(duration.split(':')[2])) #Получаем количество секунд длительности
        time = minutes*60+seconds #Вычисляем длительность в секундах
        time = round(time/100*20) #Считаем 20% от длительности, с этой секунды будет начинаться трек
        if extended == True:
            command = 'ffmpeg.exe -ss '+str(time)+' -t '+str(frame)+' -i "' +\
                      str(files[index])+'" -filter:a "afade=in:st=0:d=2, afade=out:st='+str(frame-2) +\
                      ':d=2" -y "tmp\mix'+str(index)+'.mp3"' #Это команда с добавлением fade in/out эффекта
        else:
            command = 'ffmpeg.exe -ss ' + str(time) + ' -t ' + str(frame) + ' -i "' + \
                      str(files[index]) + '" -y "tmp\mix' +\
                      str(index) + '.mp3"'  # Это команда без добавления fade in/out эффекта
        if log==True: #Если log - True выводим логи
            print('---processing file '+str(index)+': '+str(os.path.split(files[index])[-1]))
        subprocess.Popen(command, stdout=out, stderr=out)#Выполняем команду, в папке destination появится файл mix.mp3
    os.chdir(source+os.sep+r'\tmp')#Переход в папку с миксами
    files = os.listdir(os.getcwd()) #Получаем список миксов
    command = 'ffmpeg -i "concat:'+'|'.join(files)+'" -c copy output.mp3' #Формируем команду для объединения файлов
    subprocess.Popen(command, stdout=out, stderr=out) #Выполняем команду
    out.close() #Закрываем файл сохранения логов


make_mix(os.getcwd())