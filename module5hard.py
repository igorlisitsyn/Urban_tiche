import time



user_name = None

class User:
    def __init__(self, nickname=None, password=None, age = None):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


    # def __repr__(self):
    #     pass



class Video:
    def __init__(self, title, duration = 0, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []

    videos = []
    seach_video = []
    current_user = []

    def __repr__(self):
        if len(self.current_user) != 0:
            return f'Пользователь {self.current_user[0]} уже существует'

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            self.users.append(User(nickname, password, age))
            self.current_user.append(nickname)
            self.current_user.append(age)
            return

        for name in self.users:
            if nickname == name.nickname:
                # print(f" Такой пользователь {self.nickname} уже существует")
                self.log_out()
                self.current_user.append(name.nickname)
                self.current_user.append(name.age)
            else:
                self.users.append(User(nickname, password, age))
                self.log_out()
                self.current_user.append(name.nickname)
                self.current_user.append(name.age)

    def log_in(self, nickname, password):
        for name in self.users:
            if nickname == name.nickname and hash(password) == name.password:
                self.current_user.append(name.nickname)
                self.current_user.append(name.age)
            else:
                self.log_out()
            return self.current_user

    def log_out(self):
        self.current_user.clear()

    def add(self, *args):
        for film in args:
            if film.title not in self.videos:
                self.videos.append(film)

    def get_videos(self, search):
        self.seach_video = []
        for film in self.videos:
            if search.lower() in film.title.lower():
                self.seach_video.append(film.title)
        return f'{self.seach_video}'



    def watch_video(self, video_name):
        self.key = False
        if len(self.current_user) == 0:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for film in self.videos:
            if film.title == video_name:


                if self.current_user[1] < 18 and film.adult_mode is True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    self.log_out()

                    return
                else:
                    self.key = True
                    for i in range(1, film.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)

                    print('Конец видео ')

        if not self.key:
            print('urban_pythonist')



ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur)
ur.watch_video('Лучший язык программирования 2024 года!')


