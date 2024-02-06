class NationalPark:
  all = []
  def __init__(self, name):
    self.name = name
    NationalPark.all.append(self)
  
  @property
  def name(self):
    return self._name   
  @name.setter
  def name(self, name):
    if type(name) is str and 3 <= len(name) and not hasattr(self,"name"):
      self._name = name
    return
    
  def trips(self):
    return [trips for trips in Trip.all if trips.national_park == self]
    
  def visitors(self):
    return list({i.visitor for i in self.trips()})
    
  def total_visits(self):
    return len(self.trips())
    
  def best_visitor(self):
    # Returns the Visitor instance that has visited that park the most
    # Returns None if the park has no visitors
    visitors = [trip.visitor for trip in self.trips()]
    return max(set(visitors), key = visitors.count)


class Trip:
  all = []
  def __init__(self, visitor, national_park, start_date, end_date):
    self.visitor = visitor
    self.national_park = national_park
    self.start_date = start_date
    self.end_date = end_date
    Trip.all.append(self)
  
  @property
  def start_date(self):
    return self._start_date
  @start_date.setter
  def start_date(self, start_date):
    if type(start_date) is str and 7 <= len(start_date):
      self._start_date = start_date
      
  @property
  def end_date(self):
    return self._end_date
  @end_date.setter
  def end_date(self, end_date):
    if type(end_date) is str and 7 <= len(end_date):
      self._end_date = end_date
  
  @property
  def national_park(self):
    return self._national_park
  @national_park.setter
  def national_park(self, national_park):
    if isinstance(national_park, NationalPark):
      self._national_park = national_park

  @property
  def visitor(self):
    return self._visitor
  @visitor.setter
  def visitor(self, visitor):
    if isinstance(visitor, Visitor):
      self._visitor = visitor


class Visitor:
  all = []
  def __init__(self, name):
    self.name = name
    Visitor.all.append(self)
	
  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, name):
    if type(name) is str and 1 <= len(name) <= 15:
      self._name = name
    return
      

  def trips(self):
    #returns a list of all trips for that visitor
    return [i for i in Trip.all if i.visitor == self]
    
    
  def national_parks(self):
    # returns a unique list of all the national parks that a vistor has gone to. Uses the method above "self.trips()" to get all the trip data for that vistor.
    return list({i.national_park for i in self.trips()})
  
    
  def total_visits_at_park(self, park):
    if not park.visitors():
      return 0
    return len([trip for trip in self.trips() if trip.national_park == park])
      
  
np = NationalPark("under the sea")
print(np.name)
np.name = "over the sea"
print(np.name)
v1 = Visitor("Air-wreka")
print(v1.name)
t1 = Trip(v1, np, "September 11th", "September 12th")
print(t1.start_date)