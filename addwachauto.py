from data import GetData
import pyautogui
import cv2
import os 
from time import sleep
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
from random import *
from PIL import Image
def JustClick(text_to_find,screenshot_filename):
    try:
            # Apply thresholding to the image
            img = Image.open(screenshot_filename)
            gray = img.convert('L')
            threshold = 127
            binary = gray.point(lambda x: 255 if x > threshold else 0)

            # Save the thresholded image to a new file
            thresholded_filename = 'thresholded.png'
            binary.save(thresholded_filename)

            # Read the text from the thresholded image using OCR
            text = pytesseract.image_to_string(thresholded_filename, lang='eng').lower()
            coords=[]
            # Check if the specific line of text is found
            if text_to_find.lower() in text:
                print(f"Found '{text_to_find}' in the screenshot!")

                # Get the x and y coordinates of the text
                data = pytesseract.image_to_data(thresholded_filename, output_type=pytesseract.Output.DICT)
                for i, word in enumerate(data['text']):
                    if word.lower() == text_to_find.lower():
                        x = data['left'][i]
                        y = data['top'][i]

                        break

                # Click on the text
                pyautogui.moveTo(x, y,uniform(0.6, 2.7), pyautogui.easeOutQuad)
                pyautogui.click()
                print("Clicked on the text.")
                return x,y
            else:
                print(f"'{text_to_find}' not found in the screenshot.")
                return False
    finally:
        # Delete the screenshot and thresholded files
        os.remove(screenshot_filename)
        os.remove(thresholded_filename)
        try: 
            return x,y
        except:
            pass
def SCforData():

    
    TestIMG=pyautogui.screenshot('screenshot.png')
    TestIMG.save
    Text=pytesseract.image_to_string(TestIMG)
    os.remove('screenshot.png')
    return Text
def check_screenshot_for_text_and_click(text_to_find):
    # Take a screenshot using pyautogui

    image = pyautogui.screenshot("screenshot.png")
    # Save the screenshot to a file
    screenshot_filename = 'screenshot.png'
    image.save(screenshot_filename)

    try:
        # Apply thresholding to the image
        img = Image.open(screenshot_filename)
        gray = img.convert('L')
        threshold = 127
        binary = gray.point(lambda x: 255 if x > threshold else 0)

        # Save the thresholded image to a new file
        thresholded_filename = 'thresholded.png'
        binary.save(thresholded_filename)

        # Read the text from the thresholded image using OCR
        text = pytesseract.image_to_string(thresholded_filename, lang='eng').lower()
        coords=[]
        # Check if the specific line of text is found
        if text_to_find.lower() in text:
            print(f"Found '{text_to_find}' in the screenshot!")

            # Get the x and y coordinates of the text
            data = pytesseract.image_to_data(thresholded_filename, output_type=pytesseract.Output.DICT)
            for i, word in enumerate(data['text']):
                if word.lower() == text_to_find.lower():
                    x = data['left'][i]
                    y = data['top'][i]

                    break

            # Click on the text
            pyautogui.moveTo(x, y,uniform(0.6, 2.7), pyautogui.easeOutQuad)
            pyautogui.click()
            print("Clicked on the text.")
            return x,y
        else:
            print(f"'{text_to_find}' not found in the screenshot.")
            return False
    finally:
        # Delete the screenshot and thresholded files
        os.remove(screenshot_filename)
        os.remove(thresholded_filename)
        try: 
            return x,y
        except:
            pass
def check_screenshot_for_exact_text_and_click(text_to_find):
        # Take a screenshot using pyautogui

    image = pyautogui.screenshot("screenshot.png")
    # Save the screenshot to a file
    screenshot_filename = 'screenshot.png'
    image.save(screenshot_filename)

    try:
        # Apply thresholding to the image
        img = Image.open(screenshot_filename)
        gray = img.convert('L')
        threshold = 127
        binary = gray.point(lambda x: 255 if x > threshold else 0)

        # Save the thresholded image to a new file
        thresholded_filename = 'thresholded.png'
        binary.save(thresholded_filename)

        # Read the text from the thresholded image using OCR
        text = pytesseract.image_to_string(thresholded_filename, lang='eng').lower()
        coords=[]
        # Check if the specific line of text is found
        if text_to_find in text:
            print(f"Found '{text_to_find}' in the screenshot!")

            # Get the x and y coordinates of the text
            data = pytesseract.image_to_data(thresholded_filename, output_type=pytesseract.Output.DICT)
            for i, word in enumerate(data['text']):
                if word == text_to_find:
                    x = data['left'][i]
                    y = data['top'][i]

                    break

            # Click on the text
            pyautogui.moveTo(x, y,uniform(0.6, 2.7), pyautogui.easeOutQuad)
            pyautogui.click()
            print("Clicked on the text.")
            return x,y
        else:
            print(f"'{text_to_find}' not found in the screenshot.")
            return False
    finally:
        # Delete the screenshot and thresholded files
        os.remove(screenshot_filename)
        os.remove(thresholded_filename)
        try: 
            return x,y
        except:
            pass
def TopScreenAnalize(Img_Path):
    image = cv2.imread(Img_Path)  # Replace with your image path

    # Check if image reading was successful
    if image is None:
        print("Error: Could not read the image.")
    else:
        # Get the height of the image
        height = image.shape[0]

        # Crop the image to the top 300 pixels
        if height > 300:
            cropped_image = image[0:50, :]  # Crop from row 0 to 300 (exclusive), and all columns
            cv2.imwrite("cropped_image.png", cropped_image)  # Save the cropped image
numofTimeWatched=0
closeButton=[621,23]
MainPAgeCoords=[201,26]
Stop=False
numofTimeWatched=[]
ClickedOnAdd=True
WatchedAddAndWaited = False
def SCforTopImageData():
    pyautogui.screenshot("img.png")
    TopScreenAnalize("img.png")
    data = pytesseract.image_to_string("cropped_image.png")
    os.remove("img.png")
    os.remove("cropped_image.png")
    return data
def TimeLeftLogic():
    print(numofTimeWatched)
    new_sc = pyautogui.screenshot("img.png")
    TopScreenAnalize("img.png")
    TopImgData = pytesseract.image_to_string("cropped_image.png")
    print("Found left should be waiting")
    SumStuffToComaper=TopImgData.split(" ")
    print(f"stuff to compare: {SumStuffToComaper} \n Top Image Data: {TopImgData}")
    os.remove("img.png")
    os.remove("cropped_image.png")
    if "seconds" in TopImgData.lower():
        try:
            numberToSleep=SumStuffToComaper.index("Seconds")
            print(f"Sleeping: {int(SumStuffToComaper[numberToSleep-1])} seconds")
            sleep(int(SumStuffToComaper[numberToSleep-1])+1)
            numofTimeWatched.append(int(SumStuffToComaper[numberToSleep-1]))
            return True
        except:
            numberToSleep=SumStuffToComaper.index("seconds")
            print(f"Sleeping: {int(SumStuffToComaper[numberToSleep-1])} seconds")
            sleep(int(SumStuffToComaper[numberToSleep-1])+1)
            numofTimeWatched.append(int(SumStuffToComaper[numberToSleep-1]))
            return True
Accounts=[[695,1052],[749,1050]]
ChangeAccount=False
#The positions of the Cointiply page and the cose button to exit out of the code
closeButton=[621,23]
MainPAgeCoords=[201,26]
while True:
    sleep(1)
    data = SCforData()
    TippityTopData=SCforTopImageData()
    print(f"Data: {data}")
    if 'left' in TippityTopData:
        print("running time left logic line 115")
        WatchedAddAndWaited=TimeLeftLogic()
    if WatchedAddAndWaited == True:
        new_sc = pyautogui.screenshot("img.png")
        TopScreenAnalize("img.png")
        TopImgData2 = pytesseract.image_to_string("cropped_image.png")
        print("Watched Add and Waited is true")
        print(TopImgData2)
        if "complete" in TopImgData2.lower():
            pyautogui.click(closeButton[0],closeButton[1])
            sleep(1)
            ultamateImage=pyautogui.screenshot("ultamateImage.jpg")
            ultamateImage.save
            print("ready to add MSE Bullshit")
            NewData=SCforData()
            print(f"New data: {NewData}\n Split data: {NewData.split()}")
            split_new_data=NewData.split()
            if 'select:' in NewData.lower():
                try:
                    what_to_select=split_new_data.index("Select:")
                except:
                    what_to_select=split_new_data.index("select:")
            else:
                try:
                    what_to_select=split_new_data.index("select")
                except:
                    what_to_select=split_new_data.index("Select")
            print(f"What to select: {split_new_data[what_to_select+1]}")
            try:
                click_image,Click_coords = GetData(Image_path = r'ultamateImage.jpg',imgToFind=split_new_data[what_to_select+1].lower())
            except:
                sleep(3)
                click_image,Click_coords = GetData(Image_path = r'ultamateImage.jpg',imgToFind=split_new_data[what_to_select+1].lower())
            print(f"click coords: {Click_coords}")
            pyautogui.moveTo(Click_coords[0]+20, Click_coords[1]+20,uniform(0.6, 2.7), pyautogui.easeOutQuad)
            pyautogui.click()
            
        if "complete" not in TopImgData2.lower():
            print("Watched Add it is not complete retrying")
            pyautogui.click(closeButton[0],closeButton[1])
            sleep(1)
            try:
                check_screenshot_for_text_and_click("retry")
                sleep(1)
                check_screenshot_for_text_and_click("skip")
            except:
                pass
        os.remove('img.png')
        os.remove('cropped_image.png')
        WatchedAddAndWaited=False
    if WatchedAddAndWaited==False:
        if "ptc" in data.lower():
                check_screenshot_for_text_and_click("view")
            
        if "viewing" in data.lower():
            ClickedOnAdd=True
        if ClickedOnAdd:
            ClickedOnAdd=True
            sleep(4)
            new_sc = pyautogui.screenshot("img.png")
            TopScreenAnalize("img.png")
            TopImgData = pytesseract.image_to_string("cropped_image.png")
            print(TopImgData)
            if "rewards" in TopImgData.lower():
                    pyautogui.click(closeButton[0],closeButton[1])
            if "left" in TopImgData.lower():
                print("running left logic line 152")
                WatchedAddAndWaited=TimeLeftLogic()
            if "complete" in TopImgData.lower():
                print("Watched Add it is complete")
                pyautogui.click(closeButton[0],closeButton[1])
                WatchedAddAndWaited=True
