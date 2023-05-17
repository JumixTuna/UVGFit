
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from firebase_admin import firestore, credentials, initialize_app
import firebaseModule as fb
import time, threading
from PIL import Image, ImageTk, ImageSequence


class app(Tk):
    """docstring for app"""
    def changeWindow(self, which):
        self.transBgImg = PhotoImage(
            file = Path(__file__).parent/"assets\\TransitionBg.png"
        )
        self.transBg = self.canvas.create_image(
            -187.0,
            332.5,
            image=self.transBgImg
        )

        self.transApple = self.canvas.create_image(
            -187.0,
            332.5,
            image = ""
        )
        self.canvas.tk.call("raise", self.canvas._w, None)
        self.appleTrans = Image.open(Path(__file__).parent/"assets\\TransitionApple.gif")
        def playGif():
            for img in ImageSequence.Iterator(self.appleTrans):
                self.img = ImageTk.PhotoImage(img)
                time.sleep(0.00000000001)
                self.canvas.itemconfig(self.transApple, image=self.img)
                print(img)
                self.update()

        gifThread = threading.Thread(target = playGif)
        gifThread.start()

        xa = 374/50
        # self.transApple = self.transCanva.create_image(
        #          187.0,
        #          332.5,
        #          image = ImageTk.PhotoImage(ImageSequence.Iterator(self.appleTrans)[0])
        # )
        for i in range(51):
            self.canvas.move(self.transBg,xa,0)
            self.canvas.move(self.transApple,xa,0)
            self.update()
            time.sleep(0.01)

        for i in range(51):
            self.canvas.move(self.transBg,-xa,0)
            self.canvas.move(self.transApple,-xa,0)
            self.update()
            time.sleep(0.01)
            
        for element in self.trashCan:
            element.destroy()

        self.canvas.delete("all")
        which()
        

    def login(self):
        users_ref = self.db.collection(u'usuarios')
        docs = users_ref.stream()
        reader = []
        for doc in docs:
            reader.append(doc.to_dict())
        print(reader)

        userEmail = self.loginEntry.get()
        userPass = self.passEntry.get()
        userExist = False

        if userEmail and userPass:
            for usuario in reader:
                print(usuario)
                email = usuario["user"]
                passwd = usuario["password"]
                if email == userEmail:
                    userExist = True
                    if passwd == userPass:
                        self.loggedUser = email
                        self.mostrarError("Loggeado con éxito.")
                        self.update()
                    else:
                        self.mostrarError("Usuario o contraseña incorrectos.")
                        self.update()
                        return

            if not userExist:
                fb.agregar(self.db, "usuarios", {"user":userEmail, "password":userPass})
                self.mostrarError("Registrado con éxito.")
                self.loggedUser = userEmail

            self.changeWindow(self.ingresoWindow)
            
        else:
            self.mostrarError("Debe ingresar todos los datos requeridos.")
            self.update()

    def mostrarError(self, errtxt):
        if self.currentError:
            self.canvas.delete(self.currentError)
        self.currentError = self.canvas.create_text(
            187.5,
            550.0,
            anchor="center",
            text=errtxt,
            fill="#000000",
            font=("Inter Extra Bold", 14 * -1)
        )

    def __init__(self):
        super(app, self).__init__()

        #FIREBASE SETUP
        self.cred = credentials.Certificate("uvgfit-firebase-adminsdk-tqdp6-278e47d984.json")
        self.app = initialize_app(self.cred)
        self.db = firestore.client()

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"assets\frame0")

        self.geometry("375x667")
        self.configure(bg = "#FFFFFF")

        self.trashCan = []
        self.loggedUser = None
        self.currentError = None

        self.canvas = Canvas(
            bg = "#FFFFFF",
            height = 667,
            width = 375,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            186.0,
            149.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            190.0,
            240.0,
            anchor="center",
            text="Ingrese su usuario y contraseña",
            fill="#0CB814",
            font=("Inter Extra Bold", 20 * -1)
        )

        self.canvas.create_text(
            13.0,
            519.0,
            anchor="nw",
            text="Recuérdame",
            fill="#000000",
            font=("Inter Extra Bold", 14 * -1)
        )

        self.canvas.create_text(
            13.0,
            311.0,
            anchor="nw",
            text="Usuario",
            fill="#474747",
            font=("Inter Extra Bold", 14 * -1)
        )

        self.canvas.create_text(
            13.0,
            417.0,
            anchor="nw",
            text="Contraseña",
            fill="#474747",
            font=("Inter Extra Bold", 14 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            187.0,
            363.5,
            image=self.entry_image_1
        )
        self.loginEntry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.loginEntry.place(
            x=13.0,
            y=333.0,
            width=348.0,
            height=59.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            187.0,
            469.5,
            image=self.entry_image_2
        )
        self.passEntry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.passEntry.place(
            x=13.0,
            y=439.0,
            width=348.0,
            height=59.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            118.0,
            529.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.login,
            relief="flat"
        )
        self.button_1.place(
            x=112.0,
            y=567.0,
            width=146.0,
            height=53.0
        )

        self.trashCan = [self.button_1, self.passEntry, self.loginEntry]

        self.resizable(False, False)

    ##INGRESO

    def validarIngreso(self):
        nombreIng = self.entry_1.get()
        apellidoIng  = self.entry_2.get()
        edadIng  = self.entry_3.get()
        telefonoIng  = self.entry_4.get()
        pesoIng = self.entry_5.get()
        alturaIng  = self.entry_6.get()
        sexoIng = self.entry_7.get()
        actividadIng = self.entry_8.get()

        fb.agregar(self.db, "infoUsuario", {"nombre":apellidoIng, "apellido": nombreIng, "edad": telefonoIng, "telefono": edadIng, "peso": alturaIng, "altura": pesoIng, "sexo": sexoIng, "actividad": actividadIng})


    def ingresoWindow(self):
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"assets\frame4")
        self.canvas.create_text(
            187.5,
            100.0,
            anchor="center",
            text="Ingrese su información",
            fill="#181A18",
            font=("Inter Extra Bold", 15 * -1)
        )

        self.canvas.create_text(
            20.0,
            151.0,
            anchor="nw",
            text="Nombre",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.canvas.create_text(
            195.0,
            151.0,
            anchor="nw",
            text="Apellido",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            276.0,
            186.47945404052734,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            98.0,
            186.47945404052734,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=196.0, #+4
            y=168.23287963867188,
            width=160.0, #-8
            height=29.49314880371094 #-5
        )
        self.entry_2.place(
            x=18.0,
            y=168.23287963867188,
            width=160.0,
            height=29.49314880371094
        )
        

        self.canvas.create_text(
            20.0,
            151.0,
            anchor="nw",
            text="Nombre",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.canvas.create_text(
            195.0,
            231.0,
            anchor="nw",
            text="Teléfono",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            276.0,
            266.67122650146484,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            98.0,
            266.67122650146484,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=18.0,
            y=248.42465209960938,
            width=160.0,
            height=29.49314880371094
        )
        self.entry_3.place(
            x=196.0,
            y=248.42465209960938,
            width=160.0,
            height=29.49314880371094
        )

        self.canvas.create_text(
            20.0,
            231.0,
            anchor="nw",
            text="Edad",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.canvas.create_text(
            194.0,
            316.0,
            anchor="nw",
            text="Altura (cm)",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            275.0,
            351.7123336791992,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            97.0,
            351.7123336791992,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=17.0,
            y=333.46575927734375,
            width=160.0,
            height=29.49314880371094
        )
        self.entry_5.place(
            x=195.0,
            y=333.46575927734375,
            width=160.0,
            height=29.49314880371094
        )

        self.canvas.create_text(
            19.0,
            316.0,
            anchor="nw",
            text="Peso (kg)",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            98.0,
            434.75341033935547,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            277.0,
            434.24657440185547,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=197.0,
            y=416.0,
            width=160.0,
            height=29.49314880371094
        )
        self.entry_7.place(
            x=18.0,
            y=416.5068359375,
            width=160.0,
            height=29.49314880371094
        )

        self.canvas.create_text(
            20.0,
            399.0,
            anchor="nw",
            text="Sexo",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            185.0,
            518.6027374267578,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=18.0,
            y=489.2054748535156,
            width=334.0,
            height=51.794525146484375
        )

        self.canvas.create_text(
            20.0,
            466.0,
            anchor="nw",
            text="Otros aspectos importantes",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.canvas.create_text(
            197.0,
            399.0,
            anchor="nw",
            text="Actividad Física",
            fill="#474747",
            font=("Inter Extra Bold", 13 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            187.0,
            59.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            187.5,
            55.0,
            anchor="center",
            text="Formulario Inicial",
            fill="#FFFFFF",
            font=("Inter Extra Bold", 28 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.validarIngreso,
            relief="flat",
            bg="white",
            activebackground= "white"
        )
        self.button_1.place(
            x=127.8258056640625,
            y=577.0,
            width=115.01934814453125,
            height=53.3157958984375
        )

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)


app().mainloop()






