#import tkinter
from tkinter import *
#import ImageTk and Image from Pillow
from PIL import ImageTk, Image

#create root for gui
root = Tk()
root.title('Meat Guy Pricing Tool')
root.geometry("500x400")

#Labels describing to the user how to use the program/tool.
welcomeLabel = Label(root, text = "Welcome to the Meat Guy Pricing Tool")
welcomeLabel.grid(row = 0, column = 2)

stepsLabel = Label(root, text = "Please follow the steps below.")
stepsLabel.grid(row = 1, column = 2)

step1 = Label(root, text = "Step 1: ")
step1.grid(row = 3, column = 1)

selectLabel = Label(root, text = "Select the meat from the cooler.")
selectLabel.grid(row = 3, column = 2)

ribMeat = Label(root, text = "We have Ribeye Steaks")
ribMeat.grid(row = 4, column = 2)

#ribeye image resized and added alternate text
ribImage = Image.open("Ribeye.jpeg")
resized = ribImage.resize((120,100), Image.ANTIALIAS)
ribImage2 = ImageTk.PhotoImage(resized)
imageLabelr = Label(image=ribImage2, text="Ribeye Steak")
imageLabelr.grid(row = 4, column = 3)

#continued description of tool for user
nyMeat = Label(root, text = "We have New York Strip Steaks")
nyMeat.grid(row = 5, column = 2)

#newyork strip image resized and added alternate text
nyImage = Image.open("Newyork.jpeg")
resizedn = nyImage.resize((120,100), Image.ANTIALIAS)
nyImage2 = ImageTk.PhotoImage(resizedn)
imageLabelny = Label(image=nyImage2, text="New York Stip Steak")
imageLabelny.grid(row = 5, column = 3)

#continued description of tool for user
step2 = Label(root, text = "Step 2: ")
step2.grid(row = 7, column = 1)

weightLabel = Label(root, text = "Take the meat to the weighing counter.")
weightLabel.grid(row = 7, column = 2)

scaleLabel = Label(root, text = "Weigh each meat on the scale.")
scaleLabel.grid(row = 8, column = 2)

step3 = Label(root, text = "Step 3: ")
step3.grid(row = 9, column = 1)

returnLabel = Label(root, text = "Return to this station and press the NEXT button.")        
returnLabel.grid(row = 9, column = 2)

#function to open new window
def open():
    calc = Toplevel()
    calc.title('Calculator')
    calc.geometry("1300x500")
    titleLabel = Label(calc, text = "Meat Guy Pricing Tool Calculator")
    titleLabel.grid(row = 0, column = 5)

    #Labels with more instructions for user.
    instructLabel = Label(calc, text = 'Please enter in the weight of each meat you are purchasing.')
    instructLabel.grid(row = 3, column = 5)

    instructLabel2 = Label(calc, text = 'Round to the nearest pound in each entry.')
    instructLabel2.grid(row = 4, column = 5)

    spaceLabel = Label(calc, text = '                                                                                                            ')
    spaceLabel.grid(row = 5, column = 5)

    ribLabel = Label(calc, text = "      Ribeye Steak Weight:       ")
    ribLabel.grid(row = 6, column = 1)

    #Entry for user to enter weight of ribeye steaks
    ribEntry = Entry(calc, width = 12)
    ribEntry.grid(row = 6, column = 2)
    ribEntry.insert(0, "0")

    nyWeight = Label(calc, text = "      New York Strip Steak Weight:       ")
    nyWeight.grid(row = 6, column = 6)

    #Entry for user to enter weight of newyork strip steaks
    nyEntry = Entry(calc, width = 12)
    nyEntry.grid(row = 6, column = 7)
    nyEntry.insert(0, "0")
    
    #function giving subtotal button the subtotal for ribeyes entered
    def ribClick():
        x = ribEntry.get()
        global ribSub
        global ribSub2
        #if else statement to make sure user entry is a whole number.
        if x.isdigit():
            rib = int(x) * 16
            ansRib = "Your Subtotal is: $" + str(rib)
            ribSub = Label(calc, text=ansRib)
            ribSub.grid(row = 7, column = 1)
            ribSub2 = Label(calc, text="")
            ribSub2.grid(row=8, column = 1)
        else:
            ribSub = Label(calc, text="     Incorrect Amount.    ")
            ribSub.grid(row = 7, column = 1)
            ribSub2 = Label(calc, text="Click CLEAR and try again.")
            ribSub2.grid(row=8, column = 1)

    #function giving subtotal button the subtotal for newyork strips enetered
    def nyClick():
        y = nyEntry.get()
        global nySub
        global nySub2
        #if else statement to make sure user entry is a whole number.
        if y.isdigit():
            ny = int(y) * 13
            ansNy = "  Your Subtotal is: $" + str(ny) + "  "
            nySub = Label(calc, text=ansNy)
            nySub.grid(row = 7, column = 6)
            nySub2 = Label(calc, text="")
            nySub2.grid(row=8, column = 6)
        else:
            nySub = Label(calc, text="    Incorrect amount.   ")
            nySub.grid(row = 7, column = 6)
            nySub2 = Label(calc, text="Click CLEAR and try again.")
            nySub2.grid(row=8, column = 6)

    #giving clear button power to remove subtotal or error message for ribeyes
    def ribDelete():
        ribSub.grid_forget()
        ribSub2.grid_forget()
    #giving clear button power to remove subtotal or error message for newyork strip
    def nyDelete():
        nySub.grid_forget()

    #subtotal button for ribeye
    ribButton = Button(calc, text = "SUBTOTAL", command = ribClick)
    ribButton.grid(row = 6, column = 3)

    #clear button for ribeye
    ribClear = Button(calc, text = "CLEAR", command = ribDelete)
    ribClear.grid(row = 6, column = 4)

    #subtotal button for newyork strip
    nyButton = Button(calc, text = "SUBTOTAL", command=nyClick)
    nyButton.grid(row = 6, column = 8)

    #clear button for newyork strip
    nyClear = Button(calc, text = "CLEAR", command = nyDelete)
    nyClear.grid(row = 6, column = 9)

    finishLabel = Label(calc, text = 'Click the TOTAL button below to total up your purchase.')
    finishLabel.grid(row = 9, column = 5)

    #function giving power to total button to total up price of meats or show error messages.
    def totalClick():
        x = ribEntry.get()
        y = nyEntry.get()
        global totalLabel
        global totalLabel2
        global clerkLabel
        global thanksLabel
        global haveLabel
        #if else to make sure entry for ribeye is an integer
        if x.isdigit():
            rib = int(x) * 16
            #if else to make sure entry for newyork is an integer
            if y.isdigit():
                ny = int(y) * 13
                totalPrice = rib + ny
                #if else to make sure a weight has been entered in for either meat.
                if totalPrice > 0:
                    ansTotal = "The Total Price for Your Purchase Today is: $" + str(totalPrice)
                    totalLabel = Label(calc, text=ansTotal)
                    totalLabel.grid(row = 11, column = 5)
                    totalLabel2 = Label(calc, text='')
                    totalLabel2.grid(row = 12, column = 5)
                    clerkLabel = Label(calc, text="Please show the clerk this total to check out.")
                    clerkLabel.grid(row = 13, column = 5)
                    thanksLabel = Label(calc, text="Thank you for using Meat Guy Pricing Tool!")
                    thanksLabel.grid(row = 14, column = 5)
                    haveLabel = Label(calc, text="Have a great day!")
                    haveLabel.grid(row = 15, column = 5)
                else:
                    totalLabel = Label(calc, text="Please enter a weight above to get a total price.")
                    totalLabel.grid(row = 11, column = 5)
                    totalLabel2 = Label(calc, text='')
                    totalLabel2.grid(row = 12, column = 5)
                    clerkLabel = Label(calc, text="")
                    clerkLabel.grid(row = 13, column = 5)
                    thanksLabel = Label(calc, text="")
                    thanksLabel.grid(row = 14, column = 5)
                    haveLabel = Label(calc, text="")
                    haveLabel.grid(row = 15, column = 5)
            else:
                totalLabel = Label(calc, text='Error! You entered an incorrect amount for New York Strip Steaks.')
                totalLabel.grid(row = 11, column = 5)
                totalLabel2 = Label(calc, text='Click CLEAR TOTAL and try again.')
                totalLabel2.grid(row = 12, column = 5)
                clerkLabel = Label(calc, text="")
                clerkLabel.grid(row = 13, column = 5)
                thanksLabel = Label(calc, text="")
                thanksLabel.grid(row = 14, column = 5)
                haveLabel = Label(calc, text="")
                haveLabel.grid(row = 15, column = 5)
        else:
            totalLabel = Label(calc, text='Error! You entered an incorrect amount for Ribeye Steaks.')
            totalLabel.grid(row = 11, column = 5)
            totalLabel2 = Label(calc, text='Click CLEAR TOTAL and try again.')
            totalLabel2.grid(row = 12, column = 5)
            clerkLabel = Label(calc, text="")
            clerkLabel.grid(row = 13, column = 5)
            thanksLabel = Label(calc, text="")
            thanksLabel.grid(row = 14, column = 5)
            haveLabel = Label(calc, text="")
            haveLabel.grid(row = 15, column = 5)
    #function to give clear total power to remove total price or error messages
    def totalDelete():
        totalLabel.grid_forget()
        totalLabel2.grid_forget()
        clerkLabel.grid_forget()
        thanksLabel.grid_forget()
        haveLabel.grid_forget()
    
    #total button
    totalButton = Button(calc, text = "TOTAL", command=totalClick)
    totalButton.grid(row = 10, column = 4)

    #clear total button
    totalClear = Button(calc, text = "CLEAR TOTAL", command=totalDelete)
    totalClear.grid(row = 10, column = 6)

    #function to give go back and finish button power to go back to first page
    def close():
        calc.destroy()

    #go back button
    backButton = Button(calc, text = 'GO BACK', command=close)
    backButton.grid(row = 16, column = 1)

    #finish button
    finishButton = Button(calc, text = 'FINISH', command=close)
    finishButton.grid(row = 16, column = 8)

#next button to advance to calculator window
nextButton = Button(root, text="NEXT", command=open)
nextButton.grid(row = 10, column = 5)

root.mainloop()
