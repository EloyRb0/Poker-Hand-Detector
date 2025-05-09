import cv2
import numpy as np
import colorDetector

#Add templates for each suit
templates = {
    "h": [cv2.imread("./templates/heart1.png", 0), cv2.imread("./templates/heart2.png", 0), cv2.imread("./templates/heart3.png", 0), cv2.imread("./templates/heart4.png", 0), cv2.imread("./templates/heart5.png", 0), cv2.imread("./templates/heart6.png", 0)],
    "d": [cv2.imread("./templates/diamond1.png", 0), cv2.imread("./templates/diamond2.png", 0),cv2.imread("./templates/diamond3.png", 0)],
    "s": [cv2.imread("./templates/spade1.png", 0), cv2.imread("./templates/spade2.png", 0), cv2.imread("./templates/spade3.png", 0), cv2.imread("./templates/spade4.png", 0), cv2.imread("./templates/spade5.png", 0)],
    "c": [cv2.imread("./templates/club1.png", 0), cv2.imread("./templates/club2.png", 0), cv2.imread("./templates/club3.png", 0), cv2.imread("./templates/club4.png", 0), cv2.imread("./templates/club5.png", 0)],
}


def isolateFigure(card, card_val):
    height, width = card.shape[:2]
    edges = cv2.Canny(card, 150, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    FigureX, FigureY = 0, 0
    min_dist_x, min_dist_y = float('inf'), float('inf')

    for contour in contours:
        for point in contour:
            x, y = point[0]

            dist_x = np.hypot(x - width, y)
            if dist_x < min_dist_x:
                min_dist_x = dist_x
                FigureX = x

            dist_y = np.hypot(x, y - height)
            if dist_y < min_dist_y:
                min_dist_y = dist_y
                FigureY = y

    # print(FigureX, FigureY)

    if card_val in {'K', 'Q', 'J'}:
        x1, x2 = FigureX - 50, FigureX - 3
        y1, y2 = FigureY + height - FigureY - 86, FigureY + height - FigureY - 30
    if card_val in {'A'}:
        x1 = 30
        x2 = 170
        y1 = 60
        y2 = 250
    else:
        horizontal_diff = 70 - abs(width / 2 - FigureX)
        offset = abs(45 - abs(horizontal_diff)) if horizontal_diff > 50 else abs(45 - abs(70 - abs(100 - FigureX)))
        x1, x2 = FigureX - offset, FigureX + offset
        y1, y2 = FigureY + height - FigureY - 95, FigureY + height - FigureY - 30

    x1, x2 = max(x1, 0), min(x2, width)
    y1, y2 = max(y1, 0), min(y2, height)

    return int(y1), int(y2), int(x1), int(x2)


def detectSuit (card,card_val):
    img = card
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(img, 100, 200)
    # cv2.imshow('edges.png', edges)

    y1,y2,x1,x2 = isolateFigure(blur,card_val)

    suitRegion = img[y1:y2,x1:x2]

    # cv2.imshow('card', suitRegion)

    color = colorDetector.detectColor(suitRegion)

    suitRegion= cv2.cvtColor(suitRegion, cv2.COLOR_BGR2GRAY)


    bestMatch = None
    maxScore = -1

    # print(color)

    for suit, template in templates.items():
        if(color==1):
            if(suit == 'd' or suit == 'h'):
                for temp in template:
                    if len(temp.shape) == 3 and temp.shape[2] == 3:
                        tempGray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
                    else:
                        tempGray = temp
                    tempGray = cv2.resize(tempGray, (100, 100))
                    res = cv2.matchTemplate(suitRegion, tempGray, cv2.TM_CCOEFF_NORMED)
                    _, score, _, _ = cv2.minMaxLoc(res)
                    if score > maxScore:
                        maxScore = score
                        bestMatch = suit
        else: 
            if(suit=='c' or suit=='s'):
                for temp in template:
                    if len(temp.shape) == 3 and temp.shape[2] == 3:
                        tempGray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
                    else:
                        tempGray = temp
                    tempGray = cv2.resize(tempGray, (suitRegion.shape[1], suitRegion.shape[0]), interpolation=cv2.INTER_AREA)
                    res = cv2.matchTemplate(suitRegion, tempGray, cv2.TM_CCOEFF_NORMED)
                    _, score, _, _ = cv2.minMaxLoc(res)
                    if score > maxScore:
                        maxScore = score
                        bestMatch = suit


    # print(f"Figura reconocida: {bestMatch}")

    return bestMatch