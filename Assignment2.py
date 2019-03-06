#Brennon Elder (30039898)
#Lab B04
#Assignment 2 (finished)

##program that creates either a bar graph or pie chart depending on users choice; allows user to choose
#settings such as the titles and intervals as well as size, label, and amount of bars/sectors

from SimpleGraphics import *   #imports entire simplegraphics library

print("Chart Creation Menu: " ,"1. Pie Chart"," 2. Bar Chart")   #tells user which number corresponds to which graph type
chartType = int(input("Select your chart type: "))               #obtains chart type from user

#if statement for when user inputs 1(pie graph)>> do everything indented below and skip second if statement
if chartType == 1:
    chartTitle = input("Enter the title of the chart: ")                     #obtains chart title from user
    sectors = int((input("Enter the number of sectors (2 to 6): ")))         #obtains number of sectors from user
    totalValue = float((input("Enter the total value of all sectors: ")))    #obtains total value of all sectors from user
    
    #constants for pie chart
    RADIUS = 460           #radius of entire pie chart
    SECTORSTARTX = 150     #x-coordinate for chart
    SECTORSTARTY = 90      #y-coordinate for chart
    TOTALDEG = 360         #total degrees in a circle
    DEGSTART = 0           #starting location for first sector
    RED = 255              #starting value of red intensity
    GREEN = 0              #value of green intensity
    BLUE = 0               #starting value of blue intensity
    LEGENDX = 700          #x-value of legend
    LEGENDY = 75           #starting y-value of legend

    #graph title specs
    setFont("Arial", "25", "bold")     #sets font and size of title
    text(390, 50, chartTitle)          #places title of graph above graph in middle
    
    #for loop creats number of sectors inputted, colour changes, and legend(text, spacing, coloured squares)
    for i in range(1, sectors + 1):                             #loops as many times as number of sectors inputted
        sectoriLabel = input("Label sector " + str(i) + ": ")   #gets user input to label each sector
        sectoriValue = float(input("Enter the value of the " + sectoriLabel + " sector: "))  #gets user input for value of each sector
        sectoriProp = float(sectoriValue / totalValue)          #calculates proportion of each sector
        sectoriAngle = float(sectoriProp * TOTALDEG)            #calculates angle of each sector
        setFill(RED, GREEN, BLUE)                               #sets colour of first sector 
        pieSlice(SECTORSTARTX, SECTORSTARTY, RADIUS, RADIUS, DEGSTART, sectoriAngle)         #draws each sector
        rect(LEGENDX, LEGENDY, 50, 50)                          #draws squares in legend with colours corresponding to chart
        setFont("Arial", "13")                                  #sets font style and size for legend
        text(LEGENDX, LEGENDY - 15, sectoriLabel, align="w")    #prints sector label next to corresponding colour in legend
        DEGSTART = DEGSTART + sectoriAngle                      #sets start of next sector at end of last sector
        RED = RED - 40                                          #decreases intensity of red for next bar                 
        BLUE = BLUE + 40                                        #increases intensity of blue for next bar   
        LEGENDY = LEGENDY + 90                                  #starts next legend segment directly below previous

#if statement for when user inputs 2(bar graph)>> do everything indented below
if chartType == 2:
    chartTitle = input("Enter the title of the chart: ")                #obtains chart title from user
    bars = int((input("Enter the number of bars (2 to 6): ")))          #obtains number of bars from user
    interval = int(input("Enter the gridline interval (10 to 100): "))  #obatins interval spacing amount from user
    yaxis = input("Enter the label for the y-axis: ")                   #obtains y-axis title from user
    
    #constants for bar chart
    BARWIDTH = 50           #width of each bar
    BARSTART = 150          #where first bar starts
    START_LINE = 490        #where first horizontal gridline starts
    TEXTRIGHT = 0           #starting number for gridline counter
    RED = 255               #starting value of red intensity
    GREEN = 0               #value of green intensity
    BLUE = 0                #starting value of blue intensity
    
    #variables regarding spacing 
    spacesE = int(bars + 1)                     #number of spaces is one greater than number of bars
    emptySpacing = int(600 - BARWIDTH*bars)     #total empty space between bars
    spaceWidth = emptySpacing / spacesE         #distance of empty space between each
    barSpacing = BARWIDTH + spaceWidth          #distance between left side of each bar
    spaces = int(400 / interval)                #number of spaces between gridline intervals inputted
    
    #y-axis title specs
    setFont("Arial", "16", "bold")     #sets font and size of text for y-axis
    text(50, 300, yaxis)               #places title of yaxis in the middle of the right side of graph  
    
    #graph title specs
    setFont("Arial", "27", "bold")     #sets font and size of title
    text(400, 50, chartTitle)          #places title of graph above graph in middle
    
    rect(100, 90, 600, 400)            #places rectangle as background for graph
    
    setFont("Arial", "12")             #sets font and size of labels and values of respective bar
    
    #for loop creates number of bars inputted, colour changes, and spacing; prints bar labels and bar values.
    for i in range(1, bars + 1):                           #loops as many times as user inputs number of bars
        bariLabel = input("Label bar " + str(i) + ": ")    #gets input to label each bar
        bariValue = int(input("Enter the value of the " + bariLabel + " bar: "))   #gets input for value of each bar
        setFill(RED, GREEN, BLUE)                          #sets color of first bar
        rect(BARSTART, 490, BARWIDTH, -bariValue)          #draws each bar equal distance away from each other
        text(BARSTART, 515, bariLabel, align="w")          #prints label below respective bar
        text(BARSTART, -bariValue + 500, bariValue, align="w")   #prints value of bar just below the top of respective bar
        BARSTART = BARSTART + barSpacing                   #sets next bar same distance away as last
        RED = RED - 40                                     #decreases intensity of red for next bar                 
        BLUE = BLUE + 40                                   #increases intensity of blue for next bar                 

    #for loop creates horizontal grid and number values of inputted intervals on right side of graph   
    for i in range(1, spaces + 2):               #loops through certain number of times depending on interval specififed by user
        line(100, START_LINE, 700, START_LINE)   #places horizontal gridlines as x-axis increments
        setFont("Arial", "10")                   #sets font of x-axis increments
        text(730, START_LINE, TEXTRIGHT)         #places respective gridnumbers next to x-axis lines along right side of graph
        START_LINE = START_LINE - interval       #starts next gridline the increment value away from previous
        TEXTRIGHT = TEXTRIGHT + interval         #starts next gridnumber the increment value away from previous

print("Your chart is completed.")                #prints "Your chart is completed."