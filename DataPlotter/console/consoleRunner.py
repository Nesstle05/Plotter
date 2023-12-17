# console should be able to:
# - add points to the dataset (using addPointPopUp in popUpManager)
# - remove points from the dataset
# - trigger the calculation of the polynomial function
# - trigger the extrapolation of a point
# - change the mode of the dataset (line, dtm, none)
# - display the dataset
# - display the polynomial function
# - display the extrapolated point
# - trigger the calculation of the integral of the polynomial function
#
# Needed buttons:
# - add/remove points (select between add point, add multiple points from file, remove point)
# - calculate integral/derivative (select between them - change the mode of the api to line)
# - linreg (change the mode of the api to line)
# - see next predicted point (change the mode of the api to dtm)
# - extrapolate point (change the mode of the api to line)
#
# Data displaying:
# - when mode is none, display the points
# - when mode is line, display the points and the polynomial function
# - when mode is dtm, display the points

import PySimpleGUI as psg
from data_processing.processorAPI import ProcessorAPI
import console.popUpManager as popUp

def addPointPopUp_from_button():
    # Funcția care va fi apelată la apăsarea butonului "Button One"
    popUp.addPointPopUp()

def removePointPopUp_from_button():
    # Funcția care va fi apelată la apăsarea butonului "Button Two"
    popUp.removePointPopUp()

def addPlotMenuPopUp_from_button():
    popUp.addPlotMenuPopUp()


def runner():
    # Definirea aspectului ferestrei cu un element Text și un buton
    layout = [
        [psg.Text(text='Hello World',
                  font=('Arial Bold', 20),
                  size=20,
                  expand_x=True,
                  justification='center')],
        [psg.Button('Create Plot', key='-BUTTON_CREATE_PLOT-')],
        #[psg.Button('Add Point', key='-BUTTON_ONE-')],
        #[psg.Button('Remove Point', key='-BUTTON_TWO')],
        [psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-')],
        [psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-')],
        #[psg.Button('Linear Regression', key='BUTTON_FIVE')],
        [psg.Button('Next Predicted Point', key='-BUTTON_PREDICT_NEXT-')],
        [psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-')],
        [psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-')]

    ]
    popUp.welcomePopUp()

    # Crearea ferestrei PySimpleGUI
    window = psg.Window('HelloWorld', layout, size=(700, 700))

    # Crearea unei instanțe ProcessorAPI
    processor = ProcessorAPI()

    # Bucla principală de evenimente
    while True:
        event, values = window.read()

        if event in (None, 'Exit'):
            break
        elif event == '-BUTTON_CREATE_PLOT-':
            #layout.append([psg.Button('Add Point', key='-BUTTON_ADD_POINT-')]),
            #layout.append([psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-')]),
            #layout.append([psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-')]),
            layout1 = [
                [psg.Text(text='Hello World',
                          font=('Arial Bold', 20),
                          size=20,
                          expand_x=True,
                          justification='center')],
                [psg.Button('Add Point', key='-BUTTON_ADD_POINT-')],
                [psg.Button('Remove Point', key='-BUTTON_REMOVE_POINT-')],
                [psg.Button('Linear Regression', key='-BUTTON_LINEAR_REGRESSION-')],
                [psg.Button('Return', key='-BUTTON_RETURN-')]
            ]

            #window.finalize()
            window = psg.Window('HelloWorld', layout1, size=(700, 700))

            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == '-BUTTON_ADD_POINT-':
                    addPointPopUp_from_button()
                elif event == '-BUTTON_REMOVE_POINT-':
                    removePointPopUp_from_button()
                elif event == 'BUTTON_RETURN-':
                    break
            window.close()

            layout = [
                [psg.Text(text='Hello World',
                          font=('Arial Bold', 20),
                          size=20,
                          expand_x=True,
                          justification='center')],
                [psg.Button('Create Plot', key='-BUTTON_CREATE_PLOT-')],
                # [psg.Button('Add Point', key='-BUTTON_ONE-')],
                # [psg.Button('Remove Point', key='-BUTTON_TWO')],
                [psg.Button('Calculate Integral', key='-BUTTON_CALCULATE_INTEGRAL-')],
                [psg.Button('Calculate Derivative', key='-BUTTON_CALCULATE_DERIVATIVE-')],
                # [psg.Button('Linear Regression', key='BUTTON_FIVE')],
                [psg.Button('Next Predicted Point', key='-BUTTON_PREDICT_NEXT-')],
                [psg.Button('Extrapolate Point', key='-BUTTON_EXTRAPOLATE_POINT-')],
                [psg.Button('Display Dataset', key='-BUTTON_DISPLAY_DATASET-')]
            ]

            window = psg.Window('HelloWorld', layout, size=(700, 700))

    # Închiderea ferestrei la finalul buclei
    window.close()

if __name__ == '_main_':
    runner()