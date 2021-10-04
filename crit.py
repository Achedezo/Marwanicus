import PySimpleGUI as sg
import yaml


def formater_sortie():
    return(0)

def lire_data(nature,type,score):
    nat=nature[0:3]
    fichier = "data_crit/"+nat+type+".yaml"
    with open(fichier,"r") as f:
        texte=f.read()
        contenu = yaml.safe_load(texte)
    for i in contenu["vals"]:
        if score <= i:
            numero = contenu["vals"].index(i)
            break
    sortie = contenu["Descriptions"][numero]
    return(sortie)


def main():
    choix = ["Contondant", "Perforant", "Tranchant"]
    choixech = ["CaC","Distance","Déplacement"]

    layout = [  [sg.Text('Test de graphique')],
                [sg.Radio('Succes Critique',"Radio1",default = True,key='type_suc',enable_events=True),sg.Radio('Echec Critique',"Radio1",key='type_ech',enable_events=True)],
                [sg.Combo(choix,key='choix',readonly=True)],
                [sg.Text('Valeur du D100 de critique'), sg.InputText(key="val",default_text="50")],
                [sg.Text('Valeur du bonus de critique'), sg.InputText(key="bonus",default_text="0")],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Test Critique', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if values['type_suc']==True:
            window.Element('choix').Update(values=choix)
        if values['type_ech']==True:
            window.Element('choix').Update(values=choixech)
        if event == 'Ok':
            if values['type_suc']==True:
                valeur = "Succes"
            else:
                valeur = "Echec"
            val = int(values['val'])+int(values['bonus'])
            mess = lire_data(valeur,values["choix"],int(val))
            sg.popup_scrolled(mess,title="Résulat")
            print(mess)

    window.close()

main()
