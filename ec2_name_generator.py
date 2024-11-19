import random
import string

def generate_ec2_names():
    # Ask user for the department name
    department = input("Enter the name of your department: ").strip()

    # Ask how many EC2 names are needed
    while True:
        try:
            count = int(input("Enter the number of EC2 instance names you want: "))
            if count > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate unique EC2 names
    unique_names = set()
    while len(unique_names) < count:
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name = f"{department}-{random_suffix}"
        unique_names.add(ec2_name)

    # Display the generated names
    print("\nGenerated EC2 Instance Names:")
    for name in unique_names:
        print(name)
# Run the function when the script is executed
if __name__ == "__main__":
    generate_ec2_names()