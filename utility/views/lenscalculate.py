import reflex as rx




def lens ():
    return rx.box(
                rx.center(
                    rx.vstack(
                        rx.center(
                            rx.hstack(
                            rx.icon("scan-search"),
                            rx.text("lens calculator"),
                        ), 
                        ), 
                        rx.link(
                            rx.image(
                                src="/lens.gif"
                            ),
                            href="https://www.jvsg.com/calculators/cctv-lens-calculator/",
                            is_external= True
                        )  
                    )
                )    
            )  