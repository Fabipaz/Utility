import reflex as rx
from utility.states.loginstate import LoginState
from utility.complements.navbarin import navbar_icons_index




def login():
    return rx.box(
            navbar_icons_index(),
            rx.center(
                    rx.vstack(
                    rx.heading("Iniciar sesión"),
                    rx.input(placeholder="Mail", on_blur=LoginState.set_email),
                    rx.input(type="password", placeholder="Contraseña", on_blur=LoginState.set_password),
                    rx.button("Iniciar sesión", on_click=LoginState.login),
                )
            )
            
    ) 




