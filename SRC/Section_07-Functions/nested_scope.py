def output_greeting(name):
    """Output a greeting for given name"""

    def set_greetings():
        """Set the greeting message"""
        message = f"Hello {name}"

    set_greetings()
    print(message)


output_greeting("mark")
