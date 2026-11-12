class DatabaseConnection():
  def __init__(self,port,hostname,username,password):
    self.port = port
    self.hostname = hostname
    self.username = username
    self.password = password

connection = DatabaseConnection(5432,"localhost","postgres_user","user_password")
print(connection)
