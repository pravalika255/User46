"""User class module"""


class User:
    """Represents a GitHub user."""
    
    def __init__(self, username: str, email: str = None, bio: str = None):
        """
        Initialize a User instance.
        
        Args:
            username (str): The GitHub username.
            email (str, optional): The user's email. Defaults to None.
            bio (str, optional): The user's bio. Defaults to None.
        """
        self.username = username
        self.email = email
        self.bio = bio
    
    def __repr__(self) -> str:
        """Return a string representation of the User."""
        return f"User(username='{self.username}', email='{self.email}', bio='{self.bio}')"
    
    def __str__(self) -> str:
        """Return a human-readable string representation of the User."""
        return f"{self.username} ({self.email})"
    
    def get_profile_info(self) -> dict:
        """
        Get the user's profile information.
        
        Returns:
            dict: A dictionary containing username, email, and bio.
        """
        return {
            "username": self.username,
            "email": self.email,
            "bio": self.bio
        }
    
    def update_bio(self, new_bio: str) -> None:
        """
        Update the user's bio.
        
        Args:
            new_bio (str): The new bio text.
        """
        self.bio = new_bio


if __name__ == "__main__":
    # Example usage
    user = User("pravalika255", email="user@example.com", bio="GitHub user")
    print(user)
    print(user.get_profile_info())
    user.update_bio("Updated bio")
    print(user.get_profile_info())
