import reflex as rx

class StorageState(rx.State):
    bitrage: str =""
    qty_cam: str =""
    qty_days: str = ""
    storage_total: str = ""
    unidad: str = ""
    result: float = 0

    def unidades(self):
        if self.result >= 1000:
            self.unidad = "Tb"
            self.result /= 1000
        else:
            self.unidad = "Gb"

    def calculo(self):
        bits = 8
        seg = 3600
        hora = 24
        kb_gb = 1000000000
        self.bitrage=float(self.bitrage)
        self.qty_cam=int(self.qty_cam)
        self.qty_days=int(self.qty_days)
        
        self.result = ((self.bitrage / bits) * seg * hora * self.qty_cam * self.qty_days) / kb_gb
        self.unidades()
        self.storage_total = f"La capacidad requerida es {self.result:.2f} {self.unidad}"





def almacenamiento():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon("hard-drive"),
                    rx.text("CCTV Storage"),
                ),
                rx.input(
                    placeholder="Bitrage cámara",
                    on_change=StorageState.set_bitrage,
                    value=StorageState.bitrage
                ),
                rx.input(
                    placeholder="Número de cámaras",
                    on_change=StorageState.set_qty_cam,
                    value=StorageState.qty_cam
                ),
                rx.input(
                    placeholder="Número de días",
                    on_change=StorageState.set_qty_days,
                    value=StorageState.qty_days
                ),
                rx.button(
                    "Calcular", on_click=StorageState.calculo
                ),
                rx.text(StorageState.storage_total)
            )
        )
    )