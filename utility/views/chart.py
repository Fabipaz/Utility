import reflex as rx
import random

class ChartsState(rx.State):
    data = data

    def randomize_data(self):
        self.data = [
            {
                "month": item["month"],
                "Mobile": random.randint(100, 500),
                "Desktop": random.randint(400, 700),
            }
            for item in self.data
        ]

def chart():
    return rx.box(
        rx.button(
            "Randomize",
            on_click=ChartsState.randomize_data,
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="Mobile",
                stroke=rx.color("violet", 9),
                fill=rx.color("violet", 8),
                type_="natural",
            ),
            rx.recharts.area(
                data_key="Desktop",
                stroke=rx.color("slate", 8),
                fill=rx.color("slate", 7),
                type_="natural"
            ),
            rx.recharts.graphing_tooltip(),
            rx.recharts.cartesian_grid(horizontal=True, vertical=False),
            rx.recharts.x_axis(
                data_key="name",
                type_="category",
            ),
            data=ChartsState.data,
        ),
    )