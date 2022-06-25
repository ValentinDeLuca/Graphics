"""This program generates a .txt file with every Hex color. One per line."""

HEX = "0123456789abcdef"
FILENAME_OUTPUT = "colors.txt"
def main():
    with open(FILENAME_OUTPUT, "w") as otp:
        for i in HEX:
            for ii in HEX:
                for iii in HEX:
                    for iv in HEX:
                        for v in HEX:
                            for vi in HEX:
                                 otp.write(f"#{i}{ii}{iii}{iv}{v}{vi}\n")


if __name__ == '__main__':
    main()
