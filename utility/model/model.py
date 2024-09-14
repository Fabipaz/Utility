import reflex as rx
from sqlmodel import *


class User(rx.Model, table=True):
    correo: str
    password: str



class AuthState(rx.State):
    correo: str
    password: str

    def login(self):
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    (User.correo == self.correo)
                )
            ).first()
            if user and user.password == self.password:
                return rx.redirect("/utilidades")
            else:
                return rx.window_alert("Usuario o contraseña inválidos.")


def login_page():
    return rx.vstack(
        rx.heading("Iniciar sesión"),
        rx.input(placeholder="Correo", on_blur=AuthState.set_correo),
        rx.input(type="password", placeholder="Contraseña", on_blur=AuthState.set_password),
        rx.button("Iniciar sesión", on_click=AuthState.login)
    )