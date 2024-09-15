import tkinter as tk

root=tk.Tk()

#이름 변경
root.title('코로나 진단키트 예측도 계산 프로그램')

#창 크기 변경
root.geometry('600x400+100+200')

#함수
def make_lab14():
    lab14.configure(text=ent12.get())

def make_lab24():
    lab24.configure(text=ent22.get())

def make_lab34():
    lab34.configure(text=ent32.get())

def make_PPV_NPV():
    Sen=float(lab14.cget("text"))/100
    Spe=float(lab24.cget("text"))/100
    P_R=float(lab34.cget("text"))/100

    PPV=round((P_R*Sen)/(P_R*Sen+(1-P_R)*(1-Spe))*100,2)
    NPV=round(((1-P_R)*Spe)/((1-P_R)*Spe + P_R*(1-Sen))*100,2)

    lab52.configure(text=PPV)
    lab62.configure(text=NPV)

#1행라벨
lab11=tk.Label(
    root,text='민감도',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )

lab11.grid(row=1,column=1,padx=5,pady=10)

#Entry는 height 속성 없음 
ent12=tk.Entry(
    bg='white',
    width=8,font=('맑은 고딕',16,'bold'),
)

ent12.grid(row=1,column=2,padx=5,pady=10)

button13=tk.Button(
    root,
    text='\u2192',
    width=8,font=('맑은 고딕',11,'bold'),
    bg='red',
    fg='white',
    height=1,
    command=make_lab14
)

button13.grid(row=1, column=3,padx=5,pady=10)

lab14=tk.Label(
    root,text='',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )
lab14.grid(row=1,column=4,padx=5,pady=10)

#2행라벨
lab21=tk.Label(
    root,text='특이도',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )

lab21.grid(row=2,column=1,padx=5,pady=10)

#Entry는 height 속성 없음 
ent22=tk.Entry(
    bg='white',
    width=8,font=('맑은 고딕',16,'bold'),
)

ent22.grid(row=2,column=2,padx=5,pady=10)

button23=tk.Button(
    root,
    text='\u2192',
    width=8,font=('맑은 고딕',11,'bold'),
    bg='red',
    fg='white',
    height=1,
    command=make_lab24
)

button23.grid(row=2, column=3,padx=5,pady=10)

lab24=tk.Label(
    root,text='',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )
lab24.grid(row=2,column=4,padx=5,pady=10)

#3행라벨
lab31=tk.Label(
    root,text='발생률',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )

lab31.grid(row=3,column=1,padx=5,pady=10)

#Entry는 height 속성 없음 
ent32=tk.Entry(
    bg='white',
    width=8,font=('맑은 고딕',16,'bold'),
)

ent32.grid(row=3,column=2,padx=5,pady=10)

button33=tk.Button(
    root,
    text='\u2192',
    width=8,font=('맑은 고딕',11,'bold'),
    bg='red',
    fg='white',
    height=1,
    command=make_lab34
)

button33.grid(row=3, column=3,padx=5,pady=10)

lab34=tk.Label(
    root,text='',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )
lab34.grid(row=3,column=4,padx=5,pady=10)

#4행 라벨
button41=tk.Button(
    root,
    text='결과 계산하기(click)',
    width=8,font=('맑은 고딕',16,'bold'),
    bg='red',
    fg='white',
    height=1,
    command=make_PPV_NPV
)

button41.grid(row=4, column=1,padx=5,pady=10, columnspan=4, sticky='we')

#5행 라벨
lab51=tk.Label(
    root,text='양성 예측도(양성인데 진짜 걸림)',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )

lab51.grid(row=5,column=1,padx=5,pady=10, columnspan=3, sticky='we')

lab52=tk.Label(
    root,text='',
               bg='yellow',fg='black',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )
lab52.grid(row=5,column=4,padx=5,pady=10)

#6행 라벨
lab61=tk.Label(
    root,text='음성 예측도(음성인데 진짜 안걸림)',
               bg='#2F5597',fg='white',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )

lab61.grid(row=6,column=1,padx=5,pady=10, columnspan=3, sticky='we')

lab62=tk.Label(
    root,text='',
               bg='yellow',fg='black',
               width=8,height=1,
               font=('맑은 고딕',16,'bold'),
    )
lab62.grid(row=6,column=4,padx=5,pady=10)
root.mainloop()