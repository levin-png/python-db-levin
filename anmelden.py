from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class AnmeldenWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Benutzername und/oder Passwort benötigt.[/color]'
        else:
            if uname == 'levin' and passw == '12345':
                info.text = '[color=#00FF00]Erfolgreich eingeloggt.[/color]'
            else:
                info.text = '[color=#FF0000]Benutzername und/oder Passwort ungültig.[/color]'


class AnmeldenApp(App):
    def build(self):
        return AnmeldenWindow()

if __name__=="__main__":
    sa = AnmeldenApp()
    sa.run()