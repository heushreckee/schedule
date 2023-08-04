import tkinter as tk
import calendar
import datetime
import myclasses

root = tk.Tk()  # Класс для графического интерфейса
# root.geometry("461x400")
root.resizable(False, False)
root.title('Расписание')  # Заголовок
days = []  # Тут будут храниться дни
now = datetime.datetime.now()  # текущая дата
year = now.year  # то какой год отображается
month = now.month  # какой месяц отображается


def fill():  # отрисовывает календарь
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day].but['background'] = 'black'
        days[n + week_day].but['text'] = n + 1
        days[n + week_day].but['fg'] = 'white'
        if ((n + week_day - 5) % 7 == 0) or ((n + week_day - 6) % 7 == 0):
            days[n + week_day].but['fg'] = 'lightpink3'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day].but['background'] = 'hotpink4'
    for n in range(week_day):
        days[week_day - n - 1].but['text'] = prew_month_days - n
        days[week_day - n - 1].but['fg'] = 'gray'
        days[week_day - n - 1].but['background'] = 'black'
    for n in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + n].but['text'] = n + 1
        days[week_day + month_days + n].but['fg'] = 'gray'
        days[week_day + month_days + n].but['background'] = 'black'


def prew():  # Перелистывает на предыдущий месяц
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()  # функция отрисовки


def next():  # Перелистывает на следующий месяц
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()


# делаем все необходимые кнопки:
prew_button = tk.Button(root, text='<', command=prew)
prew_button.grid(row=0, column=0, sticky='nsew')
next_button = tk.Button(root, text='>', command=next)
next_button.grid(row=0, column=6, sticky='nsew')
info_label = tk.Label(root, text='0', width=1, height=1,
                      font=('Verdana', 16, 'bold'), fg='black')
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

# заполняем дни
for n in range(5):
    lbl = tk.Label(root, text=calendar.day_abbr[n], width=1, height=1,
                   font=('Verdana', 10, 'normal'), fg='black')
    lbl.grid(row=1, column=n, sticky='nsew')

lbl = tk.Label(root, text=calendar.day_abbr[5], width=1, height=1,
               font=('Verdana', 10, 'normal'), fg='hotpink4')
lbl.grid(row=1, column=5, sticky='nsew')

lbl = tk.Label(root, text=calendar.day_abbr[6], width=1, height=1,
               font=('Verdana', 10, 'normal'), fg='hotpink4')
lbl.grid(row=1, column=6, sticky='nsew')

for row in range(6):
    for col in range(7):
        lbl = myclasses.tasks_for_the_day()
        lbl.but = tk.Button(root, text='0', command=lbl.days_tasks, width=4, height=2,
                            font=('Verdana', 16, 'bold'))
        lbl.but.grid(row=row + 2, column=col, sticky='nsew')
        days.append(lbl)
fill()
root.mainloop()
