import reflex as rx
import requests
from bs4 import BeautifulSoup

def obtener_tasa_cambio(moneda_base, moneda_destino):
    url = f'https://www.google.com/finance/quote/{moneda_base}-{moneda_destino}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tasa_element = soup.find('div', class_='YMlKec fxKbKc')
            
            if tasa_element:
                tasa_cambio = float(tasa_element.text.replace(',', ''))
                return tasa_cambio
            else:
                return(f'No se pudo encontrar la tasa de cambio para {moneda_base}-{moneda_destino} en la página.')
                
    except requests.RequestExceptios as e:
            return(f'Error al obtener la tasa de cambio para {moneda_base}-{moneda_destino}')
            

class ConversorStategf(rx.State):
    monto_convertido: str = ""
    monto: str = ""
    moneda_base: str = ""
    moneda_destino: str = ""
    tasa_cambio: str = ""
    tmr_cop: str ="Cargando . . ."

    def convertir_monedas(self):
        self.monto= float(self.monto)
        if self.monto and self.moneda_base and self.moneda_destino:
            tasa_cambio = obtener_tasa_cambio(self.moneda_base, self.moneda_destino)
            if isinstance(tasa_cambio, float):
                monto_convertido = self.monto * tasa_cambio
                self.monto_convertido = f'El valor de conversión es: {tasa_cambio}, la suma de {self.monto} {self.moneda_base} equivale a {monto_convertido:.2f} {self.moneda_destino}'
                self.tasa_cambio = f'Tasa de cambio: {tasa_cambio:.4f}'
            else:
                self.monto_convertido = 'No se pudo realizar la conversión.'
                self.tasa_cambio = 'Error al obtener la tasa de cambio'
        else:
            self.monto_convertido = 'Por favor, complete todos los campos.'

    def obtener_tmr_cop(self):
            self.tmr_cop:float=0
            tasa = obtener_tasa_cambio("USD", "COP")
            self.tmr_cop = f"{tasa:.2f}"   


def conversorgf() -> rx.Component:
    return rx.box(
            rx.center(
                rx.vstack(
                rx.text("Monedas"),
                rx.hstack(
                rx.icon("circle-dollar-sign"),
                rx.text(ConversorStategf.tmr_cop, size="5", color="green"),
            ),
                rx.input(
                placeholder="Monto a Cambiar",
                type_="number",
                value=ConversorStategf.monto,
                on_change=ConversorStategf.set_monto,
            ),
                rx.select(
                ["USD", "EUR", "GBP", "COP"],
                placeholder="Moneda de origen",
                value=ConversorStategf.moneda_base,
                on_change=ConversorStategf.set_moneda_base,
            ),
                rx.select(
                ["USD", "EUR", "GBP", "COP"],
                placeholder="Moneda de destino",
                value=ConversorStategf.moneda_destino,
                on_change=ConversorStategf.set_moneda_destino,
            ),
                rx.button("Convertir", on_click=ConversorStategf.convertir_monedas),
                rx.text(ConversorStategf.monto_convertido),     
        ),
            padding="10px",
            spacing="5",
            justify="center",
            min_height="25vh",
    ),
    
            
        
)