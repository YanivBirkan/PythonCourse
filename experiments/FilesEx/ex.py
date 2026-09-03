
## ex- add hello to each file
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

## ex -read all content
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)



## ex - create a new file inside the journal lib by inputted date :
#  = input("Enter toady date : ")
# mood = input("How do you rate your mood? (1-10) : ")
# journal = input("Let your Thoughts flow : \n ")
#
# with open(f"./jounrnal/{date}.txt", "w") as file:
#     file.write(mood)
#     file.write(journal)

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for file in filenames:
    print((file.split(".")[0]).title())