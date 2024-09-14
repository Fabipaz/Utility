import reflex as rx


class UpState(rx.State):
    potencia_entrada:str= ""
    tiempo_respaldo:str= ""
    capacidad_ups:float=0
    tiempo_placa:str= ""
    potencia_requerida:str= ""
    resultado:str=""
    unidad:str=""


    def unidades(self):
        if self.resultado >= 1000:
            self.unidad = "Kw"
            self.resultado /= 1000
        else:
            self.unidad = "Watts"

    def Tiempo_Autonomia (self):
        self.potencia_entrada=float(self.potencia_entrada)
        self.tiempo_respaldo=float(self.tiempo_respaldo)
        self.tiempo_placa=float(self.tiempo_placa)

        self.capacidad_ups= self.potencia_entrada*1.3
        factor=self.tiempo_respaldo/self.tiempo_placa
        self.resultado=factor*self.capacidad_ups
        self.unidades()   
        self.potencia_requerida= f"Para la autonomia de {self.tiempo_respaldo} minutos. La potencia requerida es de: {self.resultado} {self.unidad}"







def ups():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon("battery-full"),
                    rx.text("UPS"),
                ),
                rx.input(
                    placeholder="Ingrese autonomia placa",
                    on_change= UpState.set_tiempo_placa,
                    value=UpState.tiempo_placa
                ),
                rx.input(
                    placeholder="Consumo en Watts",
                    on_change= UpState.set_potencia_entrada,
                    value=UpState.potencia_entrada,
                ),
                rx.input(
                    placeholder="Respaldo requerido minutos",
                    on_change= UpState.set_tiempo_respaldo,
                    value=UpState.tiempo_respaldo
                ),
                rx.button("Calcular", on_click=UpState.Tiempo_Autonomia),
                rx.text(UpState.potencia_requerida)
            )
        )
    )