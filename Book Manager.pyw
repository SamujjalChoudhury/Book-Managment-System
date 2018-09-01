import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 12)
xyz = '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
space = '           '
space1 = '                                                                                      '

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        icon = PhotoImage(file='pic.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)
        tk.Tk.wm_title(self, "Book Manager")

        container = tk.Frame(self, width='1366', height='700').grid(row=1, column=1)

        self.frames = {}

        for F in (StartPage, account, issue, reissue, ret):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=1, column=1, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, co):
        frame = self.frames[co]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sel = tk.Frame(self, width=100)
        sel.pack()

        account_B = ttk.Button(sel, text="\n"+space+space+space+space+"Account"+space+space+space+space+"\n", command=lambda: controller.show_frame(account))
        issue_B = ttk.Button(sel, text="\nIssue\n", command=lambda: controller.show_frame(issue))
        return_B = ttk.Button(sel, text="\nReturn\n", command=lambda: controller.show_frame(ret))
        reissue_B = ttk.Button(sel, text="\nRe-Issue\n", command=lambda: controller.show_frame(reissue))
        quit_B = ttk.Button(sel, text="\nQuit\n", command=exit)

        tk.Label(sel, text=" \n\n\n\n").pack()     #Space
        account_B.pack(fill='both', expand=1)

        tk.Label(sel, text=" \n\n").pack()  # Space
        issue_B.pack(fill='both')

        tk.Label(sel, text=" \n\n").pack()  # Space
        return_B.pack(fill='both')

        tk.Label(sel, text=" \n\n").pack()  # Space
        reissue_B.pack(fill='both')

        tk.Label(sel, text=" \n\n").pack()  # Space
        quit_B.pack(fill='both')

class account(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fp = open('info.txt', 'r')
        line = fp.readlines()
        fp.close()
        acc = []
        book = []
        authr = []
        issue = []
        re = []
        j = len(line)
        i = 0
        while i < j:
            acc.append(line[i])
            book.append(line[i + 1])
            authr.append(line[i + 2])
            issue.append(line[i + 3])
            re.append(line[i + 4])
            i += 5

        ttk.Label(self).pack(side='top')
        ttk.Label(self, text="Total Capacity : 14\t\t\tIssued Books : "+ str(available()),font=0).pack(side='top')
        ttk.Label(self, text='\n').pack(side='top')
        Frame(self, width='1366', height='1', bg ='black').place(x=0, y=40)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=41)

        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(self, yscrollcommand=scrollbar.set, bg='grey98', font=1, width=149, height=33)



        for i in range(0,len(acc)):
            mylist.insert(END, '')
            mylist.insert(END, '')
            mylist.insert(END,space+str(i+1)+". "+book[i])
            mylist.insert(END, '')
            mylist.insert(END, space+'   Author : '+authr[i])
            mylist.insert(END,space+ "   Acc No : "+acc[i])
            mylist.insert(END, space+'   Issue Date : '+issue[i] +space+'   Due Date : '+re[i])
            mylist.insert(END,'')
            mylist.insert(END, '')
            mylist.insert(END, xyz)

        mylist.place(x=0, y=41)
        scrollbar.config(command=mylist.yview)


        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')

class issue(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        month = IntVar(self)
        month.set('Select from below')
        mo={1,2,3,4,5,6,7,8,9,10,11,12}

        year = IntVar(self)
        year.set('Select from below')
        yr={2018,2019,2020,2021,2022,2023,2024,2025}

        date = IntVar(self)
        date.set('Select from below')
        da={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}

        acc_no = StringVar(self)
        book_name = StringVar(self)
        author = StringVar(self)

        month.set('Select from below')
        mo={1,2,3,4,5,6,7,8,9,10,11,12}

        year = IntVar(self)
        year.set('Select from below')
        yr={2018,2019,2020,2021,2022,2023,2024,2025}

        date = IntVar(self)
        date.set('Select from below')
        da={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}

        acc_no = StringVar(self)
        book_name = StringVar(self)
        author = StringVar(self)

        space1 = '                                                                                      '

        tk.Label(self, text=" \n\n\n\n\n\n").grid()
        tk.Label(self, text=space1+space1).grid(row=1, column=0)
        tk.Label(self, text=space1+space1).grid(row=3, column=0)
        tk.Label(self, text=space1+space1).grid(row=5, column=0)
        tk.Label(self, text=space1+space1).grid(row=7, column=0)
        tk.Label(self, text=space1+space1).grid(row=8, column=0)
        tk.Label(self, text=space1+space1).grid(row=9, column=0)
        tk.Label(self, text=space1+space1).grid(row=10, column=0)
        tk.Label(self, text=space1+space1).grid(row=12, column=0)

        tk.Label(self, text="ACCESSION NUMBER :").grid(row=1,column=1);tk.Entry(self,insertwidth=1, font= 30, textvariable=acc_no).grid(row=1,column=2)

        tk.Label(self, text=" ").grid(row=2, column=1)
        tk.Label(self, text="BOOK NAME :").grid(row=3, column=1);tk.Entry(self, insertwidth=1, font=30, textvariable=book_name).grid(row=3, column=2)

        tk.Label(self, text="").grid(row=4, column=1)
        tk.Label(self, text="AUTHOR NAME :").grid(row=5, column=1);tk.Entry(self, insertwidth=1, font=30, textvariable=author).grid(row=5, column=2)

        tk.Label(self, text="\n").grid(row=6, column=1)
        tk.Label(self,text='ISSUE DATE :\n', font=20).grid(row=7, column=2)

        tk.Label(self,text='YEAR :').grid(row=8, column=1);ttk.OptionMenu(self, year,'Year',*yr).grid(row=8, column=2)
        tk.Label(self, text='\nMONTH :').grid(row=9, column=1);ttk.OptionMenu(self,month,'Month',*mo).grid(row=9, column=2)
        tk.Label(self,text='\nDATE :').grid(row=10, column=1);ttk.OptionMenu(self,date,'Date',*da).grid(row=10, column=2)



        def ok():
            if available()<14:
                issue_date = datetime.date(year.get(),month.get(),date.get())
                return_date = issue_date + datetime.timedelta(days=121)

                f = open('info.txt', 'a')
                #if self.available() > 0:
                #    f.write('\n')
                f.write(acc_no.get()+'\n')
                f.write(book_name.get()+'\n')
                f.write(author.get()+'\n')
                f.write(str(issue_date) +'\n')
                f.write(str(return_date)+'\n')
                f.close()
                reset()
            else:
                self.popup()
                reset()

        def reset():
            acc_no.set("")
            book_name.set("")
            author.set('')
            month.set('Select from below')
            year.set('Select from below')
            date.set('Select from below')

            controller.show_frame(StartPage)


        tk.Label(self, text="\n").grid(row=11, column=1)
        ttk.Button(self,text=space+'Back'+space, command=lambda:controller.show_frame(StartPage)).grid(row=12, column=1)
        ttk.Button(self, text=space+'Issue'+space, command=ok).grid(row=12, column=2)

        ttk.Label(self, text="Total Capacity : 14\t\t\tIssued Books : " + str(available()), font=0).place(x=480, y=1)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=40)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=41)


    def available(self):
        fp = open('info.txt','r')
        line = fp.readlines()
        acc = []
        book = []
        author = []
        issue = []
        re = []
        j = len(line)
        i = 0
        while i < j:
            acc.append(line[i])
            book.append(line[i+1])
            author.append(line[i+2])
            issue.append(line[i+3])
            re.append(line[i+4])
            i=i+5
        fp.close()
        return j//5


    def popup(self):
        popup = tk.Tk()
        import winsound
        duration = 500
        freq = 1000
        winsound.Beep(freq, duration)

        popup.wm_title("!!! Warning !!!")
        label = ttk.Label(popup, text="Your limit of books is full.", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Ok", command=popup.destroy)
        B1.pack()

        popup.withdraw()
        popup.update_idletasks()  # Update "requested size" from geometry manager

        x = (popup.winfo_screenwidth() - popup.winfo_reqwidth()) / 2
        y = (popup.winfo_screenheight() - popup.winfo_reqheight()) / 2
        popup.geometry("+%d+%d" % (x, y))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        popup.deiconify()

        popup.mainloop()

class reissue(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fp = open('info.txt', 'r')
        line = fp.readlines()
        fp.close()
        acc = []
        authr = []
        issue = []
        re = []
        j = len(line)
        i = 0
        while i < j:
            acc.append(line[i])
            authr.append(line[i + 2])
            issue.append(line[i + 3])
            re.append(line[i + 4])
            i += 5
        book = bookName()

        month = IntVar(self)
        month.set('Select from below')
        mo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

        year = IntVar(self)
        year.set('Select from below')
        yr = {2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025}

        date = IntVar(self)
        date.set('Select from below')
        da = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 31}

        acc_no = StringVar(self)
        book_name = StringVar(self)
        author = StringVar(self)
        book_name.set('Select')

        def detail():
            for i, j in enumerate(bookName()):
                if j == book_name.get():
                    acc_no.set(acc[i])
                    author.set(authr[i])
                    break

        tk.Label(self, text=" \n\n\n\n\n\n").grid()

        tk.Label(self, text=space1 + space1+space).grid(row=1, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=3, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=5, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=7, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=8, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=9, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=10, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=12, column=0)

        tk.Label(self, text="BOOK NAME :").grid(row=1, column=1);ttk.OptionMenu(self, book_name, '', *bookName()).grid(row=1, column=2)
        ttk.Button(self, text='Get Details', command=detail).grid(row=1, column=3)
        tk.Label(self, text=" ").grid(row=2, column=1)
        tk.Label(self, text="ACCESSION NUMBER :").grid(row=3, column=1);ttk.OptionMenu(self, acc_no,'').grid(row=3, column=2)
        tk.Label(self, text="").grid(row=4, column=1)
        tk.Label(self, text="AUTHOR NAME :").grid(row=5, column=1);ttk.OptionMenu(self, author,'').grid(row=5, column=2)

        tk.Label(self, text="\n").grid(row=6, column=1)
        tk.Label(self, text='RE - ISSUE DATE :\n', font=20).grid(row=7, column=2)
        tk.Label(self, text='YEAR :').grid(row=8, column=1);ttk.OptionMenu(self, year, 'Year', *yr).grid(row=8, column=2)
        tk.Label(self, text='\nMONTH :').grid(row=9, column=1);ttk.OptionMenu(self, month, 'Month', *mo).grid(row=9, column=2)
        tk.Label(self, text='\nDATE :').grid(row=10, column=1);ttk.OptionMenu(self, date, 'Date', *da).grid(row=10, column=2)



        def ok():
            issue_date = datetime.date(year.get(), month.get(), date.get())
            return_date = issue_date + datetime.timedelta(days=121)
            for i,j in enumerate(bookName()):
                if j==book_name.get():
                    issue[i]=str(issue_date)+'\n'
                    re[i]=str(return_date)+'\n'
                    break

            del line[:]
            i = 0
            while i < len(acc):
                line.append(acc[i])
                line.append(book[i])
                line.append(authr[i])
                line.append(issue[i])
                line.append(re[i])
                i = i + 1
            fp = open('info.txt', 'w')
            fp.writelines(line)
            fp.close()
            book_name.set('Select')
            acc_no.set('')
            author.set('')
            year.set('Year')
            month.set('Month')
            date.set('Date')
            controller.show_frame(StartPage)

        tk.Label(self, text="\n\n\n\n\n").grid(row=11, column=1)
        ttk.Button(self, text=space+'Back'+space, command=lambda: controller.show_frame(StartPage)).grid(row=12, column=1)
        ttk.Button(self, text=space+'Re-Issue'+space, command=ok).grid(row=12, column=2)

        ttk.Label(self, text="Total Capacity : 14\t\t\tIssued Books : " + str(available()), font=0).place(x=480, y=1)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=40)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=41)

class ret(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fp = open('info.txt', 'r')
        line = fp.readlines()
        fp.close()
        acc = []
        book = []
        authr = []
        issue = []
        re = []
        j = len(line)
        i = 0
        while i < j:
            acc.append(line[i])
            authr.append(line[i + 2])
            issue.append(line[i + 3])
            re.append(line[i + 4])
            i+=5
        book = bookName()

        acc_no = StringVar(self)
        book_name = StringVar(self)
        author = StringVar(self)
        book_name.set('Select')

        def detail():
            for i, j in enumerate(bookName()):
                if j == book_name.get():
                    acc_no.set(acc[i])
                    author.set(authr[i])
                    break

        tk.Label(self, text=" \n\n\n\n\n\n\n\n\n\n").grid()

        tk.Label(self, text=space1 + space1+space).grid(row=1, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=3, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=5, column=0)
        tk.Label(self, text=space1 + space1+space).grid(row=12, column=0)

        tk.Label(self, text="BOOK NAME :").grid(row=1, column=1);ttk.OptionMenu(self, book_name,'',*bookName()).grid(row=1, column=2)
        ttk.Button(self, text='Get Details', command=detail).grid(row=1, column=3)
        tk.Label(self, text=" ").grid(row=2, column=1)
        tk.Label(self, text="ACCESSION NUMBER :").grid(row=3, column=1);ttk.OptionMenu(self, acc_no,'').grid(row=3, column=2)
        tk.Label(self, text="").grid(row=4, column=1)
        tk.Label(self, text="AUTHOR NAME :").grid(row=5, column=1);ttk.OptionMenu(self, author,'').grid(row=5, column=2)

        def ok():
            del line[:]
            i=0
            while i < len(acc):
                if book_name.get()!=book[i]:
                    line.append(acc[i])
                    line.append(book[i])
                    line.append(authr[i])
                    line.append(issue[i])
                    line.append(re[i])
                i=i+1
            fp = open('info.txt','w')
            fp.writelines(line)
            fp.close()
            book_name.set('Select')
            acc_no.set('')
            author.set('')
            controller.show_frame(StartPage)

        tk.Label(self, text="\n\n\n\n\n\n\n").grid(row=11, column=1)
        ttk.Button(self, text=space+'Back'+space, command=lambda: controller.show_frame(StartPage)).grid(row=12, column=1)
        ttk.Button(self, text=space+'Return'+space, command=ok).grid(row=12, column=2)

        ttk.Label(self, text="Total Capacity : 14\t\t\tIssued Books : " + str(available()), font=0).place(x=480, y=1)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=40)
        Frame(self, width='1366', height='1', bg='black').place(x=0, y=41)

    def bookName(self):
        fp = open('info.txt', 'r')
        line = fp.readlines()
        fp.close()
        book = []
        j = len(line)
        i = 0
        while i < j:
            book.append(line[i + 1])
            i += 5
        return book

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


def available():
    fp = open('info.txt','r')
    line = fp.readlines()
    j = len(line)
    fp.close()
    return j//5

def bookName():
    fp = open('info.txt', 'r')
    line = fp.readlines()
    fp.close()
    book = []
    j = len(line)
    i = 0
    while i < j:
        book.append(line[i + 1])
        i += 5
    return book


app = Main()
FullScreenApp(app)
app.mainloop()
