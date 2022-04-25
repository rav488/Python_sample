from tkinter import *

class App(Frame):
	def __init__ (self, master):
		super(App, self).__init__(master)
		self.pack()
		self.create_widget()
	def create_widget(self):
		Label(self, text='Przykładowy text etykiety', width = 20).pack()
		butto1 = Button(self, text='Przykład przycisku')
		button1.pack()

root = Tk()
root.title('Przyklad 1')
root.geometry('300x300')

app = App(root)

root.mainloop()
