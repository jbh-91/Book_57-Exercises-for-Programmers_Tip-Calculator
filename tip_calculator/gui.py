import PySimpleGUI as sg
import tip_calculator as tc

layout = [[sg.Text("Please enter your bill amount:")],
          [sg.InputText(key='INPUT-BILL-AMOUNT')],
          [sg.Text("Please enter your tip rate:")],
          [sg.InputText(key='INPUT-TIP-RATE')],
          [sg.Text("How satisfied have you been with your server (in %)?")],
          # The range doesn't make any sense in this task, so i used ticks in 10 % intervals
          # [sg.Slider(range=(5,20), orientation="horizontal")],
          [sg.Slider(range=(0,100), tick_interval=20, orientation="horizontal", expand_x=True)],
          [sg.Text("Your tip has not been calculated", key='OUTPUT-TIP')],
          [sg.Text("Your total has not been calculated", key='OUTPUT-TOTAL')],
          [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Tip Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    bill_amount = tc.check_input(values['INPUT-BILL-AMOUNT'])
    tip_rate = tc.check_input(values['INPUT-TIP-RATE'], allow_zero=True)
    errors = []

    if bill_amount is False:
        errors.append("bill amount")
        window['INPUT-BILL-AMOUNT'].update("")
    if tip_rate is False:
        errors.append("tip rate")
        window['INPUT-TIP-RATE'].update("")

    if not errors:
        tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(bill_amount, tip_rate))
        total_amount = tc.calculate_total_amount(bill_amount, tip_amount)
        window['OUTPUT-TIP'].update(f"Your tip is {tip_amount:.2f} €")
        window['OUTPUT-TOTAL'].update(f"Your total is {total_amount:.2f} €")
    else:
        error_message = ["The following values are invalid"] + errors
        sg.popup_error("\n- ".join(error_message), title="Invalid values")

window.close()