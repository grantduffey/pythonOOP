class Person:
    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone
      self.friends = []
      self.greeting_count = 0
      self.greeted_friends = []
      self.unique_greeting_count = 0
      
      
    def __str__(self):
     return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
      print('Hello %s, I am %s!' % (other_person.name, self.name))
      self.greeting_count += 1
      if other_person not in self.greeted_friends: 
          self.unique_greeting_count += 1
          self.greeted_friends.append(other_person)
      
    def print_greeting_count (self):
      print("Greet count for %s: %d" % (self.name, self.greeting_count))
      
    def print_contact_info(self):
        print("%s's email: %s\n%s's Phone Number: %s" % (self.name, self.email, self.name, self.phone))
        
    def add_friend(self, friend):
        self.friends.append(friend)
        
    def num_friends(self):
        return len(self.friends)
    
    def print_num_unique_people_greeted(self):
        print("%s's unique greetings: %d" % (self.name, self.unique_greeting_count))
    
        
      
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
jordan.add_friend(sonny)
sonny.add_friend(jordan)

sonny.greet(jordan)
jordan.greet(sonny)
sonny.greet(jordan)
sonny.print_greeting_count()
jordan.print_greeting_count()
sonny.print_num_unique_people_greeted()

sonny.print_contact_info()
jordan.print_contact_info()

print("%s's number of friends: %d" % (sonny.name, sonny.num_friends()))

print(jordan)

# print("Sonny's email: %s\nSonny's Phone Number: %s" % (sonny.email, sonny.phone))
# print("Jordan's email: %s\Jordan's Phone Number: %s" % (jordan.email, jordan.phone))

