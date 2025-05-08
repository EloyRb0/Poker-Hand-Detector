import cv2
import numpy as np



def isolateFigure(card, card_val):

    height, width = card.shape[:2]
    edges = cv2.Canny(card, 150, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_dist_x = float('inf')
    min_dist_y = float('inf')
    FigureX = 0
    FigureY = 0

    for contour in contours:
        for point in contour:
            x, y = point[0]
        
            # Distancia a (width, 0)
            dist_x = np.hypot(x - width, y - 0)
            if dist_x < min_dist_x:
                min_dist_x = dist_x
                FigureX = x

            # Distancia a (0, height)
            dist_y = np.hypot(x - 0, y - height)
            if dist_y < min_dist_y:
                min_dist_y = dist_y
                FigureY = y

    print(FigureX, FigureY)

    if(card_val == 'K' or card_val == 'Q' or card_val == 'J'):

        x2 =  FigureX -3
        x1 = FigureX - 45

        y1 = FigureY + (height-FigureY-31) - 50
        y2 = FigureY + (height-FigureY-30)

        #Assures to not surpass card limits
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = min(x2, card.shape[1])
        y2 = min(y2, card.shape[0])

        #Returns the cuted figure
        return card[y1:y2, x1:x2]
    else:

        horizontalDiff = 70 - abs(width/2 - FigureX)

        if(horizontalDiff > 50):
            x2 = FigureX + abs(45 - abs(horizontalDiff))
            x1 = FigureX - abs(45 - abs(45 - abs(horizontalDiff)))
            print(x2,x1)
        else:
            x2 =  FigureX + (70 - abs(100 - FigureX))
            x1 = FigureX - abs(45 - abs(70 - abs(100 - FigureX)))

        y1 = FigureY + (-65 +height - FigureY - 30)
        y2 = FigureY + (height-FigureY-30)

        #Assures to not surpass card limits
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = min(x2, card.shape[1])
        y2 = min(y2, card.shape[0])

        #Returns the cuted figure
        return card[y1:y2, int(x1):int(x2)]


def detectSuit (card,card_val):
    img = card
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(img, 100, 200)  # Lower and upper thresholds
    cv2.imshow('edges.jpg', edges)

    suitRegion = isolateFigure(blur,card_val)
    cv2.imshow('card', suitRegion)




    cv2.waitKey(0)
    cv2.destroyAllWindows()
