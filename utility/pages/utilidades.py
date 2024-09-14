import reflex as rx
from utility.complements.navbar import navbar_icons
from utility.views.porfoliop import portfoliop
from utility.complements.banner import BannerState
from utility.routes import Routes
from utility.states.loginstate import LoginState
from utility.views.conversorgf import ConversorStategf

@rx.page(title="Dashboard", route=Routes.DASHBOARD.value, on_load=LoginState.check_login)
def utilidades ()-> rx.Component:
    return rx.box(
        navbar_icons(),
        # rx.divider(),
        # banner(),
        # rx.divider(),
        rx.box(
        rx.image(
            src=BannerState.images[BannerState.current_image],
            # playing=True,
            # loop=True,
            # width="100%",
            # height="100%",
            object_fit="cover",
        ),
        width="100vw",
        height="100vh",
        position="fixed",
        top="0",
        left="0",
        z_index="-1",
        ),
        rx.divider(),
        rx.center(
            rx.vstack(
                portfoliop(),
            ),
            
        ),
        rx.divider(),
        # rx.color_mode.button(position="top-right"),
        on_mount=BannerState.change_image_periodically
        
    ),