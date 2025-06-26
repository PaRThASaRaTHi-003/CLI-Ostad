class Contact:
    valid_prfixes = {'013', '014', '015','016', '017', '018', '019'} #as Bangladeshi number starts with these prefixes

    def __init__(self, name, phone, email, address):
        if not name.replace(' ', ' ').isalpha():
            raise ValueError("Name must be alphabetic.")
        
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError("Phone number must be exactly 11 digits.")
        
        if phone[:3] not in Contact.valid_prfixes:
            raise ValueError(f"Phone number prefix must be one of: {', '.join(Contact.valid_prfixes)}.")
        
        if not self.valid_email(email):
            raise ValueError("Invalid email format. Must contain '@' and a domain like '.com'.")
        
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    @staticmethod
    def valid_email(email):
        if email.count("@") != 1:
            return False
        username, domain = email.split("@")
        if not username or "." not in domain:
            return False
        return True
    
    def listing(self):
        return [self.name, self.phone, self.email, self.address]
    
    def __str__(self): #special method for string conversion.
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"