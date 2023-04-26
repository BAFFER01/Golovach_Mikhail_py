import time
import os

dict = {
    0: ["■■■■■■■", "■■   ■■", "■■   ■■", "■■   ■■", "■■■■■■■"],
    1: [" ■■■■  ", "   ■■  ", "   ■■  ", "   ■■  ", " ■■■■■■"],
    2: [" ■■■■■ ", "■■   ■■", "    ■■ ", "  ■■   ", "■■■■■■■"],
    3: ["■■■■■■■", "     ■■", "■■■■■■■", "     ■■", "■■■■■■■"],
    4: ["■■   ■■", "■■   ■■", "■■■■■■■", "     ■■", "     ■■"],
    5: ["■■■■■■■", "■■     ", "■■■■■■■", "     ■■", "■■■■■■■"],
    6: ["■■■■■■■", "■■     ", "■■■■■■■", "■■   ■■", "■■■■■■■"],
    7: ["■■■■■■■", "     ■■", "     ■■", "     ■■", "     ■■"],
    8: ["■■■■■■■", "■■   ■■", "■■■■■■■", "■■   ■■", "■■■■■■■"],
    9: ["■■■■■■■", "■■   ■■", "■■■■■■■", "     ■■", "■■■■■■■"],
    10: ["      ", "  ■■  ", "      ", "  ■■  ", "      "],
}


def main():
    while True:
        local_time = time.localtime()
        formatted_hour = time.strftime("%H", local_time)
        formatted_min = time.strftime("%M", local_time)
        formatted_sec = time.strftime("%S", local_time)
        os.system("cls")
        for row in range(5):
            for digit in formatted_hour:
                if digit.isdigit():
                    print(dict[int(digit)][row], end="\t")
            print(dict[10][row], end="\t")
            for digit in formatted_min:
                if digit.isdigit():
                    print(dict[int(digit)][row], end="\t")
            print(dict[10][row], end="\t")
            for digit in formatted_sec:
                if digit.isdigit():
                    print(dict[int(digit)][row], end="\t")
            print()
        time.sleep(0.9)


main()
