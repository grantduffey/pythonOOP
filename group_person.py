# def create_person(name, email, phone):
#     person = {
#         "name": name,
#         "email": email,
#         "phone": phone,
#     }
#     return person

# def greet(person1, person2):
#     print('Hello {}, I am {}!'.format(person2["name"], person1["name"]))

# def print_contact_info(person):
#     print(f"{person['name']}'s email: {person['email']}, {person['name']}'s phone number: {person['phone']}")


# # Create people as dictionaries
# sonny = create_person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = create_person("Jordan", "jordan@aol.com", "495-586-3456")

# # Perform actions on people
# greet(sonny, jordan)
# greet(jordan, sonny)

# print_contact_info(sonny)

class Person():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def greet(self, person):
        print('Hello {}, I am {}!'.format(person.name, self.name))
        
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")
        
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()