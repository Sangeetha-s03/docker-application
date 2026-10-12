from pydantic import EmailStr, TypeAdapter, ValidationError

# Built once and reused, so we don't rebuild the validator on every keystroke
email_adapter = TypeAdapter(EmailStr)


def validate_username(value):
    if not value or not value.strip():
        return "Email or username is required"
    if "@" in value:
        try:
            email_adapter.validate_python(value.strip())
        except ValidationError:
            return "Enter a valid email address"
    return None


def validate_password(value):
    if not value:
        return "Password is required"
    return None