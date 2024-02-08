from abc import ABC, abstractmethod

import db
class PasswordSaver:

  def generate_password(self):
    # code for password functionality
    pass

  def upload(self, password):
    # code logic to upload it in s3 bucket.
    pass

  def write_db(self, password):
    with db.session() as session:
        session.insert({"password": password})

  def write_secret(self, password):
      # code logic to write in secret service.
      pass
  def save(self, **kwargs):
    password = self.generate_password()
    if kwargs.get("cloud"):
      self.upload(password)
    elif kwargs.get("secret"):
        self.write_secret(password)
    else:
      self.write_db(password)

# client code
ps = PasswordSaver()
ps.save(cloud=True)
ps_db = PasswordSaver()
ps_db.save()

# This class works but in future if we need to add more functionality,
# we need to keep on adding conditions and modify 'save' method which is a violtion

class Iwriter(ABC):
    @abstractmethod
    def write(self,password):
        raise NotImplementedError

class CloudWriter(Iwriter):
    def write(self,password):
        pass
class DataWriter(Iwriter):
    def write(self,password):
        pass


class SecretWriter(IWriter):
    def write(self, password):
        # code logic to write it in secret service
        pass


class IGenerator(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplementedError


class PasswordGenerator(IGenerator):
    def generate(self):
        # Code logic to generate password
        pass


class PasswordSaver:

    def __init__(self, generator, writer):
        self._generator = generator
        self._writer = writer

    def save(self):
        password = self._generator.generate()
        self._writer.write(password)

ps = PasswordSaver(PasswordGenerator(), CloudWriter())
ps.save()
ps_db = PasswordSaver(PasswordGenerator(), DataWriter())
ps_db.save()
ps_secret = PasswordSaver(PasswordGenerator(), SecretWriter())
ps_secret.save()