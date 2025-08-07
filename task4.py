class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        real_hours = self.get_hours()
        return  real_hours * self.hourly_payment
