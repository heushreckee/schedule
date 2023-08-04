import tkinter as tk
from tkinter import messagebox as m


class tasks_for_the_day:  # класс для каждого дня (позволяет добавлять данные)
    def __init__(self):
        self.infor = []
        self.but = ()

    def days_tasks(self):
        root1 = tk.Tk()
        root1.title('Задачи')
        root1.config(bg='black')
        if not (len(self.infor)):
            tk.Label(root1, height=1, text='Задач на сегодня нет', font=('Verdana', 15, 'normal'), fg='white',
                     bg='black').pack()
        entry1 = tk.Entry(root1)
        entry1.pack(pady=5)

        def check():
            answer = m.askyesno(
                title="Вопрос",
                message="Перенести данные?")
            if answer:
                self.infor.append(entry1.get())
                root1.destroy()
                self.days_tasks()
                #entry1.delete(0, tk.END)

        def delete_info(i):
            answer = m.askyesno(
                title="Вопрос",
                message="Задача выполнена?")
            if answer:
                self.infor.pop(i)
                root1.destroy()
                self.days_tasks()
                #entry1.delete(0, tk.END)

        tk.Button(root1, text='Добавить', command=check, bg='black', fg='white').pack()
        if len(self.infor):
            tk.Label(root1, height=2, text='Задачи:', font=('Verdana', 15, 'normal'), bg='black', fg='white').pack()
            for i in range(len(self.infor)):
                tk.Button(root1, height=1, command= lambda: delete_info(i), text=self.infor[i], bg='black', fg='white').pack() #удаление
                #tk.Label(root1, height=1, text=self.infor[i], bg='black', fg='white').pack()
        root1.mainloop()




