import scratchattach as scratch

session = scratch.login("your_username", "your_password")  # or use scratch.Session("your_session_id")
cloud = session.connect_cloud("PROJECT_ID")  # replace with your actual project ID

word = input("Enter a word to send to Scratch: ")

# Encode string into ASCII numbers (Scratch cloud only supports numbers)
for i, char in enumerate(word[:128]):
    cloud.set_var(f"char_{i}", ord(char))
cloud.set_var("length", len(word))

print("Word sent to Scratch cloud variables.")
