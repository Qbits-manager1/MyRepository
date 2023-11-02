import PySimpleGUI as sg
import csv

def verify_credentials(acc_no, pin):
  # open the file in read mode
  filename = open('credentials.csv', 'r')
  # create dictreader object to read the data from file
  file = csv.DictReader(filename) 
  # iterate over each row and append values to empty list
  for col in file:
    if col['Account number'] == acc_no and col['PIN'] == pin :
        return True     
  return False

def login_screen():
  sg.theme('DarkTeal12')   # Add a touch of color
  # All the stuff inside your window.
  layout = [  [sg.Text('ATM system',size=(15,2),font=('Arial',25),justification='center')],
              [sg.Text('Enter account number:',size=(20,2)), 
               sg.Input(key='acc_number', size=(10, 2), do_not_clear=True, font=('Arial', 16))],
              [sg.Text('Enter PIN:',size=(20,2)), 
               sg.Input(key='pin',password_char="*", size=(10, 2), do_not_clear=True,font=('Arial', 16))],
              [sg.Text('',size=(10,2)),sg.Button('Sign in'), sg.Button('Cancel') ]]
  

  # Create the Window
  window = sg.Window('Login', layout)  
  
  # Event Loop to process "events" and get the "values" of the inputs
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Sign in":
      acc_number = values['acc_number']
      pin = values['pin']            

      if verify_credentials(acc_number,pin):                                  
        window.close()
        main_screen(acc_number,pin)
      else:
        sg.popup("Check your account number and PIN", background_color='grey', title='Error')
        window['acc_number'].update("")
        window['pin'].update("")
        window['acc_number'].Widget.focus()
  window.close()

def main_screen(acc_no,pin):
  sg.theme('DarkTeal12')   # Add a touch of color
  # All the stuff inside your window.
  layout = [  [sg.Text('ATM system',size=(20,2),font=('Arial', 25),justification='center')],
              [sg.Button('Check Balance',size=(20,2)), sg.Button('Change PIN',size=(20,2)) ],
              [sg.Button('Withdraw Amount',size=(20,2)), sg.Button('Transfer Funds', size=(20,2))],
              [sg.Button('Deposit Amount',size=(20,2)), sg.Button('Transaction History', size=(20,2))],
              [sg.Text('',size=(15,2)), sg.Button('Logout', size=(10,2)) ]]

  # Create the Window
  window = sg.Window('Main Screen', layout)
  # Event Loop to process "events" and get the "values" of the inputs
  while True:
    event, values = window.read()
    balance = 0
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
      break

    if event == "Logout":
      window.close()
      login_screen()  

  window.close()

login_screen()
