import PySimpleGUI as sg
import tip_calculator as tc

layout = [[sg.Text("Please enter your bill amount:")],
          [sg.InputText(key='INPUT-BILL-AMOUNT')],
          [sg.Text("Please enter your tip rate:")],
          [sg.InputText(key='INPUT-TIP-RATE')],
          [sg.Text("Your tip has not been calculated", key='OUTPUT-TIP')],
          [sg.Text("Your total has not been calculated", key='OUTPUT-TOTAL')],
          [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Tip Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    bill_amount = tc.check_input(values['INPUT-BILL-AMOUNT'])
    tip_rate = tc.check_input(values['INPUT-TIP-RATE'])

    # TODO: Check bill amount and tip rate independently and use an apropriate message
    if bill_amount:
        if tip_rate:
            tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(bill_amount, tip_rate))
            total_amount = tc.calculate_total_amount(bill_amount, tip_amount)
            window['OUTPUT-TIP'].update(f"Your tip is {tip_amount:.2f} €")
            window['OUTPUT-TOTAL'].update(f"Your total is {total_amount:.2f} €")
        else:
            sg.popup_error("Please enter a valid tip rate")
            window['INPUT-TIP-RATE'].update("")
    else:
        sg.popup_error("Please enter a valid bill amount")
        window['INPUT-BILL-AMOUNT'].update("")


window.close()