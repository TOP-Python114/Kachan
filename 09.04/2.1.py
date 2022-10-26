#Разработайте класс FilmCard, который описывает карточку с информацией о фильме в каталоге онлайн-кинотеатра.
#Используйте композицию для создания возможной связи с другими фильмами.
#Около десяти полей у вас должно быть.
#Реализуйте шаблон Фабрики для создания экземпляров FilmCard.

from enum import Enum


class Genre(int, Enum):
    Romance = 1
    Crime = 2
    Drama = 3
    History = 4
    Mystery = 5
    Adventure = 5
    Horror = 6
    Comedy = 7
    Family = 8
    War = 9
    Fantasy = 10


class Actor:

    def __init__(self, role: str, fio: str ):
        self.films = {}
        self.fio = fio
        self.role = role

    def to_create(self) -> dict:
        """
        Создает словарь с ролью и именем актера
        :param name: наименование фильма
        :param role: роль актера
        """
        self.films.update({self.role:self.name})
        return self.films

    @property
    def name(self):
        return self.fio


class FilmCard:

    def __init__(self,
                 id_: int,
                 name: str,
                 genre: str,
                 year: str,
                 duration: int,
                 country: str,
                 actor: Actor,
                 reviews_from_users: int,
                 reviews_from_critics: int,
                 title: str
                 ):
        self.id = id_
        self.name = name
        self.genre = genre.name
        self.year = year
        self.duration = duration
        self.country = country
        self.reviews_from_users = reviews_from_users
        self.reviews_from_critics = reviews_from_critics
        self.title = title
        self.actor = actor

    def __str__(self):
        return f'Фильм: {self.name}\n\tID: {self.id}\n\tЖанр: {self.genre} \n\tГод: {self.year} \n\tПродолжительность: {self.duration} ' \
               f'\n\tСтрана производства: {self.country}\n\tАктеры: {self.actor}\n\tОценка зрителей: {self.reviews_from_users}'\
               f'\n\tОценка Критиков: {self.reviews_from_critics}\n\tСлоган: {self.title}'

    @property
    def name_film(self):
        return self.name

    @property
    def name_actor(self):
        return self.actor


class FilmCardFactory:

    """Создаёт и нумерует экземпляры FilmCard, используя объект класса."""
    id_ = 0
    dict_films = {}

    @classmethod
    def add_film(cls,
                 name: str,
                 genre: Genre,
                 year: str,
                 duration: int,
                 country: str,
                 actor,
                 reviews_from_users: int,
                 reviews_from_critics: int,
                 title: str
                 ):

        """
        Добавляет информацию о фильме и присваивает индекс
        :param name: наименование фильма
        :param genre: жанр
        :param year: год выпуска
        :param duration: продолжительность
        :param country: страна
        :param actor: актер\актеры
        :param reviews_from_users: оценка зрителей
        :param reviews_from_critics: оценка критиков
        :param title: слоган
        """
        cls.id_ += 1
        if name in cls.dict_films.values():
            raise ValueError(f'Add another movie, this one already exists')
        else:
            cls.dict_films.update({cls.id_: name})
        return FilmCard(cls.id_,
                        name,
                        genre,
                        year,
                        duration,
                        country,
                        actor,
                        reviews_from_users,
                        reviews_from_critics,
                        title
                        )


class CardIndex:

    list = []
    @classmethod
    def add_films(cls, film: FilmCard):
        """
        Создает общую картотеку фильмов
        :param: film: объект фильма
        """
        cls.list.append(film)
        return cls.list


class FilmCardSearch:

    @staticmethod
    def search(film: list, actor: str):
        """
        Осуществляет поиск фильмов, в которых снимался актер
        :param film: наименование фильма
        :param actor: имя актера
        """
        result = []
        for elem in film:
            for i in elem.name_actor:
                if i == actor:
                    result.append(elem.name_film)

        return f'Результат поиска: {result}'


actor1 = Actor('Джейк','Джейк Джилленхол').name
actor2 = Actor('Джейн','Эмми Россам').name

film = FilmCardFactory()
film1 = film.add_film('Послезавтра', Genre(10), 2004, 90, 'USA', [actor1, actor2], 7.7, 6.4,'Где будешь ты?')
print(film1)
print('___________________________________________________')

actor3 = Actor('Питер','Джейк Джилленхол').name
actor4 = Actor('Джесика','Дэвид Шайр').name

film2 = film.add_film('Зодиак', Genre(3), 2007, 90, 'USA', [actor3, actor4], 6.5, 5.0,'Есть много способов умереть от руки убийцы')
print(film2)
print('___________________________________________________')

actor5 = Actor('Эдвард Льюис','Ричард Гир').name
actor6 = Actor('Вивиан Уорд','Джулия Робертс').name

film3 = film.add_film('Красотка', Genre(1), 1990, 90, 'USA', [actor5, actor6], 8.5, 8.0,'She walked off the street, into his life and stole his heart')
print(film3)
print('___________________________________________________')


card = CardIndex()
card.add_films(film1)
card.add_films(film2)
card_film = card.add_films(film3)
print(FilmCardSearch.search(card_film,'Джейк Джилленхол'))

# Фильм: Послезавтра
# 	ID: 1
# 	Жанр: Fantasy
# 	Год: 2004
# 	Продолжительность: 90
# 	Страна производства: USA
# 	Актеры: ['Джейк Джилленхол', 'Эмми Россам']
# 	Оценка зрителей: 7.7
# 	Оценка Критиков: 6.4
# 	Слоган: Где будешь ты?
# ___________________________________________________
# Фильм: Зодиак
# 	ID: 2
# 	Жанр: Drama
# 	Год: 2007
# 	Продолжительность: 90
# 	Страна производства: USA
# 	Актеры: ['Джейк Джилленхол', 'Дэвид Шайр']
# 	Оценка зрителей: 6.5
# 	Оценка Критиков: 5.0
# 	Слоган: Есть много способов умереть от руки убийцы
# ___________________________________________________
# Фильм: Красотка
# 	ID: 3
# 	Жанр: Romance
# 	Год: 1990
# 	Продолжительность: 90
# 	Страна производства: USA
# 	Актеры: ['Ричард Гир', 'Джулия Робертс']
# 	Оценка зрителей: 8.5
# 	Оценка Критиков: 8.0
# 	Слоган: She walked off the street, into his life and stole his heart
# ___________________________________________________
# Результат поиска: ['Послезавтра', 'Зодиак']