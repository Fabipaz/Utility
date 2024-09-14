import reflex as rx


class MagnitudState(rx.State):
    magnitud: float = 0
    factor_potencia: float = 0
    resultado: str = ""
    conversion_type: str = ""
    constante: float = 1.34102

    @rx.var
    def resultado_computado(self):
        if self.conversion_type == "Kw to KVA":
            return f"{self.magnitud} Kw es igual {self.magnitud / self.factor_potencia} KVA"
        elif self.conversion_type == "KVA to Kw":
            return f"{self.magnitud} KVA es igual {self.magnitud * self.factor_potencia} Kw"
        elif self.conversion_type == "Kw to HP":
            return f"{self.magnitud} Kw es igual {self.magnitud * self.constante} HP"
        elif self.conversion_type == "HP to Kw":
            return f"{self.magnitud} HP es igual {self.magnitud / self.constante} Kw"
        else:
            return "Elija una opción de conversión"

    def convert(self):
        self.resultado = self.resultado_computado


def magnitudes ()-> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
            rx.hstack(
                rx.icon("cable"),
                rx.text("Kw-KVA-HP"),
            ),    
            rx.select(
                ["Kw to KVA","KVA to Kw","Kw to HP","HP to Kw"],
                placeholder="Elige una conversión",
                on_change=MagnitudState.set_conversion_type,
            ),
            rx.input(
                placeholder="Ingrese valor a convertir",
                type_="number",
                on_change=MagnitudState.set_magnitud,
                value=MagnitudState.magnitud,
            ),
            rx.hstack(
                rx.input(
                placeholder="Ingrese factor de potencia",
                type_="number",
                on_change=MagnitudState.set_factor_potencia,
                value=MagnitudState.factor_potencia,
            ),
            rx.text("F.P"),
            ),
            rx.button("Convertir", on_click=MagnitudState.convert),
            rx.text(MagnitudState.resultado, style={"color": "red", "fontSize": "1.2em"}),
        )
        ),
            padding="10px",
            spacing="5",
            justify="center",
            min_height="25vh",
        
    )