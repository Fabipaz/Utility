import reflex as rx


class MensajeState(rx.State):
    numero: str = ""
    error: str = ""
    mensaje_url: str = ""



    def enviar(self):
        if self.numero != "":
            self.mensaje_url = f"https://wa.me/57{self.numero}"
            self.error = ""
            return rx.redirect(self.mensaje_url, external=True)
        else:
            self.error = "Ingrese un número válido"
            self.mensaje_url = ""




def mensaje():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon("message-circle-x"),
                rx.text("Mensaje"),
            ),
            
            rx.input(
                placeholder="Ingrese el número",
                on_change=MensajeState.set_numero,
                value=MensajeState.numero,
            ),
            rx.button(
                "Enviar mensaje",
                on_click=MensajeState.enviar,
            ),
            rx.text(MensajeState.error, color="red"),
            padding="10px",
            spacing="5",
            justify="center",
            min_height="25vh",
        )
    )   