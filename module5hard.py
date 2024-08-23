# Дополнительное практическое задание по модулю: "Классы и объекты."
import time

# Каждый объект класса User должен обладать следующими атрибутами и методами:

class User:
    def __init__(self, nickname : str, password : str, age : int): # создаем пользователя
        self.nickname = nickname # nickname(имя пользователя, строка)
        self.password = password # password(в хэшированном виде, число)
        self.age = age # age(возраст, число)

    def __hash__(self):
        return hash(self.password) # хэшируем пароль

    def __str__(self):
        return f"{self.nickname}" # возвращаем строку с именем

#Каждый объект класса Video должен обладать следующими атрибутами и методами:
class Video:
    def __init__(self, title : str, duration : int, time_now : int = 0, adult_mode : bool = False): # создаем объект видео
        self.title = title # title(заголовок, строка)
        self.duration = int(duration) # duration(продолжительность, секунды)
        self.time_now = int(time_now) # time_now(секунда остановки (изначально 0)
        self.adult_mode = adult_mode # adult_mode(ограничение по возрасту, bool (False по умолчанию)

# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
class UrTube:
    # создаем списки пользователей и видео
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    #Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
    # Если такой пользователь существует, то current_user меняется на найденного.
    # Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname : str, password : str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return   # выход из цикла, когда логин и пароль совпали с введенными
        print("Неверное имя пользователя или пароль") # в случае если цикл отработал, а совпадений не нашлось

    #Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
    # Если существует, выводит на экран: "Пользователь {nickname} уже существует".
    # После регистрации, вход выполняется автоматически.

    def register(self, nickname : str, password : str, age : int):
        for user in self.users:
           if nickname == user.nickname:
               print(f"Пользователь {nickname} уже существует")
               return   # выход из цикла, если такой логин уже есть
        new_user = User(nickname, password, age) # создание нового пользователя в случае, если цикл отработал и логин не найден
        self.users.append(new_user)
        self.log_out()
        self.log_in(new_user.nickname, new_user.password) # вход нового пользователя

    # Метод log_out для сброса текущего пользователя на None.

    def log_out(self):
        self.current_user = None

    #Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует.
    # В противном случае ничего не происходит.

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    # Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
    # Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

    def get_videos(self, search_word : str):
        search_word = search_word.upper() # приводим к одному регистру
        video_list = []
        for video in self.videos:
            if search_word.upper() in video.title.upper(): # сравнение без учета регистра
                video_list.append(video.title)
        return video_list

    #

    def watch_video(self, title : str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = None
        for v in self.videos:
            if v.title == title:
                video = v
                break

        if not video:
            print("Видео не найдено")
            return

        if self.current_user.age < 18 and video.adult_mode == True:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print(f"Воспроизведение видео: {video.title}")
            while video.time_now < video.duration:
                time.sleep(1)
                video.time_now += 1
                print(f"Секунда воспроизведения: {video.time_now}")

            print("Конец видео")


if __name__ == '__main__':

 ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




















