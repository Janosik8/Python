def main():
    print("Email slicer\n")

    email = input("Input your email for slicing: ")

    (username, domain) = email.split("@")
    number = domain.rfind(".")
    extension = domain[number+1:]
    domain = domain[0:number]

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    print("\n")
    main()