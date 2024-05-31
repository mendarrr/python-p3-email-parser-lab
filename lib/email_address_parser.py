# your code goes here!
import re
class  EmailAddressParser:
    pattern =re.compile (r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z0-9+._-]+)')
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
        strings = re.split(r',|\s', self.input_string)
        parsed_emails=set()
        for string in strings:
            if self.pattern.fullmatch(string):
                parsed_emails.add(string)
        return sorted(list(parsed_emails))   
