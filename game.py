from pyscript import Element

def update():
    game_win = Element("game")
    game_URL = Element('game1').element.value
    text = f"https://scratch.mit.edu/projects/{game_URL}/embed"
    game_win.write(text)

print("hi")