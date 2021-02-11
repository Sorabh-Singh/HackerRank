'''
Enter Your Email: support@thecleverprogrammer.com
Your user name is ‘support’ and your domain is ‘thecleverprogrammer.com’
'''
# My Approach:

user_input = input("Enter Your Email: ").rstrip()
user_name, user_domain = user_input.split('@')
print(f"Your user name is '{user_name}' and your domain is ‘{user_domain}’")


# Other Approach:
email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)