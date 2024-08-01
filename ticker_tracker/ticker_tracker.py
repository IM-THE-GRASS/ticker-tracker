import reflex as rx

class State(rx.State):
    tickets:str = "9999"    
    goal_percent:str = "7.5"

def index():
    return rx.box(
        rx.text(
            f"You currently have {State.tickets} tickets!",
            font_size="8.89vh",
            font_family="Slackey, sans-serif",
            color="rgba(123.25, 255, 176.77, 0.94)",
            text_align="center",
            position="absolute",
            top="40vh",
            left="-16vw",
            width="132vw",
            height="23vh",
        ),
        rx.image(
            src="https://cloud-837rvecwy-hack-club-bot.vercel.app/0111851_sp880-airpods-pro-2nd-gen.png",
            width="12.97vw",
            height="24.72vh",
            position="absolute",
            top="67vh",
            left="5vw",
            transform="rotate(4deg)",
        ),
        rx.image(
            src="https://cloud-bscuvqen5-hack-club-bot.vercel.app/045ee3bbe-1519-481a-908e-781f1323a72e-4_f7e8a61e-ae12-4b8d-9c20-68c38709be13.png",
            width="26vw",
            height="46h",
            position="absolute",
            top="-7vh",
            left="72vw",
            transform="rotate(-10deg)",
        ),
        rx.text(
            f"You are {State.goal_percent}% of the way to your goal!",
            font_size="4.44vh",
            font_family="Slackey, sans-serif",
            color="#3DD68C",
            text_align="center",
            position="absolute",
            top="51vh",
            left="22vw",
            width="57vw",
            height="12vh",
        ),
        rx.button(
            rx.hstack(
                rx.box(
                    rx.icon(
                        "pencil",
                        size=30
                    ),
                    width="2vw",
                    height="4vh",
                ),
                rx.text(
                    "Change goal",
                    color="#F5F5F5",
                    font_size="4vh",
                    font_family="Slackey",
                ),
                spacing="1vw",
            ),
            bg="#30A46C",
            border_radius="0.5vw",
            padding="2vh",
            position="absolute",
            top="60vh",
            left="40vw",
            width="20vw",
            height="40px",
        ),
        rx.box(
            rx.center(
                rx.icon(
                    "settings",
                    size=92, 
                ),
                height="100%"
            ),
            bg="#30A46C",
            border_radius="50%",
            position="absolute",
            top="1vh",
            left="1vw",
            width="40",
            height="40",
        ),
        overflow="hidden",
        width="100vw",
        height="100vh",
        position="relative",
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Slackey&display=swap"
    ],
)
app.add_page(index)