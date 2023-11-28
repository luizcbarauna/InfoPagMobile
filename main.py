from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel

KV = '''
ScreenManager:
    LoginScreen:
    ContrachequeScreen:
    RendimentosScreen:
    DadosPessoaisScreen:
    ExibirContrachequeScreen:
    ExibirRendimentosScreen:

<LoginScreen>:
    name: "login"
    MDScreen:
        MDCard:
            size_hint: None, None
            size: "280dp", "220dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            orientation: "vertical"
            spacing: "12dp"
            # restante dos elementos da tela de login
            Image:
                source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
                size_hint_y: None
                height: "150dp"
            MDLabel:
                text: "Login"
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                font_size: "20sp"
            MDTextField:
                id: username
                hint_text: "CPF"
            MDTextField:
                id: password
                hint_text: "Senha"
                password: True
            Widget:
            AnchorLayout:
                anchor_x: 'center'
                MDRaisedButton:
                    text: "Entrar"
                    size_hint: None, None
                    size: "120dp", "36dp"
                    font_size: "12sp"
                    md_bg_color: 0.06, 0.06, 0.2, 1
                    on_release: root.check_login()

<ContrachequeScreen>:
    name: "contracheque"
    FloatLayout:
        Image:
            source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
            size_hint_y: None
            size: (40,40)
            pos_hint: {"top": .95}
        MDRaisedButton:
            text: "Sair"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": .95, "top": .95}
            on_release: app.confirm_exit()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            elevation_normal: 0
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Contracheque"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"left": 1, "top": .85}
            on_release: root.go_to_contracheque()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Rendimentos"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .49, "top": .85}
            on_release: root.go_to_rendimentos()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Dados Pessoais"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": 1, "top": .85}
            on_release: root.go_to_dados_pessoais()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDLabel:
            text: "Bem Vindo!"
            halign: 'left'
            pos_hint: {"center_x": .55, "center_y": .75}
            height: self.texture_size[1]
        MDLabel:
            text: "Selecione o período que deseja:"
            halign: 'left'
            pos_hint: {"center_x": .55, "center_y": .65}
            height: self.texture_size[1]
        MDTextField:
            id: entrada_mes
            hint_text: "Mês"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .35, "center_y": .55}
            max_text_length: 2
            input_filter: "int"
        MDTextField:
            id: entrada_ano
            hint_text: "Ano"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .65, "center_y": .55}
            max_text_length: 4
            input_filter: "int"
        MDRaisedButton:
            text: "Confirmar"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            on_release: root.confirmar_mes_e_ano()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1

<RendimentosScreen>:
    name: "rendimentos"
    FloatLayout:
        Image:
            source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
            size_hint_y: None
            size: (40,40)
            pos_hint: {"top": .95}
        MDRaisedButton:
            text: "Sair"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": .95, "top": .95}
            on_release: app.confirm_exit()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            elevation_normal: 0
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Contracheque"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"left": 1, "top": .85}
            on_release: root.go_to_contracheque()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Rendimentos"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .49, "top": .85}
            on_release: root.go_to_rendimentos()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Dados Pessoais"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": 1, "top": .85}
            on_release: root.go_to_dados_pessoais()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDLabel:
            text: "Selecione o período que deseja:"
            halign: 'left'
            pos_hint: {"center_x": .55, "center_y": .65}
            height: self.texture_size[1]
        MDTextField:
            id: entrada_ano
            hint_text: "Ano"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .50, "center_y": .55}
            max_text_length: 4
            input_filter: "int"
        MDRaisedButton:
            text: "Confirmar"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            on_release: root.confirmar_ano()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1

<DadosPessoaisScreen>:
    name: "dados_pessoais"
    FloatLayout:
        Image:
            source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
            size_hint_y: None
            size: (40,40)
            pos_hint: {"top": .95}
        MDRaisedButton:
            text: "Sair"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": .95, "top": .95}
            on_release: app.confirm_exit()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            elevation_normal: 0
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Contracheque"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"left": 1, "top": .85}
            on_release: root.go_to_contracheque()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Rendimentos"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .49, "top": .85}
            on_release: root.go_to_rendimentos()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Dados Pessoais"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": 1, "top": .85}
            on_release: root.go_to_dados_pessoais()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
        MDTextField:
            id: nome
            hint_text: "Nome"
            size_hint: None, None
            size: "200dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .60}
            readonly: True
        MDTextField:
            id: cpf
            hint_text: "CPF"
            size_hint: None, None
            size: "200dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .50}
            readonly: True
        MDTextField:
            id: cargo
            hint_text: "Cargo"
            size_hint: None, None
            size: "200dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .40}
            readonly: True
        MDTextField:
            id: email
            hint_text: "E-mail Institucional"
            size_hint: None, None
            size: "200dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .5, "center_y": .30}
            readonly: True

<ExibirContrachequeScreen>:
    name: "exibir_contracheque"
    FloatLayout:
        Image:
            source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
            size_hint_y: None
            size: (40,40)
            pos_hint: {"top": .95}
        Image:
            source: "C:/Users/Henrique/Desktop/joao.gif"
            size_hint_y: None
            size: (240,240)
            pos_hint: {"center_x": .5, "center_y": .5}
        MDRaisedButton:
            text: "Sair"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": .95, "top": .95}
            on_release: app.confirm_exit()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            elevation_normal: 0
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Contracheque"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"left": 1, "top": .85}
            on_release: root.go_to_contracheque()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Rendimentos"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .49, "top": .85}
            on_release: root.go_to_rendimentos()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Dados Pessoais"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": 1, "top": .85}
            on_release: root.go_to_dados_pessoais()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Salvar"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .8, "center_y": .1}
            on_release: root.confirm_save()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1

<ExibirRendimentosScreen>:
    name: "exibir_rendimentos"
    FloatLayout:
        Image:
            source: "C:/Users/Henrique/Desktop/logo_infopagbege.gif"
            size_hint_y: None
            size: (40,40)
            pos_hint: {"top": .95}
        Image:
            source: "C:/Users/Henrique/Desktop/Rendimento_anual_final.gif"
            size_hint_y: None
            size: (410,410)
            pos_hint: {"center_x": .5, "center_y": .45}
        MDRaisedButton:
            text: "Sair"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": .95, "top": .95}
            on_release: app.confirm_exit()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            elevation_normal: 0
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Contracheque"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"left": 1, "top": .85}
            on_release: root.go_to_contracheque()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Rendimentos"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .49, "top": .85}
            on_release: root.go_to_rendimentos()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Dados Pessoais"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"right": 1, "top": .85}
            on_release: root.go_to_dados_pessoais()
            md_bg_color: 1, 1, 1, 1
            theme_text_color: "Custom" 
            text_color: 0, 0, 0, 1
            line_width: 1
            line_color: 0, 0, 0, 1

        MDRaisedButton:
            text: "Salvar"
            size_hint: None, None
            size: "100dp", "36dp"
            font_size: "12sp"
            pos_hint: {"center_x": .8, "center_y": .1}
            on_release: root.confirm_save()
            md_bg_color: 0.6196, 0.6196, 0.6196, 1
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            line_width: 2
            line_color: 0, 0, 0, 1
'''


class LoginScreen(Screen):
    def check_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username == "12345678900" and password == "senha":
            self.manager.current = "contracheque"

            nome = "João da Silva"
            cpf = "123.456.789-00"
            cargo = "Desenvolvedor"
            email = "joaojds@outlook.com"

            self.manager.get_screen("dados_pessoais").set_employee_data(nome, cpf, cargo, email)


        elif username == "12365478900" and password == "senha":
            self.manager.current = "contracheque"

            nome = "Patrícia Abravanel"
            cpf = "123.654.789-00"
            cargo = "Gerente"
            email = "patriciaabr@outlook.com"

            self.manager.get_screen("dados_pessoais").set_employee_data(nome, cpf, cargo, email)


        else:
            Snackbar(text="Usuário ou senha incorretos").open()


class ContrachequeScreen(Screen):
    def go_to_contracheque(self):
        pass

    def go_to_rendimentos(self):
        self.manager.current = "rendimentos"

    def go_to_dados_pessoais(self):
        self.manager.current = "dados_pessoais"

    def confirmar_mes_e_ano(self):
        mes = self.ids.entrada_mes.text
        ano = self.ids.entrada_ano.text

        if len(ano) == 4 and 1 <= int(mes) <= 12:
            self.manager.current = "exibir_contracheque"
        else:
            Snackbar(text=f"Mês ou ano inválidos.").open()


class RendimentosScreen(Screen):
    def go_to_contracheque(self):
        self.manager.current = "contracheque"

    def go_to_rendimentos(self):
        pass

    def go_to_dados_pessoais(self):
        self.manager.current = "dados_pessoais"

    def confirmar_ano(self):
        ano = self.ids.entrada_ano.text

        if len(ano) == 4:
            self.manager.current = "exibir_rendimentos"
        else:
            Snackbar(text=f"Ano inválido.").open()


class DadosPessoaisScreen(Screen):
    def go_to_contracheque(self):
        self.manager.current = "contracheque"

    def go_to_rendimentos(self):
        self.manager.current = "rendimentos"

    def go_to_dados_pessoais(self):
        pass

    def set_employee_data(self, nome, cpf, cargo, email):
        self.ids.nome.text = nome
        self.ids.cpf.text = cpf
        self.ids.cargo.text = cargo
        self.ids.email.text = email


class ExibirContrachequeScreen(Screen):
    def go_to_contracheque(self):
        pass

    def go_to_rendimentos(self):
        self.manager.current = "rendimentos"

    def go_to_dados_pessoais(self):
        self.manager.current = "dados_pessoais"

    def confirm_save(self):
        Snackbar(text="Arquivo salvo").open()


class ExibirRendimentosScreen(Screen):
    def go_to_contracheque(self):
        self.manager.current = "contracheque"

    def go_to_rendimentos(self):
        pass

    def go_to_dados_pessoais(self):
        self.manager.current = "dados_pessoais"

    def confirm_save(self):
        Snackbar(text="Arquivo salvo").open()

class InfoPag(MDApp):
    def build(self):
        Window.size = (360, 640)
        self.theme_cls.theme_style = "Light"
        self.dialog = None
        screen = Builder.load_string(KV)
        return screen

    def confirm_exit(self):
        self.dialog = MDDialog(
            title="Sair",
            text="Deseja sair do sistema?",
            buttons=[
                MDRaisedButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss(),
                    text_color=(0, 0, 0, 1),
                    md_bg_color=(0.6196, 0.6196, 0.6196, 1)
                ),
                MDRaisedButton(
                    text="Confirmar",
                    on_release=lambda x: self.exit_app(),
                    text_color=(1, 1, 1, 1),
                    md_bg_color=(0.06, 0.06, 0.2, 1)
                )
            ]
        )
        self.dialog.open()

        self.dialog.text = "[color=000000]Deseja sair do sistema?[/color]"
        self.dialog.text_cls = MDLabel(font_style="Subtitle1", theme_text_color="Secondary")

    def exit_app(self):
        if self.dialog:
            self.dialog.dismiss()
        login_screen = self.root.get_screen("login")
        login_screen.ids.username.text = ""
        login_screen.ids.password.text = ""
        self.root.current = "login"


if __name__ == '__main__':
    InfoPag().run()
