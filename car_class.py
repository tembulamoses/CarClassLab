class Car(object):
	def __init__(self,name='General', model='GM', vehicle_type='None'):
		self.name = name
		self.speed = 0
		self.model = model
		self.vehicle_type = vehicle_type

		if self.name in ['Porshe', 'Koenigsegg']:
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4
		if self.vehicle_type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	def is_saloon(self):
		if self.vehicle_type is not 'trailer':
			self.vehicle_type == 'saloon'
			return True
		return False