import reflex as rx
from spellchecker import SpellChecker


# Inicializar el corrector fuera de la clase de estado
corrector = SpellChecker(language='es')

class GramaticaState(rx.State):
    text_in: str = ''
    text_out: str = ''
    show_notification: bool = False

    def validacion(self):
        self.text_out = self.correct_text(self.text_in)

    def copy_text(self):
        self.show_notification = True
        return rx.set_clipboard(self.text_out)

    def correct_text(self, text):
        words = text.split()
        corrected_words = [
            corrector.correction(word) if corrector.correction(word) is not None else word
            for word in words
        ]
        return " ".join(corrected_words)


def gramatica():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon('book-open-check'),
                rx.text('Ortografía')
            ),
            rx.text_area(
                placeholder='Ingrese el texto a validar',
                on_change=GramaticaState.set_text_in,
                value=GramaticaState.text_in
            ),
            rx.button('Validar', on_click=GramaticaState.validacion),
            rx.box(
                rx.text_area(
                    value=GramaticaState.text_out,
                    is_read_only=True,
                    height='100px'
                ),
                rx.icon(
                    'copy',
                    on_click=GramaticaState.copy_text,
                    position="absolute",
                    top="0.5em",
                    right="0.5em",
                    cursor="pointer",
                ),
                position="relative",
            ),
            rx.cond(
                GramaticaState.show_notification,
                rx.text("¡Texto copiado!", color="green"),
            )
        )
    )