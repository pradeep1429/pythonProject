
import db


class PasswordGenerator:
    def generate(self):
      # Code logic to generate password
      pass

class WriteData:
  def write(self, password):
    with db.session() as session:
      session.insert({"password": password})

class PasswordSaver:
    def __init__(self, generator: PasswordGenerator, writer: WriteData):
      self._generator = generator
      self._writer = writer
    def save(self):
      password = self._generator.generate()
      self._writer.write(password)


ps = PasswordSaver(PasswordGenerator(), WriteData())
ps.save()