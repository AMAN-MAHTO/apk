from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from function import add_user, QR_scanner


class grid(Widget):
    name = ObjectProperty(None)
    ph = ObjectProperty(None)

    def btn(self):
        if self.name.text == '' or self.ph.text == '':
            print('fill both')
        else:
            add_user(self.name.text, self.ph.text)
            self.name.text = ''
            self.ph.text = ''

    def verifie_user(self):
        scan_output = QR_scanner()
        if scan_output == None:
            print('User not identifie')
        else:
            print(
                f"User Details\nID: {scan_output[0][0]}\nName: {scan_output[0][1]}\nMKD: {scan_output[0][2]}\nEXP: {scan_output[0][3]}\nPh: {scan_output[0][4]} ")


class mainapp(MDApp):

    def build(self):
        # self.title = 'pro'
        # self.them_cls.primary_palette ="Blue"

        return grid()


mainapp().run()
