import reflex as rx


class BandaState(rx.State):
    fps: str = ''
    resolucion: str = ''
    resultado: str = ''
    compresion_type:str = ''

    def h264(self):
        cu=float(self.fps)
        re=float(self.resolucion)
        kbps = 2 * (cu / 30) * (re * 1024)
        self.resultado = f'{kbps / 1000:.2f} Mbps'
    
    def h265(self):
        cu=float(self.fps)
        re=float(self.resolucion)
        kbps = 1 * (cu / 30) * (re * 1024)
        self.resultado = f'{kbps / 1000:.2f} Mbps'



def banda() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon("video"),
                    rx.text("Ancho de Banda"),
                    ),
                    rx.select(
                        ["H.265", "H.264"],
                        placeholder="Seleccione Compresión",
                        on_change= BandaState.set_compresion_type,
                        value=BandaState.compresion_type,
                    ),
                    rx.cond(
                        BandaState.compresion_type =="H.265",
                        rx.vstack(
                            rx.input(
                                placeholder="Ingrese FPS",
                                on_change=BandaState.set_fps,
                                value=BandaState.fps
                            ),
                            rx.input(
                                placeholder="Ingrese Resolución",
                                on_change=BandaState.set_resolucion,
                                value=BandaState.resolucion
                            ),
                            rx.button("Calcular", on_click=BandaState.h265),
                        ),
                        rx.vstack(
                            rx.input(
                                placeholder="Ingrese FPS",
                                on_change=BandaState.set_fps,
                                value=BandaState.fps
                            ),
                            rx.input(
                                placeholder="Ingrese Resolución",
                                on_change=BandaState.set_resolucion,
                                value=BandaState.resolucion
                            ),
                            rx.button("Calcular", on_click=BandaState.h264),
                        ),
                    ),
                    rx.text(BandaState.resultado),
            )
        )
    )