import pyperclip

def change_link(link): # changes the link
    return "https://libredd.it" + link.split('reddit.com').pop()

old_link = pyperclip.waitForPaste() # saves the last copied element (text) from clipboard to old_link.
new_link = change_link(old_link)
pyperclip.copy(new_link) # automatically copies new link to your clipboard.
print(f"new link was copied to your clipboard: {new_link}")
input("any input to close task")
