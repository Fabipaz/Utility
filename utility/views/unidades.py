import reflex as rx

class TemperatureState(rx.State):
    temperature: str=""
    result: str = ""
    conversion_type: str = ""



    def celsius_to_kelvin(self):
        self.temperature= float(self.temperature)
        self.result = f"{self.temperature}°C es {self.temperature + 273.15:.2f}°K"

    def kelvin_to_celsius(self):
        self.temperature= float(self.temperature)
        self.result = f"{self.temperature}°K es {self.temperature - 273.15:.2f}°C"

    def fahrenheit_to_kelvin(self):
        self.temperature= float(self.temperature)
        kelvin = (5/9) * (self.temperature - 32) + 273.15
        self.result = f"{self.temperature}°F es {kelvin:.2f}°K"

    def kelvin_to_fahrenheit(self):
        self.temperature= float(self.temperature)
        fahrenheit = (9/5) * (self.temperature - 273.15) + 32
        self.result = f"{self.temperature}°K es {fahrenheit:.2f}°F"

    def convert(self):

        if self.conversion_type == "Celsius a Kelvin":
            self.celsius_to_kelvin()
        elif self.conversion_type == "Kelvin a Celsius":
            self.kelvin_to_celsius()
        elif self.conversion_type == "Fahrenheit a Kelvin":
            self.fahrenheit_to_kelvin()
        elif self.conversion_type == "Kelvin a Fahrenheit":
            self.kelvin_to_fahrenheit()
        else: self.result="Elija una opción de conversión"    

def unidades():
    return rx.box(
            rx.center(
                rx.vstack(
                rx.hstack(
                    rx.icon("thermometer-snowflake"),
                    rx.text("Temp"),
                ),
            rx.select(
                ["Celsius a Kelvin", "Kelvin a Celsius", "Fahrenheit a Kelvin", "Kelvin a Fahrenheit"],
                placeholder="Elige una conversión",
                on_change=TemperatureState.set_conversion_type,
            ),
            rx.input(
                placeholder="Introduce la temperatura",
                type_="number",
                on_change=TemperatureState.set_temperature,
                value=TemperatureState.temperature,
            ),
            rx.button("Convertir", on_click=TemperatureState.convert),
            rx.text(TemperatureState.result, style={"color": "red", "fontSize": "1.2em"}),
            ),
        ),
        
            padding="10px",
            spacing="5",
            justify="center",
            min_height="25vh",

    )

