"""
from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

register_new_user("A", "BestPassword", "abc@gmail.com")

password_forgotten("abc@gmail.com")

upgrade_plan("abc@gmail.com")

"""