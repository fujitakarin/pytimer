#coding: utf-8

import tkinter as Tk
import time
import tkinter.messagebox as MS
import pygame.mixer as ALM

class Timer(Tk.Frame):
	def __init__(self,master=None):
		Tk.Frame.__init__(self,master)
		ALM.init()

		self.master.title('timer')
		b1=Tk.Button(self,text='1',command=lambda:self.up(0))
		b2=Tk.Button(self,text='2',command=lambda:self.up(1))
		b3=Tk.Button(self,text='3',command=lambda:self.up(3))
		b4=Tk.Button(self,text='4',command=lambda:self.up(4))
		b5=Tk.Button(self,text='スタート',command=self.start)
		b6=Tk.Button(self,text='リセット',command=self.stop)
		self.tokei=Tk.Label(self,text=u'00:00',font=('Arial','100'))

		b1.grid(row=1,column=0,padx=5,pady=0,sticky=Tk.W+Tk.E)
		b2.grid(row=1,column=1,padx=5,pady=0,sticky=Tk.W+Tk.E)
		b3.grid(row=1,column=2,padx=5,pady=0,sticky=Tk.W+Tk.E)
		b4.grid(row=1,column=3,padx=5,pady=0,sticky=Tk.W+Tk.E)
		b5.grid(row=2,column=0,columnspan=2,padx=5,pady=2,sticky=Tk.W+Tk.E)
		b6.grid(row=2,column=2,columnspan=2,padx=5,pady=2,sticky=Tk.W+Tk.E)
		self.tokei.grid(row=0,column=0,columnspan=4,padx=5,pady=0,sticky=Tk.W+Tk.E)

	def start(self):
		self.started=True
		self.kake()
		self.finish=time.time()+self.s3
		self.count()

	def count(self):
		if self.started:
			t=self.finish-time.time()
			if t < 0:
				ALM.music.load("alarm.WAV")#音楽を取り込む
				ALM.music.play(1)#音楽を再生する
				MS.showinfo('タイマー','設定した時間が経過しました')

			else:
				self.tokei.config(text='%02d:%02d'%(t/60,t%60))
				self.after(100,self.count)

	def stop(self):
		self.started=False
		self.tokei.config(text='00:00')
		ALM.music.stop()#音楽を止める

	def kake(self):
		num=self.tokei.cget('text')
		t=num.split(":")#split ()内の文字で文字列を分割する
		second=int(t[1])
		minute=int(t[0])
		self.s3=minute*60+second#秒に直して計算

	def up(self, digit):
		s=self.tokei.cget('text')
		n=int(s[digit])
		n=n+1
		if digit==3 and n>6 or n>9:
			n=0

		if digit==0:
			text=str(n)+s[1:]

		if digit==1:
			text=s[0]+str(n)+s[2:]

		if digit==3:
			text=s[:3]+str(n)+s[4]

		if digit==4:
			text=s[:4]+str(n)

		self.tokei.config(text=text)


if __name__== '__main__':
	f=Timer()
	f.pack()
	f.mainloop()
