def authentication(auth, role, user_role):
    if auth is True:
        if role == user_role:
            return True
        else:
            return False, "invalid_user"
    else:
        return False, "not_login"
