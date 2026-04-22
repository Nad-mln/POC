import tkinter as tk
from tkinter import messagebox
import requests

API_BASE_URL = "http://localhost:5000/api/avion"


class AirplaneTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contrôle avion - Tkinter")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.altitude_var = tk.StringVar(value="1000")
        self.orientation_var = tk.StringVar(value="90")
        self.status_var = tk.StringVar(value="Prêt")

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Pilotage de l'avion",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Altitude :").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(form_frame, textvariable=self.altitude_var, width=20).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Orientation :").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(form_frame, textvariable=self.orientation_var, width=20).grid(row=1, column=1, padx=10, pady=10)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=15)

        tk.Button(
            buttons_frame,
            text="Envoyer en POST",
            width=18,
            command=self.send_post
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            buttons_frame,
            text="Envoyer en GET",
            width=18,
            command=self.send_get
        ).grid(row=0, column=1, padx=10, pady=10)

        gpio_frame = tk.LabelFrame(self.root, text="Simulation boutons GPIO", padx=15, pady=15)
        gpio_frame.pack(pady=20)

        tk.Button(gpio_frame, text="Altitude +100", width=18, command=self.altitude_up).grid(row=0, column=0, padx=10, pady=8)
        tk.Button(gpio_frame, text="Altitude -100", width=18, command=self.altitude_down).grid(row=0, column=1, padx=10, pady=8)
        tk.Button(gpio_frame, text="Orientation -10", width=18, command=self.orientation_left).grid(row=1, column=0, padx=10, pady=8)
        tk.Button(gpio_frame, text="Orientation +10", width=18, command=self.orientation_right).grid(row=1, column=1, padx=10, pady=8)

        status_frame = tk.Frame(self.root)
        status_frame.pack(pady=20)

        tk.Label(status_frame, text="Statut :", font=("Arial", 11, "bold")).pack(side="left")
        tk.Label(status_frame, textvariable=self.status_var, fg="blue", font=("Arial", 11)).pack(side="left", padx=8)

    def validate_inputs(self):
        try:
            altitude = float(self.altitude_var.get())
            orientation = float(self.orientation_var.get())

            if altitude < 0:
                raise ValueError("L'altitude doit être positive ou nulle.")

            if orientation < 0 or orientation > 360:
                raise ValueError("L'orientation doit être comprise entre 0 et 360.")

            return altitude, orientation

        except ValueError as e:
            messagebox.showerror("Erreur de validation", str(e))
            self.status_var.set("Erreur de validation")
            return None, None

    def send_post(self):
        altitude, orientation = self.validate_inputs()
        if altitude is None:
            return

        try:
            response = requests.post(
                API_BASE_URL,
                json={
                    "altitude": altitude,
                    "orientation": orientation
                },
                timeout=5
            )
            response.raise_for_status()

            self.status_var.set("Données envoyées en POST avec succès")
            messagebox.showinfo("Succès", "Données envoyées en POST à l'API")

        except requests.exceptions.RequestException as e:
            self.status_var.set("Erreur POST")
            messagebox.showerror("Erreur API", f"Impossible d'envoyer les données en POST.\n\n{e}")

    def send_get(self):
        altitude, orientation = self.validate_inputs()
        if altitude is None:
            return

        try:
            response = requests.get(
                f"{API_BASE_URL}/update",
                params={
                    "altitude": altitude,
                    "orientation": orientation
                },
                timeout=5
            )
            response.raise_for_status()

            self.status_var.set("Données envoyées en GET avec succès")
            messagebox.showinfo("Succès", "Données envoyées en GET à l'API")

        except requests.exceptions.RequestException as e:
            self.status_var.set("Erreur GET")
            messagebox.showerror("Erreur API", f"Impossible d'envoyer les données en GET.\n\n{e}")

    def altitude_up(self):
        try:
            altitude = float(self.altitude_var.get())
            altitude += 100
            self.altitude_var.set(str(altitude))
            self.send_post()
        except ValueError:
            messagebox.showerror("Erreur", "Altitude invalide")

    def altitude_down(self):
        try:
            altitude = float(self.altitude_var.get())
            altitude = max(0, altitude - 100)
            self.altitude_var.set(str(altitude))
            self.send_post()
        except ValueError:
            messagebox.showerror("Erreur", "Altitude invalide")

    def orientation_left(self):
        try:
            orientation = float(self.orientation_var.get())
            orientation = (orientation - 10) % 360
            self.orientation_var.set(str(orientation))
            self.send_post()
        except ValueError:
            messagebox.showerror("Erreur", "Orientation invalide")

    def orientation_right(self):
        try:
            orientation = float(self.orientation_var.get())
            orientation = (orientation + 10) % 360
            self.orientation_var.set(str(orientation))
            self.send_post()
        except ValueError:
            messagebox.showerror("Erreur", "Orientation invalide")


if __name__ == "__main__":
    root = tk.Tk()
    app = AirplaneTkinterApp(root)
    root.mainloop()