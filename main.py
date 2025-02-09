from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty , NumericProperty ,ObjectProperty
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "300")

class Mainwidget (BoxLayout):
    timer_running = False
    
    counter =1500
    total_time = 1500
    
    timer_mode = StringProperty("Pomo time")
    label_timer = StringProperty("25:00")
    progress_bar = ObjectProperty(None)
    auto_break = True
    Clock_event = None




    def rest_timer(self, button, mode):
        if self.Clock_event :
            Clock.unschedule(self.update_counter)
            self.timer_running = False
            button.text = "Start"
            
            
            #print ("Clock is running   "+str (self.counter )+  "   " +str(self.timer_running))
        
        if mode == "Pomo time":
                self.counter = 1500
                self.label_timer = "25:00"
                self.auto_break = True
                self.timer_mode = "Pomo time"
        if mode == "Break":
                self.counter = 300
                self.label_timer = "05:00"
                self.auto_break = False
                self.timer_mode = "Break"
        if mode == "Long break":
                self.counter = 900
                self.label_timer = "15:00"
                self.auto_break = False
                self.timer_mode = "Long break"
        self.total_time = self.counter  # Update total session time
        if self.progress_bar:
            self.progress_bar.progress = 1
        
    def start_timer(self, button):
        try :
            start_sound = SoundLoader.load("mixkit-modern-technology-select-3124.wav")
        except : 
            print("Error")
        if start_sound:
            start_sound.play()
            pass
        if  not self.timer_running:  
            button.text = "Stop"
            self.Clock_event =Clock.schedule_interval(self.update_counter, 1)
            self.timer_running = True
            
        else:
            button.text = "start"
            Clock.unschedule(self.update_counter)
            
            self.timer_running = False
            print("rest")



    
    def update_counter (self,dt):
        
        
        self.counter -=1
        
        if self.counter >= 0:
            
            min = self.counter // 60
            sec = self.counter % 60

        
            x = f"{min:02}:{sec:02}"
            self.label_timer = str(x)

            if self.progress_bar:
                elapsed_time = self.total_time - self.counter
                self.progress_bar.update_progress(elapsed_time, self.total_time)
        
        
        if self.counter == 0 :

            self.timer_is_done()            
                
        





    def timer_is_done (self):
            try :
                sound = SoundLoader.load("alarm.wav")
            except : 
                print("Error")
            if sound:
                sound.play()
                pass
            if self.auto_break:
                self.timer_mode = "Take a break"
                self.counter = 300
                self.auto_break = False
                self.total_time = self.counter  # Update total session time
                if self.progress_bar:
                        self.progress_bar.progress = 1
        
                
            else: 
                self.timer_running = False
                self.timer_mode = "Pomo time"
                self.counter = 1500
                self.label_timer = "25:00"
                Clock.unschedule(self.update_counter) 
                start_button = self.ids.start_button
                start_button.text = "Start"
                self.total_time = self.counter 
                if self.progress_bar:
                    self.progress_bar.progress = 1
        
class Lineprogress (Widget):
    
    progress = NumericProperty(1)  

    def update_progress(self, elapsed, total):
        self.progress = max(0, min(1, elapsed / total))  # Normalize between 0 and 1
        self.canvas.ask_update()  

class PomotimeApp(App):
    def build(self):
        return Mainwidget()

if __name__ == "__main__":
    PomotimeApp().run()



