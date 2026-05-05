import random

def generate_random_digits(length=9):
    return ''.join(str(random.randint(0, 9)) for i in range(length))

def main():
    ip = input("Enter IP: ")
    port = input("Enter port: ")
    user = input("Enter user: ")
    password = input("Enter password: ")
    count = int(input("How many proxies you want? "))

    filename = "bright-data-resi-proxy.txt"

    with open(filename, "w") as file:
        print("\nGenerated strings:")
        for i in range(count):
            rand_part = generate_random_digits()
            result = f"{ip}:{port}:{user}-session-{rand_part}:{password}"
            
            print(result)
            file.write(result + "\n")

    print(f"\n###########################################################################################\n")
    print(f"Ayooooo Nigerian, just generated {count} proxies for you")
    print(f"It's been saved to {filename}, and PLEASE, always test the proxy before you use it!")
    print(f"If you ask me how to navigate and open a txt file... I'll block you\n")
    print(f"###########################################################################################\n")

if __name__ == "__main__":
    main()