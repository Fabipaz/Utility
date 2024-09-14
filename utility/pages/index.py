import reflex as rx
from utility.complements.navbarin import navbar_icons_index
from utility.views.porfoliop import portfoliop
from utility.complements.banner import BannerState

@rx.page(title="Home")
def index ()-> rx.Component:
    return rx.box(
        navbar_icons_index(),
        # rx.divider(),
        # banner(),
        # rx.divider(),
        rx.box(
        rx.video(
            url="https://www.youtube.com/embed/9bZkp7q19f0",
            playing=True,
            loop=True,
            width="100%",
            height="100%",
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
                rx.box()
                # portfoliop(),
            ),
            
        ),
        rx.divider(),
        on_mount=BannerState.change_image_periodically
        
    ),