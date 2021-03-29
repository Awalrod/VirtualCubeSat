import PySimpleGUI as sg
import os
import server.pythonserver as pyServ
import sys



sg.ChangeLookAndFeel('LightGreen')

column1 = [
            [sg.Text('COMMAND LOG:')],
            [sg.Output(size=(100,25))]
          ]

column2 = [
                [sg.Button(' POWER SYSTEM ON ')],
                [sg.Text('')],
                [sg.Button('POWER SYSTEM OFF',button_color = 'red')],
                [sg.Text('')],
                [sg.Text('_'*20)],
                [sg.Text('')],
                [sg.Text('')],
                [sg.Text('')],
                [sg.Text('')],
            ]


layout = [
            [sg.Column(column1),sg.Column(column2,element_justification='c')],
            [sg.Button('Exit')],
        ]


#

#callback function for server
def incoming_data(data):
	print(data)

# Create the window
window = sg.Window('GROUND STATION', layout,element_justification='r')

#Initialize server
ip = sys.argv[1]
port = int(sys.argv[2])
groundServer = pyServ.GroundServer(ip,port,incoming_data)


while True:
    event, values = window.read()
    if event == " POWER SYSTEM ON ":
        print("POWER SYSTEM ON")
        groundServer.startServer()
    if event == "POWER SYSTEM OFF":
        print("POWER SYSTEM OFF")
        groundServer.quit()
    if event == "SEND PULSE":
        print("SENDING INFORMATION PULSE")
    if event == "STOP PULSE":
        print("STOPPING INFORMATION PULSE")
    if event == "Exit" or event == sg.WIN_CLOSED:
        #add code for stopping info puleses to make sure it isn't left on
        groundServer.quit()
        break
