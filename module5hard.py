import time



user_name = None

class User:
    def __init__(self, nickname=None, password=None, age = None):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.current_user = None

    def __repr__(self):
        pass



class Video:
    def __init__(self, title, duration = 0, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube(User):
    users = {}

    videos = []
    seach_video = []


    def __repr__(self):
        if self.current_user is not None:
            return f'Пользователь {self.current_user} уже существует'

    def register(self, nickname, password, age):
        super().__init__(nickname, password, age)
        # self.nickname = nickname
        # self.password = password
        # self.age = age
        # self.current_user = None
        self.test = 'jfsjlfksfjsjflskf'
        if nickname in self.users:
            # print(f" Такой пользователь {self.nickname} уже существует")
            self.current_user = nickname
        else:
            self.users[nickname] = [self.password, self.age]
            self.current_user = nickname

    def log_in(self, nickname, password,):
        if nickname in self.users and hash(password) == hash(self.users[nickname][0]):
            self.current_user = nickname
        else:
            self.current_user = None
        return self.current_user

    def log_out(self):
        self.current_user = None

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
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for film in self.videos:
            if film.title == video_name:

                if self.users[self.current_user][1] < 18 and film.adult_mode is True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
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


