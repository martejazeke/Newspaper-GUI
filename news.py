from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("BSU Newsletter")

#window sizes
root.geometry("1240x816")
root.maxsize(width=1240, height=816)

#title label
title = Label(root, text="BAGUMBAYAN NEWSLETTER", font=("Courier", 50, "bold"), padx= "10px", pady= "10px")
title.pack()

#resizing the image
taal = Image.open("taal.jpeg")
resized_taal = taal.resize((500, 300))

#image label
news_img1 = ImageTk.PhotoImage(resized_taal)
news_img_label1 = Label(image=news_img1, borderwidth = 2, relief="solid")
news_img_label1.place(x="5", y="100")

#headline label

headline = Label(root, text="Philippines issues health warning\nas capital hit by smog, \nvolcanic gas", font=("Courier", 25, "bold"), justify="left", padx="5px")
headline.place(x="512", y="100")

#article1 label

article1 = Label(root, text="A small but restive volcano near the Philippine capital Manila spewed\nabove average sulfur dioxide and volcanic smog on Friday, prompting \nauthorities to close schools in dozens of cities and towns and to urge \npeople to stay indoors. The state volcanology and seismology institute \nsaid it observed upwelling of hot volcanic fluids in the Taal volcano's \ncrater lake, resulting in the emission of volcanic gases. Heavy\npollution also shrouded buildings in the capital region in haze. The\nalert remained at level 1 on a five-level scale, denoting a\n'slight increase in volcanic earthquake, and steam or gas activity'.", 
                
                font=("Courier", 13), justify="left", pady="10px", padx="5px")
article1.place(x="512", y="210")

#image2 label

swim = Image.open("swim.jpg")
resized_swim = swim.resize((500, 300))

news_img2 = ImageTk.PhotoImage(resized_swim)
news_img_label2 = Label(image=news_img2, borderwidth= 2, relief="solid")
news_img_label2.place(x="725", y="450")

#headline2 label

headline2 = Label(root, text="PH tankers remain medal-less after\nDay 4 of Asiad swimming", font=("Courier", 25, "bold"), justify="left")
headline2.place(x="5", y="450")

#article2 label

article2 = Label(root, text="Xiandi Chua was the lone Filipino swimmer to advance to the finals of\nthe swimming competitions on Wednesday at the 19th Asian Games in\nHangzhou, China. Chua finished seventh overall in the preliminaries of\nthe women's 400m individual medley with a time of 4:55.83. In the\nfinals at the HOC Aquatic Sports Arena, she finished in seventh place\nafter touching the wall with at time of 4:50.50 -- 15.06 seconds behind\nChina's Yu Yiting who won gold with a time of 4:35.44.",
                 font=("Courier",13), justify="left")
article2.place(x="5", y="530")

article2_1 = Label(root, text="Japan's Tanigawa Ageha took silver (4:35.65), followed by another\nJapanese swimmer in Narita Mio (4:38.77). Kayla Sanchez, Teia Salvino,\nJasmine Alkhaldi and Jarold Hatch missed the finals of their respective\nevents.",
                   font=("Courier",13), justify="left")
article2_1.place(x="5", y="675")

#main program
root.mainloop()