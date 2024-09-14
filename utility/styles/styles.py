import reflex as rx

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "https://fonts.googleapis.com/css2?family=Lobster&display=swap",
    "https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap",
    "/css/styles.css"

]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer",
        "background-color": "black",  # Color de fondo inicial
        "color": "white",  # Color del texto inicial
        "border": "none",
        "padding": "auto",
        "text-align": "center",
        "text-decoration": "none",
        "display": "inline-block",
        "font-size": "16px",
        "transition": "background-color 0.1s ease",
        ':hover':{
            "background-color": "darkblue",  # Cambia el color de fondo al pasar el cursor
            "color": "white",  
            
        },
            # Suaviza la transición de color
    },
    rx.text: {
        'font-family': 'Comic Sans MS',
        'text-align': 'justify',
        'animation': 'fadeIn 4s ease-in-out'
    },
    rx.heading: {
        'font-family': 'Indie Flower, cursive',
        'display': 'inline-block',  # Asegura que cada letra se anime individualmente
        'animation': 'slideAndColor 5s ease-in-out forwards',
        'animation-delay': 'calc(var(--i) * 10s)',  # Retrasa cada letra
    },
    rx.image: {
        'animation': 'bounceAndSettle 4s ease-out forwards'  # Duración y repetición infinita
    },
    rx.icon: {
        'animation': 'flipCoin 8s ease-in-out infinite' 
    },
}



