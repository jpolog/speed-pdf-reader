import PySimpleGUI as sg

# Text that will be shown
dummyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet odio in tortor accumsan tempus. Mauris diam tortor, maximus in porta ac, gravida non arcu. Curabitur feugiat euismod nibh ac sollicitudin. Suspendisse ipsum turpis, congue id aliquam id, sodales at massa. Donec eu erat nec tortor fringilla volutpat in et nisl. Donec pulvinar sapien orci, eu fermentum tellus egestas gravida. Pellentesque vitae dignissim odio, vitae facilisis lorem. Donec aliquam consectetur metus, tempor tincidunt nunc elementum eu. Donec cursus pharetra lorem, eget facilisis tellus pellentesque ac. Vivamus eget ante sed dui placerat euismod. Vestibulum malesuada tellus ac odio posuere rhoncus." 
testList = dummyText.split(" ")

numWords = 2
wpm = 450
pace = (60000/wpm)*numWords

# Input text window
def textInWindow():
    layout = [[sg.Text('Enter the text:', font=('Helvetica', 15), justification='w')],
            [sg.VPush()],
            [sg.Push(), sg.Multiline(size=(80,40),autoscroll=False), sg.Push()],
            [sg.VPush()],
            [sg.Push(),sg.Button('Speed Read!', key='textInput'),sg.Push()],
            [sg.VPush()]]

    return sg.Window('Input your text', layout, resizable=True, size=(600, 750))

inputWindow = textInWindow()

event, values = inputWindow.read()
wordList = values[0].replace('\n\n','  ').replace('\n','').split(' ')
print(wordList)
wordCount=len(wordList)



inputWindow.close()


# RSVP text window
def RSVPWindow():
    
    layout = [[sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text(size=(50, 1), font=('Helvetica', 20), justification='center', key='text'), sg.Push()],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Button('Play', key='playPause'), sg.Button('Cancel'), sg.Push()],
            [sg.VPush()],
            [sg.Push(),sg.Text('WPM:\t'),sg.Input(str(wpm), size=10,),sg.Push()],
            [sg.VPush()]]

    return sg.Window('This is a test window', layout, resizable=True, size=(600, 300))

window = RSVPWindow()

# Utilities for buttons and text inputs
def playPause():
    if window['playPause'].get_text() == 'Pause':
        window['playPause'].update('Play')
    else:   # Resume playing
        window['playPause'].update('Pause')
        # Adjust new wpm if necessary
        wpm = int(values[0])
        global pace
        pace = (60000/wpm)*numWords


counter = 0 # To choose the word
# The main loop starts when play button is pressed
event, values = window.read()
if event == 'playPause':
    playPause()
else:
    exit()
while True:

    event, values = window.read(pace)
    if event == 'playPause':    # Play/Pause
        playPause()
        event, values = window.read()
        if event == 'playPause':
            playPause()
            continue
    if event in (sg.WIN_CLOSED, 'Cancel'):  # Close window
        break
    
    # Shows the chosen number of words at a time
    # TODO: Check for longer words to show independently (max char)
    words = ''
    for i in range(0,numWords):
        words += wordList[counter] + ' '
        counter+=1  
        if counter >= wordCount:    # The text is finished
            window['playPause'].update('Play')
            event, values = window.read()
            if event == 'playPause':    # Play from the beginnig
                playPause()
                event, values = window.read()
                if event == 'playPause':
                    playPause()
                    continue
            if event in (sg.WIN_CLOSED, 'Cancel'):  # Close window
                break

    window['text'].update(words)
        

    