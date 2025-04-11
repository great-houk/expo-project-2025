import pygame as pg
import socket
import time


###########################################################
#####             Set up Server Connection         #########
###########################################################
PI_IP = 'XXX.XXX.X.XX'  
PI_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (PI_IP, PI_PORT)  
print("connection established")

###########################################################
#####        Initialize pg and Joystick       #########
###########################################################
pg.init()
pg.joystick.init()

if pg.joystick.get_count() == 0:
    raise Exception("No controller")

controller = pg.joystick.Joystick(0)
controller.init()


###########################################################
#####        Controller Communication Loop        #########
###########################################################
try:
    while True:
        pg.event.pump() # Frees up the event queue
        
        
        x = controller.get_axis(0) * 100
        y = controller.get_axis(1) * 100
        button1 = controller.get_button(pg.CONTROLLER_BUTTON_A)  
        button2 = controller.get_button(pg.CONTROLLER_BUTTON_B)  
    
        
        message = f"{int(x):03},{int(y):03},{button1},{button2}"
        client_socket.sendto(message.encode(), server_address)
        

        # 20 actions per second
        time.sleep(0.05)  

        
except KeyboardInterrupt:   
    print("AAAAAAAAAAA")
finally:
    client_socket.close()
    pg.quit()