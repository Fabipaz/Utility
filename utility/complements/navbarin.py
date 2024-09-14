import reflex as rx
from utility.views.conversorgf import ConversorStategf
from utility.routes import Routes




def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_menu_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_index() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/Fabipazdev.gif",
                        width="4em",
                        height="auto",
                        border_radius="100%",
                    ),
                    rx.heading(
                        "Cálculos y mas...", size="8", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Inicio", "home",Routes.INDEX.value ),
                    navbar_icons_item(
                        ConversorStategf.tmr_cop, "circle-dollar-sign", "https://www.banrep.gov.co/es/estadisticas/trm",
                        
                    ),
                    navbar_icons_item(
                        "Blog", "rss", Routes.BLOG.value
                    ),
                    # navbar_icons_item(
                    #     "Proveedores", "external-link", "/#"
                    # ),
                    navbar_icons_item(
                        "login", "user", Routes.LOGIN.value
                    ),
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/Fabipazdev.gif",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Cálculos y mas...", size="6", weight="bold",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=20)
                    ),
                    rx.menu.content(
                        navbar_icons_menu_item(
                            "Inicio", "home", Routes.INDEX.value
                        ),
                        navbar_icons_menu_item(
                            ConversorStategf.tmr_cop, "coins", "https://www.banrep.gov.co/es/estadisticas/trm"
                        ),
                        navbar_icons_menu_item(
                            "Blog", "rss", Routes.BLOG.value
                        ),
                        # navbar_icons_menu_item(
                        #     "Proveedores", "external-link", "/#"
                        # ),
                        navbar_icons_item(
                        "login", "user", Routes.LOGIN.value
                    ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )