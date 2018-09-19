# Get user email address
email = input("What is your email adress?: ").strip()
# Slice out the user name
user = email[:email.index("@")]
# Slice out the domain name
domain = email[email.index("@") + 1 :]
# Format message
output = "Your username is {} and your domain name is {}".format(user, domain)
# display output message
print(output)
