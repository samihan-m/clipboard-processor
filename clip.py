import pyperclip as pc
from pynput.keyboard import Key, Listener, KeyCode

do_process: bool = True

def invert(key: KeyCode) -> None:
    global do_process
    try:
        if key.char == '`':
            do_process = not do_process
            print(f"Processing: {'on' if do_process else 'off'}")
        # TODO add key code for exiting program
    except:
        # print("Key is not a character")
        pass

listener = Listener(on_press = invert)
listener.start()

print("Clipboard processing on. Removing all newline characters from copied text before placing it in the clipboard.")
print("Press '`' to toggle clipboard processing.")

while True:
    text = pc.waitForNewPaste()
    if do_process is False:
        continue
    print(f"In: {repr(text)}")
    split_text = text.replace("\r\n", "\n").split("\n")
    processed_text = " ".join([term.strip() for term in split_text])
    pc.copy(processed_text)
    print(f"Out: {repr(processed_text)}")