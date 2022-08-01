import tkinter as tk
from tkinter import filedialog

from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp

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
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from database import *

import os
import logging
import sqlite3

#logger=logging.getLogger()
#logger.disabled=True

#os.environ['KIVY_NO_CONSOLELOG'] = '1'


class ItemScreen(Screen):
    pass


class Item1Screen(Screen):
    pass


class Item2Screen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class MyMainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables=None

    def build(self):
        return Builder.load_file("items.kv")

    def add_datatable1(self):
        item_data_list=get_all_locations_of_item(1)
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.4, 'center_y': 0.5},
            size_hint=(0.9, 0.9),
            padding=10,
            column_data=[
                ("Item ID", dp(15)),
                ("Item Name", dp(25)),
                ("Compartment", dp(25)),
                ("X Position", dp(20)),
                ("Height", dp(20)),
                ("Stock", dp(20))
            ],
            row_data=item_data_list
        )
        self.root.ids.data_scr1.ids.data_layout1.add_widget(self.data_tables)

    def add_datatable2(self):
        item_data_list=get_all_locations_of_item(2)
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.4, 'center_y': 0.5},
            size_hint=(0.9, 0.9),
            padding=10,
            column_data=[
                ("Item ID", dp(15)),
                ("Item Name", dp(25)),
                ("Compartment", dp(25)),
                ("X Position", dp(20)),
                ("Height", dp(20)),
                ("Stock", dp(20))
            ],
            row_data=item_data_list
        )
        self.root.ids.data_scr2.ids.data_layout2.add_widget(self.data_tables)

    def change_screen(self, s):
        self.root.current=s

    def drop_item1(self):
        fetch_item(get_item(1))

    def drop_item2(self):
        fetch_item(get_item(2))

    def add_stock1(self):
        item_data_list = get_all_locations_of_item(1)[0]
        add_stock_to_item(item_data_list[0], item_data_list[1], item_data_list[2], item_data_list[3], item_data_list[4], item_data_list[5], 1)

    def add_stock2(self):
        item_data_list = get_all_locations_of_item(2)[0]
        add_stock_to_item(item_data_list[0], item_data_list[1], item_data_list[2], item_data_list[3], item_data_list[4], item_data_list[5], 1)


if __name__ == "__main__":
    MyMainApp().run()











'''
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

