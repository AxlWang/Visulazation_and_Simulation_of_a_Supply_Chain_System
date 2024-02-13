
class Store(object):
	"""docstring for ClassName"""
	def __init__(self, longitude, latitude, rank, dc, store_id):
		self.longitude = longitude
		self.latitude = latitude
		self.rank = rank
		self.dc = dc
		self.id = store_id
		self.soh = 0
		self.marker = 'o'
		self.color = 'Blue'

	def soh_ch(self, qty):
		self.soh = qty

	def marker_ch(self, m):
		self.marker = m

	def color_ch(self, c):
		self.color = c



	




		
