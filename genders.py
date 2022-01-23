    def is_male(gender):
        return gender == "male"

    def gender_print(male):
        if male:
            print("You are a male then aren't you")
        else:
            print("You are a female then aren't you")

    GENDERS = 'male', 'female'

    while True:  # infinite loop
        gender = input("What is your gender: ").strip().lower()
        if gender in GENDERS:
            male = is_male(gender)
            gender_print(male)
            break  # leave loop
        else:
            print("sorry User, my program only allows me to select")
            print("a gender either male or female for now, please try again.")
        # will return to top of loop from here