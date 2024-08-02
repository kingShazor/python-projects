import re

def printMails(text):
    emails = re.findall(r"[^\s@]*?[@][^\s@]*?[.](?:de|com|org)", text)
    print(f"Alle gefundenen E-Mail-Adressen: {emails}")

text = "Hier@hacon.depwfw;pwefwe@ewofw.comfwoefwfnoi efewofw@bla.def32p4r xy@lafda@hacon.de"
text2 = "Bitte kontaktiere uns unter info@example.com oder support@example.org."

printMails(text)
printMails(text2)
