# from gpiozero import Button as btn

# import requests

# from time import sleep
# from signal import pause

# class Avion : 
#     def __init__(self, root):
#         self.__root = root
#         self.__alt = 0
#         self.__ort = 0
#         self.__altPlus = btn(16)
#         self.__altPlus.when_pressed = self.AltitudePlus
#         self.__altMoins = btn(17)
#         self.__altMoins.when_pressed = self.AltitudeMoins
#         self.__ortPlus= btn(22)
#         self.__ortPlus.when_pressed = self.OrientPlus
#         self.__ortMoins= btn(6)
#         self.__ortMoins.when_pressed = self.OrientMoins
#         self.__reset = btn(12)
#         self.__reset.when_pressed = self.Reset
#         self.__envoyer = btn(5)
#         self.__envoyer.when_pressed = self.Envoyer


#     def AltitudePlus(self):
#         self.__alt += 10
    
#     def AltitudeMoins(self):
#         self.__alt -= 10

#     def OrientPlus(self):
#         self.__ort += 10

#     def OrientMoins(self):
#         self.__ort -= 10

#     def Reset(self):
#         self.__alt = 0
#         self.__ort = 0

#     def Envoyer(self):
#         try:
#             response = requests.post("http://localhost:5000/api/avion", json={"altitude":self.__alt, "orientation" : self.__ort})
#             if response.status_code == 200:
#                 print("donnees envoyees avec succes")
#         except Exception as e:
#             print("Erreur lors de l'envoi des donness")

from gpiozero import Button as btn
import requests
from time import sleep
from signal import pause

class Avion:
    def __init__(self, root):
        self.__root = root
        self.__alt = 0
        self.__ort = 0
        self.__altPlus = btn(16)
        self.__altPlus.when_pressed = self.AltitudePlus
        self.__altMoins = btn(17)
        self.__altMoins.when_pressed = self.AltitudeMoins
        self.__ortPlus = btn(22)
        self.__ortPlus.when_pressed = self.OrientPlus
        self.__ortMoins = btn(6)
        self.__ortMoins.when_pressed = self.OrientMoins
        self.__reset = btn(12)
        self.__reset.when_pressed = self.Reset
        self.__envoyer = btn(5)
        self.__envoyer.when_pressed = self.Envoyer

    def AltitudePlus(self):
        self.__alt += 10
        print(f"Altitude increased to {self.__alt}")

    def AltitudeMoins(self):
        self.__alt -= 10
        print(f"Altitude decreased to {self.__alt}")

    def OrientPlus(self):
        self.__ort += 10
        print(f"Orientation increased to {self.__ort}")

    def OrientMoins(self):
        self.__ort -= 10
        print(f"Orientation decreased to {self.__ort}")

    def Reset(self):
        self.__alt = 0
        self.__ort = 0
        print("Altitude and Orientation reset")

    def Envoyer(self):
        try:
            response = requests.post("http://localhost:5000/api/avion", json={"altitude": self.__alt, "orientation": self.__ort})
            if response.status_code == 200:
                print("Données envoyées avec succès")
            else:
                print(f"Erreur avec le statut {response.status_code}")
        except Exception as e:
            print(f"Erreur lors de l'envoi des données: {e}")

pause()