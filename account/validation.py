def validate_data(password, repass):
    if password != repass:
        return False
    return True