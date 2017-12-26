weigth = int()
main_food = ''
main_words = ''


class Farm():
    alive = True  # boolean
    type = 'None'  # bird or animal
    weigth = 0  # kg
    max_weigth = 0  # kg
    main_food = 'None'
    main_words = 'None'
    food = 'None'  # grass or grain or potato

    def feed(self, food):
        if food == main_food:
            if weigth < max_weigth:
                print('Амм-ням-ням..')
                print('..я набираю вес!', main_words)
                self.weigth += 0.5
                print('Мой вес теперь {} кг'.format(weigth), main_words)
            else:
                print('Уже не лезет!.. я и так {} кило!!'.format(weigth), main_words)
        else:
            print('Фууууу!! Я это не ем', main_words)

    def weigh(self):
        print('Я вешу {} кг'.format(weigth))
        print('Мой максимум {} кг'.format(max_weigth), main_words)

    def say(self):
        print(main_words + '..смотрит умными глазами..' + main_words)

    def __init__(self, type, max_weigth, main_food, main_words, weigth):
        self.type = type
        self.max_weigth = max_weigth
        self.main_food = main_food
        self.main_words = main_words
        self.weigth = weigth


class Cow(Farm):
    type = 'animal'
    max_weigth = 450
    main_food = 'grass'
    main_words = 'muuuu..'


class Goat(Farm):
    type = 'animal'
    max_weigth = 23
    main_food = 'grass'
    main_words = 'meeee..'


class Sheep(Farm):
    type = 'animal'
    max_weigth = 25
    main_food = 'grass'
    main_words = 'beeee..'


class Pig(Farm):
    type = 'animal'
    max_weigth = 150
    main_food = 'potato'
    main_words = 'oink-oink..'


class Duck(Farm):
    type = 'bird'
    max_weigth = 6
    main_food = 'grain'
    main_words = 'quack..'


class Chicken(Farm):
    type = 'bird'
    max_weigth = 5
    main_food = 'grain'
    main_words = 'ko-ko-ko..'


class Goose(Farm):
    type = 'bird'
    max_weigth = 7
    main_food = 'grain'
    main_words = 'ga-ga-ga..'


Mashka = Duck('bird', 6, 'grain', 'quack', 3)
Mashka.feed('grain')
Mashka.say()

B = Cow('animal', 300, 'grass', 'moooo', 100)
print(B.weigth)
B.say()

# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:

# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.
