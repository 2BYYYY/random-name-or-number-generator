import random 

choice = ("name","number")

while True:
    user = input("what do you want to generate? (name, number)")

    while user not in choice:
        print("try again...")
        user = input("what do you want to generate?")
#problem 1: indent of the while and if, that is why my code did not run
    if user == "name":
        first_name = ["Oliver",
                    "Charlotte",
                    "Declan", 
                    "Aurora",
                    "Theodore",
                    "Violet",
                    "Jasper",
                    "Hazel",
                    "Silas",
                    "Luna"]

        made_up_name = random.sample(first_name,3)

        string = " ".join(made_up_name)

        print(string)
    elif user == "number":
        inte = random.randint(1,1000)
        print(inte)
    break
print("thank you")


