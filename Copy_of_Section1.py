def main():
    months_list = ['NOV', 'DEC', 'JAN', 'FEB']
    #complete the main method
    filename = input("Enter a filename: ")
    print("NZ-resident traveller arrivals")
    print()

    try:
        #Do not use the file pathway when submiting the code below, Leave only filename.
        with open(filename, "r") as file:
            region_info = file.read().strip().split(":")
            display_continent = Continent(region_info[0])

            for region_sub_info in region_info[1].split(","):
                region_sub_info = region_sub_info.split("-")
                display_continent.process(region_sub_info[0], region_sub_info[1], months_list)
                
            print(display_continent)
            
                
    except FileNotFoundError:
        print(f"File {filename} not found.")
    

#Copy the classes here
class Arrival:

    def __init__(self, month = "JAN", number_of_arrivals = 0):
        self.month = month
        self.number_of_arrivals = number_of_arrivals

    def get_number_of_arrivals(self):
        return (self.number_of_arrivals)
        
    def get_month(self):
        return (self.month)
    
    def __str__(self):
        return (f"{self.get_month()}:{self.get_number_of_arrivals():>7}")
    
    
    
class Region:
    
    def __init__(self, region_name, region_code, months_list, arrivals_list = None):
        self.region_name = region_name
        self.region_code = region_code
        if arrivals_list == None:
            self.arrivals_list = []
        self.process(months_list)

        

    def get_arrivals_list(self):
        return (self.arrivals_list)
                

    def add_arrival(self, month, value):
        self.arrivals_list.append(Arrival(month, value))
    
    
    def get_total_number_of_arrivals(self):
        total = 0
        
        for arrival in self.arrivals_list:
            total += arrival.get_number_of_arrivals()
            
        return (total)
            
        
    def __str__(self):
        stats_list = ("\t").join([arrival.__str__() for arrival in self.arrivals_list])

        return(f"{self.region_code}({self.get_total_number_of_arrivals()})\t{stats_list}")
    
    
    def process_data_per_month(self, month_name):

        filename = (str(self.region_code) + "_" + str(month_name) + ".txt") 
        with open(filename, "r") as file:
            data = file.read().split("\n")
            
            total_arrivals = 0
            for number in data:
                number = int(number)
                total_arrivals += number
            
        self.arrivals_list.append(Arrival(month_name, total_arrivals))


    def process(self, months_list):
        
        for month in months_list:
            self.process_data_per_month(month)


class Continent:

    def __init__(self, name, regions_list = None):
        self.name = name
        if regions_list == None:
            self.regions_list = []

    def process(self, region_name, region_code, months_list):
        self.regions_list.append(Region(region_name, region_code, months_list))

    def get_regions_list(self):
        return self.regions_list
    
    def get_total_arrivals(self):

        total_arrivals = 0
        for region_object in self.regions_list:
            total_arrivals += region_object.get_total_number_of_arrivals() 
        return total_arrivals
    
    def __str__(self):
        formated_list = [region_object.__str__() for region_object in self.regions_list]
        formated_list = "\n".join(formated_list)
        return(f"{self.name}(Total: {self.get_total_arrivals()})\n{''.join(formated_list)}")
    

    main()
    