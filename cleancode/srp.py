
import db

class PasswordSaver:
  def generate_password(self):
    # code for password functionality
    pass
  def save(self):
    password = self.generate_password()
    with db.session() as session:
      session.insert({"password": password})

ps = PasswordSaver()
ps.save()

# The class has two responsibilities which violates single resp principle

class PasswordGenerator:
    def generate(self):
      # Code logic to generate password
      pass

class WriteData:
  def write(self, password):
    with db.session() as session:
      session.insert({"password": password})

class PasswordSaver:
    def __init__(self, generator, writer):
      self._generator = generator
      self._writer = writer
    def save(self):
      password = self._generator.generate()
      self._writer.write(password)

# Now PasswordGenerator takes care of managing the password and WriteData takes care of managing the database.
# The two classes are smaller, so they’re manageable.
# The PasswordSaver will not change for the new security requirements. It’s easier to test, debug and maintain.
ps = PasswordSaver(PasswordGenerator(), WriteData())
ps.save()