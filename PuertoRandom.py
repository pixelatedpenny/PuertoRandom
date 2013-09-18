import sys
import random

class Building:
	def __init__(self, n, c, e, b):   #Constructor
		self.name = n                 #Name
		self.cost = c                 #Cost
		self.expansion = e            #Expansion (1 = new buildings, 2 = nobles)
		self.blacklist = b            #Not Allowed with this building

def main():
	argv = sys.argv
	argv.pop(0)
	expansions = ["0"]
	if len(argv) > 0:
		for expansion in argv:
			expansions.extend(expansion)
	else:
		expansions.extend("1")
		
	buildings = [Building("Aqueduct",1,1,""),
				Building("Small Market",1,0,""),
				Building("Black Market",2,1,""),
				Building("Construction Hut",2,0,""),
				Building("Forest House",2,1,"Hacienda"),
				Building("Hacienda",2,0,"Forest House"),
				Building("Land Office",2,2,""),
				Building("Small Warehouse",3,0,""),
				Building("Storehouse",3,1,""),
				Building("Chapel",3,2,""),
				Building("Guesthouse",4,1,""),
				Building("Hospice",4,0,""),
				Building("Hunting Lodge",4,2,""),
				Building("Church",5,1,""),
				Building("Office",5,0,"Trading Post"),
				Building("Large Market",5,0,""),
				Building("Trading Post",5,1,"Office"),
				Building("Zoning Office",5,2,""),
				Building("Large Warehouse",6,0,""),
				Building("Small Wharf",6,1,""),
				Building("Royal Supplier",6,2,""),
				Building("Factory",7,0,"Specialty Factory"),
				Building("Lighthouse",7,1,""),
				Building("Villa",7,2,"Jeweler"),
				Building("Harbor",8,0,""),
				Building("Library",8,1,""),
				Building("Jeweler",8,2,"Villa"),
				Building("Specialty Factory",8,1,"Factory"),
				Building("University",8,0,""),
				Building("Union Hall",9,1,""),
				Building("Wharf",9,0,""),
				Building("City Hall",10,0,""),
				Building("Cloister",10,1,""),
				Building("Customs House",10,0,""),
				Building("Fortress",10,0,""),
				Building("Guild Hall",10,0,""),
				Building("Residence",10,0,""),
				Building("Statue",10,1,""),
				Building("Royal Garden",10,2,"")]

	while True:
		selected_buildings = []
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 1 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 2 and str(b.expansion) in expansions], 2))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 3 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 4 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 5 and str(b.expansion) in expansions], 2))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 6 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 7 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 8 and str(b.expansion) in expansions], 2))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 9 and str(b.expansion) in expansions], 1))
		selected_buildings.extend(random.sample([b for b in buildings if b.cost == 10 and str(b.expansion) in expansions], 5))
		
		selected_names = [b.name for b in selected_buildings]
		selected_blacklists = [b.blacklist for b in selected_buildings]
		
		if len(set(selected_names).intersection(set(selected_blacklists))) < 1:
			break
	
	for building in [b for b in selected_buildings if b.expansion == 0]:
		print(str(building.cost) + " - " + building.name)
	print()	
	for building in [b for b in selected_buildings if b.expansion == 1]:
		print(str(building.cost) + " - " + building.name)
	print()	
	for building in [b for b in selected_buildings if b.expansion == 2]:
		print(str(building.cost) + " - " + building.name)
		
if __name__ == "__main__":
    main()