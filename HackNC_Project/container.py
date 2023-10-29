import datetime

class Container:
  def __init__(self,med_name : str = [], open_by : datetime.datetime = datetime.datetime.now()):
    self.med_name = med_name
    self.open = False
    self.open_by = open_by

  def __str__(self):
    return "medicine name: %s is open:%s open by:%s"%(self.med_name, self.open, self.open_by)

  def med_late(self):
    return self.open_by < datetime.datetime.now()
  
  def is_open(self):
    return self.open

  def open_container(self):
    if self.open:
      return "container is already open"
    else:
      self.open = True
      return self.med_name
  def close_container(self):
    if self.open:
      self.open = False
      return "Door Closed"
    else:
      return "Door is already closed"

  def insert_medicine(self, medicine):
    if self.open:
      self.med_name.append(medicine)
      return "Medicine inserted"
    else:
      return "door is closed. Operation failed."

  def remove_medicine(self):
    if self.open:
      tmp = self.med_name
      self.med_name = []
      return tmp
    else:
      return "Door is closed. Operation failed."
  
  def time_until_due(self):
    return datetime.datetime.now() - self.open_by