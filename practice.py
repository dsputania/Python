rain_check = ""
while rain_check != "no":
    print("Good morning! Please go to your office.")

    rain_check = input("Is it raining outside? (yes/no): ").lower().strip()
    if rain_check == "yes":


        umbrella_check = input("Do you have an umbrella? (yes/no): ").lower().strip()
        if umbrella_check == "yes":
            print("GO OUTSIDE.")
            break

        else:
            print("WAIT A WHILE")


            while True:
                rain_check_again = input("Is it still raining? (yes/no) : ").lower().strip()
                if rain_check_again == "yes":
                    print("WAIT FOR SOME MORE TIME")
                else:
                    print("GO OUTSIDE")
                    break

    else:
        print("GO OUTSIDE")
        break













