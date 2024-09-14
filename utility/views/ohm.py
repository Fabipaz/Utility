import reflex as rx

class OhmState(rx.State):
    voltaje: float = 0
    valor_variable: float = 0
    corriente_options: list[str] = ["Amperios", "Miliamperios", "Microamperios"]
    resistencia_options: list[str] = ["Ω", "KΩ", "MΩ"]
    select_unidad_option: str = ""
    resultado: str = ""
    conversion_type: str = ""

    @rx.var
    def resultado_ohm(self) -> str:
        if self.conversion_type == "Calcular valor de la corriente":
            if self.voltaje == 0 or self.valor_variable == 0:
                return "Por favor, ingrese valores válidos"
            corriente = self.voltaje / self.valor_variable
            if self.select_unidad_option == "Amperios":
                return f"La corriente es igual a {corriente} A"
            elif self.select_unidad_option == "Miliamperios":
                return f"La corriente es igual a {corriente * 1000} mA"
            elif self.select_unidad_option == "Microamperios":
                return f"La corriente es igual a {corriente * 1000000} µA"
        elif self.conversion_type == "Calcular valor de la resistencia":
            if self.voltaje == 0 or self.valor_variable == 0:
                return "Por favor, ingrese valores válidos"
            resistencia = self.voltaje / self.valor_variable
            if self.select_unidad_option == "Ω":
                return f"La resistencia es igual a {resistencia} Ω"
            elif self.select_unidad_option == "KΩ":
                return f"La resistencia es igual a {resistencia / 1000} KΩ"
            elif self.select_unidad_option == "MΩ":
                return f"La resistencia es igual a {resistencia / 1000000} MΩ"
        elif self.conversion_type == "Calcular valor del voltaje":
            if self.voltaje == 0 or self.valor_variable == 0:
                return "Por favor, ingrese valores válidos"
            return f"El voltaje es igual a {self.voltaje * self.valor_variable} V"
        else:
            return "Elija una opción de conversión"

    @rx.var
    def placeholder_uno(self) -> str:
        if self.conversion_type == "Calcular valor de la corriente" or self.conversion_type == "Calcular valor de la resistencia":
            return "Ingrese el valor del voltaje"
        elif self.conversion_type == "Calcular valor del voltaje":
            return "Ingrese el valor de la corriente"
        return "Ingrese el valor"

    @rx.var
    def placeholder_dos(self) -> str:
        if self.conversion_type == "Calcular valor de la corriente":
            return "Ingrese el valor de la resistencia"
        elif self.conversion_type == "Calcular valor de la resistencia":
            return "Ingrese el valor de la corriente"
        elif self.conversion_type == "Calcular valor del voltaje":
            return "Ingrese el valor de la resistencia"
        return "Ingrese el valor"

    def convert(self):
        self.resultado = self.resultado_ohm


def ohm() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon("plug-zap"),
                rx.text("Ley de Ohm"),
            ),
            rx.select(
                ["Calcular valor de la corriente", "Calcular valor de la resistencia", "Calcular valor del voltaje"],
                placeholder="Elige una conversión",
                on_change=OhmState.set_conversion_type,
            ),
            rx.cond(
                OhmState.conversion_type == "Calcular valor de la corriente",
                rx.select(
                    OhmState.corriente_options,
                    placeholder="Seleccione unidad de corriente",
                    on_change=OhmState.set_select_unidad_option,
                ),
            ),
            rx.cond(
                OhmState.conversion_type == "Calcular valor de la resistencia",
                rx.select(
                    OhmState.resistencia_options,
                    placeholder="Seleccione unidad de resistencia",
                    on_change=OhmState.set_select_unidad_option,
                ),
            ),
            rx.input(
                placeholder=OhmState.placeholder_uno,
                type_="number",
                on_change=OhmState.set_voltaje,
                value=OhmState.voltaje,
            ),
            rx.input(
                placeholder=OhmState.placeholder_dos,
                type_="number",
                on_change=OhmState.set_valor_variable,
                value=OhmState.valor_variable,
            ),
            rx.button("Convertir", on_click=OhmState.convert),
            rx.text(OhmState.resultado, style={"color": "green", "fontSize": "1.2em"}),
        )
    )


