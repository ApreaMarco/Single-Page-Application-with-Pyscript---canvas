from pyscript import document, when, display
from pyodide.ffi.wrappers import add_event_listener
from py.library.domdict import DOMDict
from math import pi

class App:
    # Applicazione = dizionario
    dizModel = {}  # dizionario delle variabili ( .. )
    dom = {}  # dizionario view  è il dom del browser
    dizControl = {}  # dizionario Control => CallBack


def init_app_Model():
    dizModel = {
        # Variabili dell'applicazione
        'conta_tst01': 1,
        'toggle_canvas05': True
    }
    return dizModel


def init_app_Control():
    # ogni def interna ha il collegamento con il suo tasto di attivazione
    # chiavi-valore CallBack
    dizCallback = {
        'cb_tst01': callback_tst01,
        'cb_canvas03': callback_canvas03,
        'cb_canvas04': callback_canvas04,
        'cb_canvas05': callback_canvas05
    }
    return dizCallback


def init_binding():
    # Collego gli elementi dom alle funzioni
    add_event_listener(App.dom["tst01"], "click", App.dizControl['cb_tst01'])
    add_event_listener(App.dom["canvas03"], "mousemove", App.dizControl['cb_canvas03'])
    add_event_listener(App.dom["canvas04"], "mousemove", App.dizControl['cb_canvas04'])
    add_event_listener(App.dom["canvas05"], "click", App.dizControl['cb_canvas05'])


# Disegna sul canvas01, senza eventi
def drawOnCanvas01():
    dom_canvas01 = App.dom['canvas01']
    ctx = dom_canvas01.getContext('2d')

    # Disegna un rettangolo rosso al centro del canvas01
    ctx.fillStyle = 'red'
    ctx.fillRect(25, 25, 50, 50)


# Callback tasto tst01
# Conta quante volte è stato premuto il tasto tst01
# Aggiunge una figura al canvas e ritorna allo stato di partenza
def callback_tst01(event=None):
    # Ottieni il riferimento al canvas e al suo contesto di disegno
    dom_canvas02 = App.dom["canvas02"]
    ctx = dom_canvas02.getContext('2d')
    premuto = App.dizModel['conta_tst01']
    testo = ""
    match premuto:
        case 1:
            testo = "Disegno un quadrato rosso"
            ctx.fillStyle = 'red'
            ctx.fillRect(10, 10, 30, 30)
        case 2:
            testo = "Disegno un cerchio verde"
            ctx.beginPath()
            ctx.arc(50, 50, 20, 0, 2 * pi)
            ctx.fillStyle = 'green'
            ctx.fill()
            ctx.closePath()
        case 3:
            testo = "Disegno un triangolo blu"
            ctx.beginPath()
            ctx.moveTo(80, 80)
            ctx.lineTo(60, 60)
            ctx.lineTo(40, 80)
            ctx.fillStyle = 'blue'
            ctx.fill()
            ctx.closePath()
        case _:
            testo = "Cancello il canvas"
            ctx.clearRect(0, 0, dom_canvas02.width, dom_canvas02.height)
            premuto = 0

    dom_p01 = App.dom["p01"]
    dom_p01.innerHTML = testo
    print(f"Sono nella callback_tst01 -> {premuto} -> {testo}")
    display(f"Sono nella callback_tst01 -> {premuto} -> {testo}")
    # Cambia lo stato del conta_tst01
    App.dizModel['conta_tst01'] = premuto + 1

# Callback per il canvas03
def callback_canvas03(event=None):
    # Ottieni il riferimento al canvas e al suo contesto di disegno
    dom_canvas03 = App.dom["canvas03"]
    ctx = dom_canvas03.getContext('2d')

    # Ottieni le coordinate del mouse rispetto al canvas
    rect = dom_canvas03.getBoundingClientRect()
    mouseX = event.clientX - rect.left
    mouseY = event.clientY - rect.top

    # Disegna un cerchio giallo centrato sulla posizione del mouse
    ctx.clearRect(0, 0, dom_canvas03.width, dom_canvas03.height)
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 20, 0, 2 * pi)
    ctx.fillStyle = 'yellow'
    ctx.fill()
    ctx.closePath()
    print(f"Sono nella callback_canvas03")
    display(f"Sono nella callback_canvas03")


# Callback per il canvas04
def callback_canvas04(event=None):
    # Ottieni il riferimento al canvas e al suo contesto di disegno
    dom_canvas04 = App.dom["canvas04"]
    altezza = dom_canvas04.height
    larghezza = dom_canvas04.width
    meta_altezza = altezza / 2
    meta_larghezza = larghezza / 2
    ctx = dom_canvas04.getContext('2d')

    # Pulisco il canvas
    ctx.clearRect(0, 0, larghezza, altezza)

    # Ottieni le coordinate del mouse rispetto al canvas
    rect = dom_canvas04.getBoundingClientRect()
    mouseX = event.clientX - rect.left
    mouseY = event.clientY - rect.top

    # Modifica il comportamento in base alla posizione del mouse
    if (mouseX < meta_larghezza) and (mouseY < meta_altezza):
        ctx.fillStyle = 'red'
        ctx.fillRect(0, 0, meta_larghezza, meta_altezza)
    elif (mouseX >= meta_larghezza) and (mouseY < meta_altezza):
        ctx.fillStyle = 'blue'
        ctx.fillRect(meta_larghezza, 0, meta_larghezza, meta_altezza)
    elif (mouseX < meta_larghezza) and (mouseY >= meta_altezza):
        ctx.fillStyle = 'green'
        ctx.fillRect(0, meta_altezza, meta_larghezza, meta_altezza)
    else:
        ctx.fillStyle = 'yellow'
        ctx.fillRect(meta_larghezza, meta_altezza, meta_larghezza, meta_altezza)

    print(f"Sono nella callback_canvas04")
    display(f"Sono nella callback_canvas04")


# Callback per il canvas05
def callback_canvas05(event=None):
    # Ottieni il riferimento al canvas e al suo contesto di disegno
    dom_canvas05 = App.dom["canvas05"]
    ctx = dom_canvas05.getContext('2d')

    stato = App.dizModel['toggle_canvas05']
    # Disegna un quadrato rosso o un cerchio verde in base allo stato
    ctx.clearRect(0, 0, dom_canvas05.width, dom_canvas05.height)
    if stato:
        ctx.fillStyle = 'red'
        ctx.fillRect(10, 10, 30, 30)
        testo = "Disegno un quadrato rosso"
    else:
        ctx.beginPath()
        ctx.arc(50, 50, 20, 0, 2 * pi)
        ctx.fillStyle = 'green'
        ctx.fill()
        ctx.closePath()
        testo = "Disegno un cerchio verde"

    dom_p02 = App.dom["p02"]
    dom_p02.innerHTML = testo

    print(f"Sono nella callback_canvas05 -> {testo}")
    display(f"Sono nella callback_canvas05 -> {testo}")
    # Cambia lo stato del toggle_canvas05
    App.dizModel['toggle_canvas05'] = not stato

def main():
    App.dizModel = init_app_Model()
    App.dom = DOMDict()
    App.dizControl = init_app_Control()
    init_binding()
    drawOnCanvas01()


if __name__ == "__main__":
    main()

