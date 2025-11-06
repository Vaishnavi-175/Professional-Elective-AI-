
print("---- Career Guidance Expert System ----")

interest = input("What is your main interest? (science/arts/commerce): ").lower()

if interest == "science":
    subject = input("Do you like computers or biology? ").lower()
    if subject == "computers":
        print("You can choose a career in Software Engineering or Data Science.")
    elif subject == "biology":
        print("You can choose a career in Medicine or Biotechnology.")
    else:
        print("You can explore Engineering or Research fields.")

elif interest == "arts":
    talent = input("Do you like writing, painting, or teaching? ").lower()
    if talent == "writing":
        print("You can become a Journalist or Author.")
    elif talent == "painting":
        print("You can become a Designer or Artist.")
    elif talent == "teaching":
        print("You can become a Professor or School Teacher.")
    else:
        print("You can explore Humanities or Languages.")

elif interest == "commerce":
    skill = input("Do you like accounting, business, or finance? ").lower()
    if skill == "accounting":
        print("You can become a Chartered Accountant.")
    elif skill == "business":
        print("You can become an Entrepreneur or Business Analyst.")
    elif skill == "finance":
        print("You can work in Banking or Investment.")
    else:
        print("You can explore Management or Marketing careers.")

else:
    print("Invalid input. Please choose from science, arts, or commerce.")

print("\nThank you for using the Career Guidance Expert System!")