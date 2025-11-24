from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
import time
import webbrowser
import random
import os

# --- सेटिंग्स ---
DEV_NAME = "PRITAM POONIA"  # अपना नाम यहाँ बदल सकते हैं
PASSWORD = "1234"           # अपना पासवर्ड यहाँ बदल सकते हैं

# कलर्स (Hacker Theme)
NEO_GREEN = (0, 1, 0, 1)
NEO_RED = (1, 0, 0, 1)
NEO_DARK = (0.05, 0.05, 0.05, 1)
NEO_CYAN = (0, 1, 1, 1)
NEO_YELLOW = (1, 1, 0, 1)

Window.clearcolor = NEO_DARK

# --- ANDROID FUNCTIONALITY (Safe Mode के साथ) ---
def get_android_apps():
    """Android ऐप्स की लिस्ट लाता है, अगर परमिशन नहीं मिली तो पॉपुलर ऐप्स दिखाता है"""
    apps_list = []
    
    # 1. असली ऐप्स ढूंढ़ने की कोशिश (Real Apps Try)
    if platform == 'android':
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            pm = PythonActivity.mActivity.getPackageManager()
            
            main_intent = Intent(Intent.ACTION_MAIN, None)
            main_intent.addCategory(Intent.CATEGORY_LAUNCHER)
            
            activities = pm.queryIntentActivities(main_intent, 0)
            
            for i in range(activities.size()):
                try:
                    resolve_info = activities.get(i)
                    package_name = resolve_info.activityInfo.packageName
                    char_seq = resolve_info.loadLabel(pm)
                    app_name = char_seq.toString() if char_seq else package_name
                    
                    # खुद के ऐप को लिस्ट में न दिखाएं
                    if package_name != PythonActivity.mActivity.getPackageName():
                        apps_list.append({'name': str(app_name), 'package': str(package_name)})
                except:
                    continue
                    
        except Exception as e:
            print(f"System Error: {e}")

    # 2. अगर लिस्ट खाली है (Android ने रोका), तो ये मैन्युअल ऐप्स दिखाएं
    if not apps_list:
        manual_apps = [
            ("WhatsApp", "com.whatsapp"),
            ("YouTube", "com.google.android.youtube"),
            ("Chrome", "com.android.chrome"),
            ("Settings", "com.android.settings"),
            ("Camera", "com.android.camera"),
            ("Play Store", "com.android.vending"),
            ("Phone", "com.google.android.dialer"),
            ("Messages", "com.google.android.apps.messaging"),
            ("Instagram", "com.instagram.android"),
            ("Facebook", "com.facebook.katana"),
            ("Gallery", "com.google.android.apps.photos"),
            ("Gmail", "com.google.android.gm"),
            ("Maps", "com.google.android.apps.maps")
        ]
        
        apps_list.append({'name': "[ SYSTEM MODE ]", 'package': ''}) 
        for name, pkg in manual_apps:
            apps_list.append({'name': name, 'package': pkg})

    # 3. नाम के अनुसार A-Z सॉर्ट करें
    apps_list.sort(key=lambda x: x['name'].lower())
    return apps_list

def launch_android_app(package_name):
    """ऐप खोलें"""
    if not package_name: return
    
    if platform == 'android':
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            pm = PythonActivity.mActivity.getPackageManager()
            intent = pm.getLaunchIntentForPackage(package_name)
            if intent:
                PythonActivity.mActivity.startActivity(intent)
            else:
                print("App not installed")
        except Exception as e:
            print(f"Launch Error: {e}")
    else:
        print(f"PC Test Launch: {package_name}")

# --- स्क्रीन 1: लॉगिन ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.add_widget(Label(text="[ SYSTEM LOCKED ]", font_size='24sp', color=NEO_RED, bold=True))
        self.info = Label(text=f"USER: {DEV_NAME}", color=NEO_GREEN)
        self.layout.add_widget(self.info)
        self.pass_input = TextInput(multiline=False, password=True, background_color=(0.2,0.2,0.2,1), foreground_color=NEO_GREEN, cursor_color=NEO_GREEN, size_hint=(1, 0.2), halign='center', font_size='20sp')
        self.pass_input.bind(on_text_validate=self.check_pass)
        self.layout.add_widget(self.pass_input)
        self.btn = Button(text="UNLOCK", background_color=(0,0.5,0,1), size_hint=(1, 0.2))
        self.btn.bind(on_press=self.check_pass)
        self.layout.add_widget(self.btn)
        self.add_widget(self.layout)

    def check_pass(self, instance):
        if self.pass_input.text == PASSWORD:
            self.manager.current = 'launcher'
        else:
            self.info.text = "ACCESS DENIED"
            self.info.color = NEO_RED

# --- स्क्रीन 2: लॉन्चर (होम) ---
class LauncherScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # टॉप बार
        info = BoxLayout(size_hint=(1, 0.08))
        self.date_lbl = Label(text="INIT...", color=NEO_GREEN, font_size='14sp', halign='left')
        self.batt_lbl = Label(text="SYS: ONLINE", color=NEO_GREEN, font_size='14sp', halign='right')
        info.add_widget(self.date_lbl); info.add_widget(self.batt_lbl)
        self.layout.add_widget(info)

        # घड़ी
        self.time_lbl = Label(text="00:00", font_size='70sp', color=(1,1,1,1), bold=True)
        self.layout.add_widget(self.time_lbl)

        self.layout.add_widget(Label(text=f"WELCOME, {DEV_NAME}", color=(0.5,0.5,0.5,1), font_size='13sp', size_hint=(1, 0.05), bold=True))
        self.layout.add_widget(Label(text="COMMAND CENTER >_", color=NEO_CYAN, size_hint=(1, 0.05)))
        
        # सर्च बार
        self.search_input = TextInput(hint_text="Search...", multiline=False, background_color=(0.2,0.2,0.2,1), foreground_color=NEO_GREEN, cursor_color=NEO_GREEN, size_hint=(1, 0.12), padding_y=[10, 0])
        self.search_input.bind(on_text_validate=self.process_command)
        self.layout.add_widget(self.search_input)

        # बटन ग्रिड
        grid = GridLayout(cols=4, spacing=5, size_hint=(1, 0.15))
        def mk_btn(n, c, cmd):
            b = Button(text=n, background_color=c, font_size='11sp')
            b.bind(on_press=lambda x: self.process_command(None, cmd=cmd))
            grid.add_widget(b)
        
        mk_btn("GAME", NEO_YELLOW, "game")
        mk_btn("APPS", (1,0.5,0,1), "apps") # App Drawer Link
        mk_btn("YT", (0.8,0,0,1), "youtube")
        mk_btn("EXIT", (0.5,0,0,1), "exit")
        self.layout.add_widget(grid)

        self.log_lbl = Label(text="> SYSTEM READY...", color=NEO_GREEN, size_hint=(1, 0.25), text_size=(Window.width-20, None), halign='left', valign='top', font_size='11sp')
        self.layout.add_widget(self.log_lbl)
        
        self.add_widget(self.layout)
        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        self.time_lbl.text = time.strftime("%H:%M")
        self.date_lbl.text = time.strftime("%d %b").upper()

    def process_command(self, instance, cmd=None):
        q = cmd if cmd else self.search_input.text.strip()
        if not q: return
        c = q.lower()

        if c == "game": self.manager.current = 'game'
        elif c == "apps": self.manager.current = 'drawer'
        elif c == "youtube": webbrowser.open("https://youtube.com")
        elif c == "exit": App.get_running_app().stop()
        else: webbrowser.open(f"https://www.google.com/search?q={q}")
        if instance: self.search_input.text = ""

# --- स्क्रीन 3: APP DRAWER (लिस्ट) ---
class AppDrawerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # हेडर
        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(Label(text="INSTALLED MODULES", color=NEO_CYAN, bold=True, font_size='20sp'))
        
        close_btn = Button(text="X", size_hint=(0.2, 1), background_color=NEO_RED)
        close_btn.bind(on_press=self.go_back)
        header.add_widget(close_btn)
        self.layout.add_widget(header)

        # स्क्रॉलिंग लिस्ट
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=3, spacing=10, size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)
        self.apps_loaded = False

    def on_enter(self):
        # हर बार जब पेज खुले तो चेक करें
        if not self.apps_loaded:
            self.load_apps()
            self.apps_loaded = True

    def load_apps(self):
        self.grid.clear_widgets()
        apps = get_android_apps()
        
        for app in apps:
            safe_name = app['name'][:12]
            btn = Button(text=safe_name, size_hint_y=None, height=100, font_size='12sp', background_color=(0.2,0.2,0.2,1))
            
            # ऐप लॉन्च करने का लॉजिक
            btn.bind(on_press=lambda x, pkg=app['package']: launch_android_app(pkg))
            self.grid.add_widget(btn)

    def go_back(self, instance):
        self.manager.current = 'launcher'

# --- स्क्रीन 4: गेम ---
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.add_widget(Label(text="TIC-TAC-TOE", font_size='30sp', color=NEO_YELLOW, size_hint=(1, 0.15), bold=True))
        self.turn_lbl = Label(text="TURN: X", color=NEO_GREEN, size_hint=(1, 0.1))
        self.layout.add_widget(self.turn_lbl)

        self.grid = GridLayout(cols=3, spacing=5)
        self.buttons = []
        for i in range(9):
            btn = Button(text="", font_size='40sp', background_color=(0.2,0.2,0.2,1))
            btn.bind(on_press=self.move)
            self.buttons.append(btn)
            self.grid.add_widget(btn)
        self.layout.add_widget(self.grid)

        back = Button(text="< BACK", background_color=(1,0,0,1), size_hint=(1, 0.15))
        back.bind(on_press=self.go_back)
        self.layout.add_widget(back)
        self.add_widget(self.layout)
        self.turn = 'X'; self.game_active = True

    def move(self, btn):
        if not self.game_active or btn.text != "": return
        btn.text = self.turn
        btn.color = NEO_GREEN if self.turn == 'X' else NEO_RED
        if self.check_win():
            self.turn_lbl.text = f"WINNER: {self.turn}!"
            self.game_active = False
        elif all(b.text != "" for b in self.buttons):
            self.turn_lbl.text = "DRAW!"; self.game_active = False
        else:
            self.turn = 'O' if self.turn == 'X' else 'X'
            self.turn_lbl.text = f"TURN: {self.turn}"

    def check_win(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.buttons[a].text == self.buttons[b].text == self.buttons[c].text != "": return True
        return False

    def go_back(self, instance):
        for b in self.buttons: b.text = ""
        self.turn = 'X'; self.game_active = True
        self.manager.current = 'launcher'

# --- मुख्य ऐप ---
class NeoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(LauncherScreen(name='launcher'))
        sm.add_widget(AppDrawerScreen(name='drawer'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    NeoApp().run()
  
