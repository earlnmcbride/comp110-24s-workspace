""""Practice Writing A Twitter Profile Class."""

# definition
class Profile: 
    
    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create new profile"""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None: 
        """If Profile is NOT Private, print msg."""
        if self.private is False: 
            print(msg)

# instatiation
user1: Profile = Profile("110_rulez") # __init__
user1.private = False
user1.tweet("OOP is cool!")





    