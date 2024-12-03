import reflex as rx
from utility.views.mensaje import mensaje
from utility.views.baterias import baterias
from utility.views.conversorgf import conversorgf
from utility.views.almacenamiento import almacenamiento
from utility.views.magnitudes import magnitudes
from utility.views.ohm import ohm
from utility.views.unidades import unidades
from utility.views.ups import ups
from utility.views.lenscalculate import lens
from utility.views.banda import banda
# from utility.views.gramatica import gramatica






def portfoliop ()-> rx.Component:
    return rx.grid(
                rx.card(
                    mensaje(),
                ),
                rx.card(
                    baterias(),
                ),
                rx.card(
                    conversorgf(),
                ),
                rx.card(
                    almacenamiento(),
                ),
                rx.card(
                    magnitudes(),
                ),
                rx.card(
                    ohm(),
                ),
                rx.card(
                    unidades(),
                ),
                rx.card(
                    ups(),
                ),
                rx.card(
                    lens(),
                ),
                rx.card(
                    banda(),
                ),
                # rx.card(
                #     gramatica(),
                # ),
                rx.foreach(
                    list(range(0)),
                    lambda _: rx.box(
                        bg_color="#a7db76",
                        height="auto",
                        width="auto",
                    ),
                ),
    columns=rx.breakpoints(initial="1", sm="2", lg="2"),
    spacing="4",
)
