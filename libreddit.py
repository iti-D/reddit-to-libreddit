#import pyperclip

def change_link(link):
    return "https://libredd.it" + link.split('reddit.com').pop()

old_link = input("your URL here: ")
new_link = change_link(old_link)
#pyperclip.copy(new_link)
print(f"new link was copied to your clipboard: {new_link}")
input("any input to close task")
