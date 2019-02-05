input("What is the title of the book? ")
input("Who is the author of the book? ")
input("When was the book published? ")
input("How many total pages does the book have? ")
pubyear = int(1982)
current_year =int(2019)
book_age = (current_year - pubyear)
if (book_age < 10):
    print("This book is younger than 10 years old. ")
else: 
    print("This book is at least 10 years old. ")
total_pages = int(200)
if (total_pages < 100):
    print("The book is a short book. ")
else:
    print("This book is a long book. " )