from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

#Config

Config.set("graphics", "resizeble", 1)
Config.set("graphics", "width", 600)
Config.set("graphics", "heigth", 400)

#main class
class Application(App):
    
    def click(self, instance):
        self.label.text = "Спасибо, что нажал!"


    #Постройка виджетов на окне  
    def build(self):
        but_together = BoxLayout()
        grid = GridLayout(cols=1) 
       
        zapis = Button(text="Запись", font_size=28, background_color="cyan", on_press=self.click)
        masters = Button(text="Список мастеров", font_size=28, background_color="red")
        clients = Button(text="Клиенты", font_size=28, background_color="yellow")
        label = Label (text="Текст", font_size=28)
        
        but_together.add_widget(zapis)
        but_together.add_widget(masters)
        but_together.add_widget(clients)
        
        grid.add_widget(but_together)
        grid.add_widget(label)
        return grid
 
  
if __name__ == "__main__":
     Application().run()
	
