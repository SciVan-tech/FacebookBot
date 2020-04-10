from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def login(self):
       # driver.get("http://www.python.org")
        bot = self.bot
        bot.get('https://www.facebook.com/')cd ..
        time.sleep(3)
        email= bot.find_element_by_name('email')
        password = bot.find_element_by_name('pass')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)


    def like(self,hashtag):
        bot = self.bot
        #bot.get('https://www.facebook.com/search/top/?q='+ hashtag +'&epa=SEARCH_BOX')
        bot.get('https://www.facebook.com/search/pages/?q=' +
                hashtag + '&epa=SERP_TAB')
        time.sleep(3)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            pages = bot.find_elements_by_class_name('_32mo')
            links = [elem.get_attribute('href') for elem in pages]
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_class_name('likeButton._4jy0._4jy4._517h._51sy._42ft').click()
                    time.sleep(1)
                    bot.find_element_by_class_name('_55pe').click()
                    time.sleep(1)
                except Exception as ex:
                    time.sleep(3)

# ed = TwitterBot('scivan.science@gmail.com', 'KKK999KKK')
# ed.login()
# ed.like('science')


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='e-mail')
        self.lbl2 = Label(win, text='password')
        self.lbl3 = Label(win, text='Search word')
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn1 = Button(win, text='Submit')
        self.btn2 = Button(win, text='Quit')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='Submit', bd=1, fg="green", command=self.Submit)
        self.b1.place(x=200, y=200)
        self.b2 = Button(win, text='Quit', bd=1,fg="red", command=quit)
        self.b2.place(x=250, y=200)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)

    def Submit(self):
        email = str(self.t1.get())
        password = str(self.t2.get())
        word = str(self.t3.get())
        Bot = TwitterBot(email, password)
        Bot.login()
        Bot.like(word)


window = Tk()
mywin = MyWindow(window)
window.title('SciVan Facebook Bot')
window.geometry("400x300")
window.mainloop()