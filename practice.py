while True:
    print("Good morning! Please go to your office.")
    rain_check = input("Is it raining outside?: ").strip().lower()
    if rain_check == "no":
        print("GO OUTSIDE")
        break
    elif rain_check == "yes":
        while True:
            umbrella_check = input("Do you have an umbrella?: ").strip().lower()
            if umbrella_check == "yes":
                print("GO OUTSIDE")
                exit()
            elif umbrella_check == "no":
                while True:
                    print("Wait for sometime and watch NETFLIX.")
                    rain_check2 = input("Is it still raining?: ").strip().lower()
                    if rain_check2 == "no":
                        print("GO OUTSIDE")
                        exit()
                    elif rain_check2 == "yes":
                        continue
                    else:
                        print("Please reply in yes or no only.")
            else:
                print("Please reply in yes or no only.")
    else:
        print("Please reply in yes or no only.")







































