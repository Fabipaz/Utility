import reflex as rx

class BateriaState(rx.State):
    voltajebat: str = ""
    corrientebat: str = ""
    corrientesalida: str = ""
    resultado: str = ""
    convert_type: str = ""
    days_input: str = ""

    def calculo(self):
        try:
            vbat = float(self.voltajebat)
            cbat = float(self.corrientebat)
            csal = float(self.corrientesalida)
            wbat = vbat * cbat
            wload = vbat * csal
            test = wbat / wload
            self.resultado = f"El tiempo de autonomia son {test:.2f} horas "
        except ValueError:
            self.resultado = "Error: Ingrese valores numéricos válidos"

    def futuro(self):
        try:
            vbat = float(self.voltajebat)
            csal = float(self.corrientesalida)
            day = float(self.days_input)
            cbat = day * csal
            self.resultado = f"La batería requerida es de {vbat:.2f} V y {cbat} AH "
        except ValueError:
            self.resultado = "Error: Ingrese valores numéricos válidos"

def baterias() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon("battery-charging"),
                    rx.text("Baterías"),
                ),
                rx.select(
                    ["Proyección", "Presente"],
                    placeholder="Selecciona el cálculo",
                    on_change=BateriaState.set_convert_type,
                    value=BateriaState.convert_type,
                ),
                rx.cond(
                    BateriaState.convert_type == "Proyección",
                    rx.vstack(
                        rx.input(
                            placeholder="voltaje de la batería",
                            on_change=BateriaState.set_voltajebat,
                            value=BateriaState.voltajebat
                        ),
                        rx.input(
                            placeholder="Corriente de salida",
                            on_change=BateriaState.set_corrientesalida,
                            value=BateriaState.corrientesalida
                        ),
                        rx.input(
                            placeholder="Horas autonomia",
                            on_change=BateriaState.set_days_input,
                            value=BateriaState.days_input
                        ),
                        rx.button("Calcular", on_click=BateriaState.futuro),
                    ),
                    rx.vstack(
                        rx.input(
                            placeholder="voltaje de la batería",
                            on_change=BateriaState.set_voltajebat,
                            value=BateriaState.voltajebat
                        ),
                        rx.input(
                            placeholder="Corriente de salida",
                            on_change=BateriaState.set_corrientesalida,
                            value=BateriaState.corrientesalida
                        ),
                        rx.input(
                            placeholder="AH batería",
                            on_change=BateriaState.set_corrientebat,
                            value=BateriaState.corrientebat
                        ),
                        rx.button("Calcular", on_click=BateriaState.calculo),
                    ),
                ),
                rx.text(BateriaState.resultado, size="4", color="red"),
            )
        )
    )

