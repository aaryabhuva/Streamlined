import tkinter as tk
from tkinter import filedialog

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')






from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, NoTransition, CardTransition, RiseInTransition
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

from database import get_list_of_items, get_all_locations_of_item

import os
import logging
import sqlite3

#logger=logging.getLogger()
#logger.disabled=True


#os.environ['KIVY_NO_CONSOLELOG'] = '1'

class ItemScreen(Screen):
    def onpress_item1(self):
        sm.current="item1"
    def onpress_item2(self):
        sm.current="item2"

class Item1Screen(Screen):
    def get_item_data(self):
        item_data_list=get_all_locations_of_item(1)
        data_str="Item_Id    Item_Name   X_Pos   Height  Stock\n"
        #for item_shelf in item_data_list:
            
        #for item_shelf in item_data_list:

        return str(item_data_list)
'''
class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):


class SelectableButton(RecycleDataViewBehavior, Button):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        "Add selection on touch down"
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected

    def on_press(self):
        popup = TextInputPopup(self)
        popup.open()

    def update_changes(self, txt):
        self.text = txt


class RV(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_item_data()

    def get_item_data(self):
        item_data_list=get_all_locations_of_item(1)
        for row in item_data_list:
            for col in row:
                print(col)
                self.data_items.append(col)


class TestApp(App):
    title = "Kivy RecycleView & SQLite3 Demo"

    def build(self):
        return RV()


if __name__ == "__main__":
    TestApp().run()
'''


kv = Builder.load_file("items.kv")

sm = ScreenManager(transition=NoTransition())

screens = [ItemScreen(name="items"),Item1Screen(name="item1")]

for screen in screens:
    sm.add_widget(screen)


class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
    


'''


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.username.text=="a" and self.password.text=="a":
            try:
                conn=sqlite3.connect('sq.db')
                cursor = conn.cursor()
                sql_command = "UPDATE USER SET Logged_In=TRUE"
                cursor.execute(sql_command)
                conn.commit()
                conn.close()
            except:
                garbage_val=0
            sm.current = "home"
        else:
            self.invalidLogin()


    def invalidLogin(self):
        pop = Popup(title='Invalid Login',
                      content=Label(text='Invalid username or password.'),
                      size_hint=(None, None), size=(400, 400))
        pop.open()


class PathButton(Button):

    def get_path(self):

        root = tk.Tk()
        root.withdraw()

        file_name=filedialog.askopenfilename()

        if len(file_name)>=4 and (file_name[-4:]=="xlsx" or file_name[-3:]=="xls"):
            return file_name
        return "Not an Excel File!"

    def get_image_path(self):

        root = tk.Tk()
        root.withdraw()

        file_name = filedialog.askopenfilename()

        if len(file_name) >= 4 and (file_name[-3:] == "jpg" or file_name[-3:] == "png" or file_name[-3:] == "gif"):
            return file_name
        return "Not an Image File!"


class HomeScreen(Screen):

    def onpress_template1(self):
        sm.current="template1"

    def onpress_template2(self):
        sm.current="template2"



#class ItemScreen(Screen):


class Template1Screen(Screen):
    message=ObjectProperty(None)

    def send_message(self):
        #print(self.message.text)
        if self.path_label.text!="" and self.path_label.text!="Not an Excel File!":
            try:
                send_common_message(self.path_label.text, self.message.text)
            except:
                sm.current="home"
                garbage_val=0

    def back_to_home(self):
        sm.current="home"


class Template2Screen(Screen):
    message=ObjectProperty(None)

    def send_message(self):
        if self.path_label.text != "" and self.image_path_label.text != "" and self.path_label.text != "Not an Excel File!" and self.image_path_label.text != "Not an Image File!":
            try:
                send_common_image_message(self.path_label.text, self.image_path_label.text, self.message.text)
            except:
                sm.current = "home"
                garbage_val = 0

    def back_to_home(self):
        sm.current="home"


class WindowManager(ScreenManager):
    pass
'''
