from client import Client
from vklad import SuperVklad, CapitalVklad

if __name__ == '__main__':

    ivan = Client('Иван Петров', 500000, 8, 12)
    elena = SuperVklad('Светлана Петрова', 700000, 9, 12)
    ekaterina = SuperVklad('Екатерна Долгова', 550000, 8, 16)
    sergey = CapitalVklad('Сергей Иванов', 690000, 12, 14)

    print(ivan)
    print(ivan.vklad(), '\n')
    print(elena)
    print(elena.vklad(), '\n')
    print(ekaterina)
    print(ekaterina.vklad(), '\n')
    print(sergey)
    print(sergey.vklad(), '\n')