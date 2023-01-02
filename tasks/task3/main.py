# -*- coding: utf-8 -*-


import openpyxl
from rich import print
import matplotlib.pyplot as plt
import eel


def task_3_1(data):
    """ Обрахуємо питомі тепловтрати будівлі маючи звичайні данні та дані із креслення які записані у файлі """
    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    t1 = sheet[5][2].value # Получаємо температуру приміщення
    t2 = sheet[6][2].value # Получаємо температуру ззовні
    T = t1 - t2 # Обчислюємо різницю між зовнішньою і внутрішньо температурою будівлі

    sheet[4][2].value = T # Запишемо значення у файл

    Q = sheet[3][2].value # Получаємо коефіцієнт втрати тепла

    length = sheet[9][2].value # Получаємо довжину будинку
    width = sheet[10][2].value # Получаємо ширину будинку
    height = sheet[11][2].value # Получаємо висоту будинку

    V = length * width * height # Получаємо об'єм приміщення

    sheet[7][2].value = V # Записуємо об'єм приміщення у файл

    q = (Q / V * T) * 10 ** 6 # обраховуємо питомі тепловтрати будівлі
    q = float('{:.2f}'.format(q)) # обрізаємо число на 2 знака після крапки
    

    print(f"[bold blue]питомі тепловтрати будівлі: {q} Вт/м²[/bold blue]")

    sheet[2][2].value = q # Запишемо значення у файл

    """ Обрахуємо загальну площу приміщення маючи дані із Креслення будинку які записані у файлі """

    S = width * height # Обчислюємо загальну площу будинку
    sheet[8][2].value = S # Запишемо значення у файл

    print(f"[bold blue]Загальна площа приміщення: {S} м²[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"питомі тепловтрати будівлі: {q} Вт/м²<br>Загальна площа приміщення: {S} м²"

 
def task_3_2_1(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    N = sheet[13][2].value 
    Q1 = sheet[14][2].value

    Q = N * Q1 # обрвховуємо обсяги споживання води на прийоми душу

    sheet[14][2].value = Q

    print(f"[bold blue]Обсяги споживання води на прийоми душу: {Q} л[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"Обсяги споживання води на прийоми душу: {Q} л"


def task_3_2_2(T):

    data = r"House/data.xlsx"

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    print("[bold yellow]Задаємо температуру води при прийомі душу[/bold yellow]")
    T = int(T)
    #T = int(input("Введіть температуру води: "))

    sheet[16][2].value = T

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його


def task_3_2_3(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    N = sheet[17][2].value
    Q1 = sheet[18][2].value

    Q = N * Q1

    sheet[19][2].value = Q

    print(f"[bold blue]Обсяги споживання води на прийоми ванни: {Q} л[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"Обсяги споживання води на прийоми ванни: {Q} л"


def task_3_2_4(T):

    data = r"House/data.xlsx"

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    print("[bold yellow]Задаємо температуру води при прийомі ванни[/bold yellow]")
    #T = int(input("Введіть температуру води: "))
    T = int(T)

    sheet[20][2].value = T

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його


def task_3_2_5(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    ρ_standart = 998.23
    koeficient = ρ_standart / 60

    ρ_d = koeficient * sheet[16][2].value
    ρ_v = koeficient * sheet[20][2].value

    ρ = ρ_d + ρ_v / 2

    sheet[24][2].value = ρ_d
    sheet[25][2].value = ρ_v

    T_vh = sheet[26][2].value
    T_vuh = sheet[27][2].value

    QT_dysh = sheet[15][2].value * ( (sheet[16][2].value - T_vh) / (T_vuh - T_vh) )
    QT_vanni = sheet[15][2].value * ( (sheet[20][2].value - T_vh) / (T_vuh - T_vh) )
    QT_all = QT_dysh + QT_vanni / ρ

    QT_dysh = float('{:.2f}'.format(QT_dysh))
    QT_vanni = float('{:.2f}'.format(QT_vanni))
    QT_all = float('{:.2f}'.format(QT_all))

    sheet[21][2].value = QT_dysh
    sheet[22][2].value = QT_vanni
    sheet[23][2].value = QT_all
    sheet[24][2].value = ρ_d
    sheet[25][2].value = ρ_v

    print(f"[bold blue]Корегування витрати гарячої води для визначеної температури на виході з бака ГВП:\nДля душу: {QT_dysh} л/добу\nДля ванни: {QT_vanni} л/добу\nЗагальні: {QT_all} м³/добу.[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"Корегування витрати гарячої води для визначеної температури на виході з бака ГВП:<br>Для душу: {QT_dysh} л/добу<br> Для ванни: {QT_vanni} л/добу<br>Загальні: {QT_all} м³/добу."


def task_3_2_6(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    W = 1.163 * sheet[23][2].value * (sheet[29][2].value - sheet[26][2].value)

    W = float('{:.2f}'.format(W))

    sheet[28][2].value = W

    print(f"[bold blue]Енергія необхідна для нагріву води: {W} кВт·год[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"Енергія необхідна для нагріву води: {W} кВт·год"


def task_3_2_7(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    #print("[bold yellow]Введіть час нагрівання бака ГВП (в хвилинах)[/bold yellow]")
    t_nagr = 10

    sheet[31][2].value = t_nagr

    P = sheet[28][2].value / t_nagr

    P = float('{:.2f}'.format(P))

    print(f"[bold blue]Необхідна теплова потужність нагрівача: {P} кВт[/bold blue]")

    sheet[30][2].value = P

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"Необхідна теплова потужність нагрівача: {P} кВт"


def task_3_2(T1, T2):

    data = r"House/data.xlsx"
    t1 = task_3_2_1(data)
    task_3_2_2(T1)
    t2 = task_3_2_3(data)
    task_3_2_4(T2)
    t3 = task_3_2_5(data)
    t4 = task_3_2_6(data)
    t5 = task_3_2_7(data)

    return f"{t1}<br>{t2}<br>{t3}<br>{t4}<br>{t5}"


def task_3_3(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    q = sheet[2][2].value
    T = sheet[6][2].value
    S = sheet[8][2].value

    Q = q * T * S
    Q = Q / 10 ** 6
    Q = float('{:.2f}'.format(Q))

    sheet[32][2].value = Q

    print(f"[bold blue]потужність тепловтрат будівлі: {Q} кВт[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"потужність тепловтрат будівлі: {Q} кВт"


def task_3_4(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    x = [sheet[6][2].value, sheet[5][2].value]
    y = [sheet[32][2].value, 0]

    f = plt.figure() # Створюємо нову фігуру
    #f.set_size_inches(30, 40) # Задаємо розміри
    plt.plot(x, y) # Додаємо дані для лінійного графіка
    plt.title("Залежність тепловтрат будівлі від температурних умов") # Назва графіка
    plt.xlabel("Температура Т (°C)") # Назва осі Х
    plt.ylabel("потужність тепловтрат Q (кВт)") # назва осі У
    #plt.show() # демонструємо графік
    f.savefig(r"report/task_3-4_plot.pdf") # Зберігаємо графік у пдф за шляхом
    f.savefig(r"report/task_3-4_plot.png")
    f.savefig(r"web/img/task_3-4_plot.png")


def task_3_5(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку

    W = sheet[32][2].value * sheet[4][2].value
    W = float('{:.2f}'.format(W))

    sheet[33][2].value = W

    print(f"[bold blue]витрати енергії на опалення за визначений період: {W} кВт[/bold blue]")

    book.save(data) # Зберігаємо файл
    book.close() # Завершуємо роботу з файлом та закриваємо його

    return f"витрати енергії на опалення за визначений період: {W} кВт"


def task_3_6_and_3_7(data):

    book = openpyxl.open(data) # Відкриваємо Excel файл тільки для читання
    sheet = book.active # вибираємо сторінку
    """ Розрахуємо коефіцієнти (ціна в грн за 1 кВт) """
    k1 = sheet[34][2].value / sheet[35][2].value
    k2 = sheet[36][2].value / sheet[37][2].value
    k3 = sheet[38][2].value / sheet[39][2].value
    k4 = sheet[40][2].value / sheet[41][2].value
    k5 = sheet[42][2].value / sheet[43][2].value
    k6 = sheet[44][2].value / sheet[45][2].value

    Q = sheet[33][2].value
    """ Розрахуємо вартості на опалення вряховуючи пораховані коефіцієнти за 1кВт та кількість споживання """
    v1 = k1 * Q
    v2 = k2 * Q
    v3 = k3 * Q
    v4 = k4 * Q
    v5 = k5 * Q
    v6 = k6 * Q
    """ Побудуємо стовбцеву діаграму із вартістю опалення на місяць і наглядно побачимо який спосіб найдешевший """

    """ 
    Способи опалення за методичкою:
    1. Теплозабезпечення від централізованої мережі;
    2. Автономного теплозабезпечення від газового котла;
    3. Автономного теплозабезпечення від вугільного котла;
    4. Автономного теплозабезпечення від дров’яного котла;
    5. Автономного теплозабезпечення від котла, що працює на деревних пелетах;
    6. Автономного теплозабезпечення від електричного котла.
    """
    x = list(range(1,7)) # кількість та послідовність способів за методичкою (наведено зверху)
    y = [v1, v2, v3, v4, v5, v6] # вартість цього способу

    fig, ax = plt.subplots()

    ax.bar(x, y) # створюємо стовпцеву діаграму
    plt.title("Діаграма вартості опалення")
    plt.xlabel("Способи опалення (по послідовності методички)")
    plt.ylabel("вартість (грн/міс)")
    ax.set_facecolor("seashell")
    fig.set_facecolor("floralwhite")
    #fig.set_figwidth(len(values)) # Задаємо розміри діаграми за кількістю даних
    #fig.set_figheight(len(numbers))
    fig.savefig(r"report/task_3-7_plot.pdf")
    fig.savefig(r"report/task_3-7_plot.png")
    fig.savefig(r"web/img/task_3-7_plot.png")

    #plt.show()


@eel.expose
def main(T1, T2):

    data = r"House/data.xlsx"
    t1 = task_3_1(data)
    t2 = task_3_2(T1, T2)
    t3 = task_3_3(data)
    task_3_4(data)
    t4 = task_3_5(data)
    task_3_6_and_3_7(data)

    return f"{t1}<br>{t2}<br>{t3}<br>{t4}"


if __name__ == "__main__":

    #main()
    eel.init("web")

    eel.start("main.html", size = (700, 700))