import reflex as rx
import os
from utility.routes import Routes
from dotenv import load_dotenv


load_dotenv()


user_email = os.getenv("EMAIL")
user_password = os.getenv("PASSWORD")

class LoginState (rx.State):
    email:str
    password:str
    is_logged_in: bool = False

    
    def login (self):
        if self.email == user_email and self.password == user_password:
            self.is_logged_in = True,
            return rx.redirect(Routes.DASHBOARD.value)
        else:
            return rx.window_alert("Usuario o contraseña incorrectos")
    


    def logout(self):
        self.is_logged_in = False
        self.username = ""
        self.password = ""
        return rx.redirect(Routes.INDEX.value)    
    
    def check_login(self):
        if not self.is_logged_in:
            return rx.redirect(Routes.LOGIN.value)