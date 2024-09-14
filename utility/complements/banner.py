import reflex as rx
import asyncio

class BannerState(rx.State):
    images: list[str] = ["/1.jpg", "/10.jpg","/11.jpg"]
    current_image: int = 0

    @rx.background
    async def change_image_periodically(self):
        while True:
            await asyncio.sleep(5)
            async with self:
                self.current_image = (self.current_image + 1) % len(self.images)



def banner():
    return rx.box(
        rx.desktop_only(
                rx.image(
                    src=BannerState.images[BannerState.current_image],
                    width="100%",
                    height="300px",
                    object_fit="cover",
                ),
            ),
            rx.mobile_and_tablet(
                rx.image(
                    src=BannerState.images[BannerState.current_image],
                    width="auto",
                    height="auto",
                    object_fit="cover",
                ),
                rx.divider(),
                on_mount=BannerState.change_image_periodically,
                
    )
)