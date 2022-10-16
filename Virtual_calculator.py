import cv2
from cvzone.HandTrackingModule import HandDetector
import math


def virtual_calculator():
    class Button:
        def __init__(self, pos, width, height, value):
            self.pos = pos
            self.width = width
            self.height = height
            self.value = value

        def draw(self, img):
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (140, 0, 0))
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (0, 0, 0), 4)
            cv2.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 30), cv2.FONT_HERSHEY_PLAIN,
                        2, (255, 0, 0), 2)

        def check_click(self, x, y):
            if self.pos[0] < x < self.pos[0] + self.width and \
                    self.pos[1] < y < self.pos[1] + self.height:
                cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                              (250, 250, 250), cv2.FILLED)
                cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                              (0, 0, 0), 4)
                cv2.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 30), cv2.FONT_HERSHEY_PLAIN,
                            2, (0, 0, 0), 2)
                return True
            else:
                return False

    # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1350)
    cap.set(4, 1000)
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    # creating button
    button_list = [['C', 'CE', "sqrt", "+", "cos", "tan", "sin"],
                   ['7', "8", "9", "-", "acos", "asin", "atan"],
                   ["4", "5", "6", "*", 'cosh', 'tanh', "sinh"],
                   ["1", "2", "3", "/", "sec", "cosec", "cot"],
                   ["0", ".", "2^x", "=", "x^y", "x^2", "x^3"],
                   ["(", ")", "pi", "2pi", "|x|", "e^x", "1/x"],
                   ["e", "log10", "ln", "rad", "deg", "10^x", "x!"]]
    buttonList = []
    for x in range(7):
        for y in range(7):
            xpos = x * 120 + 300
            ypos = y * 50 + 200
            buttonList.append(Button((xpos, ypos), 120, 50, button_list[y][x]))

    my_equation = ""
    delay_counter = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        # detection of hand
        hands, img = detector.findHands(img, flipType=False)

        # draw all buttons
        cv2.rectangle(img, (300, 120), (500 + 640, 120 + 80), (0, 0, 0))
        cv2.rectangle(img, (300, 120), (500 + 640, 120 + 80), (0, 0, 0), 4)
        for button in buttonList:
            button.draw(img)

        # Check for Hand
        if hands:
            lmList = hands[0]["lmList"]
            length, _, img = detector.findDistance(lmList[8], lmList[12], img)
            x, y = lmList[8]
            if length < 50:
                for i, button in enumerate(buttonList):
                    if button.check_click(x, y) and delay_counter == 0:
                        my_value = (button_list[int(i % 7)][int(i / 7)])
                        try:
                            if my_value == 'C':
                                my_equation = my_equation[0:len(my_equation) - 1]
                            elif my_value == "CE":
                                my_equation = ""
                            elif my_value == "sqrt":
                                my_equation = round(math.sqrt(eval(str(my_equation))), 4)
                            elif my_value == 'pi':
                                my_equation = my_equation + str(round(math.pi, 4))
                            elif my_value == 'cos':
                                my_equation = round(math.cos(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == 'tan':
                                my_equation = round(math.tan(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == 'sin':
                                my_equation = round(math.sin(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == 'cosh':
                                my_equation = round(math.cosh(eval(str(my_equation))), 4)
                            elif my_value == 'tanh':
                                my_equation = round(math.tanh(eval(str(my_equation))), 4)
                            elif my_value == 'sinh':
                                my_equation = round(math.sinh(eval(str(my_equation))), 4)
                            elif my_value == "x^y":
                                my_equation = str(my_equation) + "**"
                            elif my_value == "x!":
                                my_equation = math.factorial(int(eval(str(my_equation))))
                            elif my_value == 'log10':
                                my_equation = round(math.log10(int(eval(str(my_equation)))), 4)
                            elif my_value == "ln":
                                my_equation = round(math.log(int(eval(str(my_equation)))), 4)
                            elif my_value == "=":
                                my_equation = round(float(eval(str(my_equation))), 4)
                            elif my_value == "e":
                                my_equation = my_equation + str(round(math.e, 4))
                            elif my_value == "2pi":
                                my_equation = str(my_equation) + str(round(2 * math.pi, 4))
                            elif my_value == "acos":
                                my_equation = round(math.acos((eval(str(my_equation)))), 4)
                            elif my_value == "asin":
                                my_equation = round(math.asin((eval(str(my_equation)))), 4)
                            elif my_value == "atan":
                                my_equation = round(math.atan((eval(str(my_equation)))), 4)
                            elif my_value == "sec":
                                my_equation = round(1 / math.cos(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == "cosec":
                                my_equation = round(1 / math.sin(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == "cot":
                                my_equation = round(1 / math.tan(math.radians(eval(str(my_equation)))), 4)
                            elif my_value == "e^x":
                                my_equation = str(my_equation) + str(round(math.e, 4)) + "**"
                            elif my_value == "2^x":
                                my_equation = str(my_equation) + "2**"
                            elif my_value == "x^2":
                                my_equation = round((float(eval(str(my_equation))) ** 2), 4)
                            elif my_value == "x^3":
                                my_equation = round((float(eval(str(my_equation))) ** 3), 4)
                            elif my_value == "|x|":
                                my_equation = round(math.fabs(float(eval(str(my_equation)))), 4)
                            elif my_value == "1/x":
                                my_equation = round(1 / float(eval(str(my_equation))), 4)
                            elif my_value == "10^x":
                                my_equation = str(my_equation) + "10**"
                            elif my_value == "rad":
                                my_equation = round(math.radians(float(eval(str(my_equation)))),4)
                            elif my_value == "deg":
                                my_equation = round(math.degrees(float(eval(str(my_equation)))), 4)
                            else:
                                my_equation = str(my_equation) + my_value
                        except ZeroDivisionError:
                            my_equation = "Division by 0 invalid"
                        except SyntaxError:
                            my_equation = "Syntax error"
                        except TypeError:
                            my_equation = "Type Error"
                        except ValueError:
                            my_equation = "Value Error "
                        delay_counter = 1

        # Avoid repitions:
        if delay_counter != 0:
            delay_counter += 1
            if delay_counter > 10:
                delay_counter = 0
        # Display equation
        cv2.putText(img, str(my_equation), (300 + 20, 120 + 50), cv2.FONT_HERSHEY_PLAIN,
                    2.5, (255, 0, 0), 2)

        # Display image
        cv2.imshow("image", img)

        key = cv2.waitKey(1)
        if key == ord("C"):
            cv2.destroyAllWindows()
            break

virtual_calculator()