# regex_pattern = r",|\."	# Do not delete 'r'.
regex_pattern = r"[,.]"    
import re
print("\n".join(re.split(regex_pattern, input())))