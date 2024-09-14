import reflex as rx
from utility.styles.styles import BASE_STYLE,STYLESHEETS
from utility.views.conversorgf import ConversorStategf
from utility.pages.index import index
from utility.pages.login import login
from utility.pages.utilidades import utilidades









app = rx.App( 
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,)
app.add_page(index,
            on_load=ConversorStategf.obtener_tmr_cop
            )

app.add_page(login)
