
def GetData(Image_path,imgToFind):
    import cv2
    import numpy as np
    import os
    import shutil
    import glob
    imageNames=[]
    Coords=[]
    numOfCorrectImages=0
    D = "C:\\Users\\Fletcher\\Desktop\\ComapreIMGdir"
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

    # Iterate over each image extension and delete the files
    for extension in image_extensions:
        # Get a list of all files in the directory with the current extension
        files = glob.glob(os.path.join(D, extension))
        for file in files:
            # Delete the file
            os.remove(file)
            print(f"Deleted {file}")
    def find_squares(image_path):
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image at path {image_path} not found.")
            
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise and improve edge detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Perform Canny edge detection
        edges = cv2.Canny(blurred, 50, 150)
        
        # Find contours in the edge-detected image
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        squares = []
        
        for i, contour in enumerate(contours):
            # Approximate the contour to a polygon
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            
            # A square should have 4 vertices
            if len(approx) == 4:
                # Check if the approximated contour is convex
                if cv2.isContourConvex(approx):
                    # Calculate the bounding rectangle for the approximated contour
                    (x, y, w, h) = cv2.boundingRect(approx)

                    area = w * h
                    # Check if the bounding rectangle is approximately square (aspect ratio ~ 1) and area is over 4000 pixels
                    if 0.9 <= float(w) / h <= 1.1 and area > 4000:
                        
                        Coords.append([x, y])
                        print(Coords[0])
                        squares.append(approx)
                        
                        # Save the square as a separate image
                        square_image = image[y:y+h, x:x+w]
                        
                        output_path = f'C:\\Users\\Fletcher\\Desktop\\ComapreIMGdir\\square_{i}.jpg'  # Unique filename for each square
                        imageNames.append(output_path)
                        cv2.imwrite(output_path, square_image)
        
        # Draw the squares on the original image
        for square in squares:
            cv2.drawContours(image, [square], -1, (0, 255, 0), 3)
        
        # Save and/or display the image with squares highlighted
        output_path = 'squares_detected.jpg'
        cv2.imwrite(output_path, image)
        return squares

    
    squares = find_squares(image_path=Image_path)
    print(f"Found {len(squares)} squares.")
    import cv2
    import numpy as np
    import os
    def mse(startImg, img1):
        if len(startImg.shape) >2:
            startImg = cv2.cvtColor(startImg, cv2.COLOR_BGR2GRAY)
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        h, w = startImg.shape
        diff = cv2.subtract(startImg, img1)
        err = np.sum(diff**2)
        mse = err/(float(h*w))
        return mse, diff
    KnownFolderDir = r"C:\Users\Fletcher\Desktop\DataForCointiply"
    UnknownFolderDir=r"C:\Users\Fletcher\Desktop\ComapreIMGdir"
    comarisonImages=[]

    for images in os.listdir(UnknownFolderDir):
    
        # check if the image ends with jpg
        if (images.endswith(".jpg")):
            comarisonImages.append(images)
            print(images)
    click_image=False
    all_MSE=[]
    findLowest=False
    for i in comarisonImages:
        if numOfCorrectImages !=0:
            break
        image = cv2.imread(os.path.join(UnknownFolderDir, i))
        compareImage=cv2.imread(os.path.join(KnownFolderDir, imgToFind)+".jpg")
        if image.shape==compareImage.shape:
            MSE, diff = mse(image,compareImage)
            print(f"MSE for {i} is {MSE}")
            all_MSE.append(MSE)

            if MSE <1:
                click_image=True
                numOfCorrectImages+=1
                print("I found it")
                print(f"Image {i} is {imgToFind}")
                Click_coords=Coords[comarisonImages.index(i)]
                findLowest=False
                return click_image,Click_coords
            if numOfCorrectImages==0:
                findLowest=True
    if findLowest:
        print("The image you are looking for is not in the folder")
        print(f"The image with the lowest MSE is {comarisonImages[all_MSE.index(min(all_MSE))]} with a MSE of {min(all_MSE)}")
        Click_coords=Coords[comarisonImages.index(comarisonImages[all_MSE.index(min(all_MSE))])]
        return click_image,Click_coords
            
            
        

#click_image,Click_coords = GetData(Image_path = r"C:\Users\Fletcher\Pictures\Screenshots\Screenshot (140).png",imgToFind="carrot")

