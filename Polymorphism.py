#parent class
class Plants:
    common_name="Unknown"
    scientific_name= "Unknown"
    native_regions = "Unknown"
    common_uses = "Unknown"

    def information(self):
        msg= '\nCommon Name: {}\nScientific Name: {}\nNative Regions: {}\nCommon Uses: {}'.format(self.common_name, self.scientific_name, self.native_regions, self.common_uses)
        return msg
    


#Child Class instance
class Trees(Plants):
    common_name='Oak'
    scientific_name= 'Quercus'
    native_regions = "North Temperate zone and at high altitude in the tropics"
    common_uses = "Building and constructing furniture"
    
    def information(self):
        msg= 'Oak is any of about 450 species of ornamental and timber trees and shrubs constituting the genus Quercus in the beech family. It is a common source of ink and cork production in some countries.'
        return msg
    
#Child class instance
class Herbs(Plants):
    common_name='Basil'
    scientific_name='Oscumum basilicum'
    native_regions ='Tropical regions from central Africa to Southeast Asia'
    common_uses = 'used in cuisine worldwide'

    def information(self):
        msg= '\nSauces\nSoups\nPesto\nPizza'
        return msg

if __name__ == "__main__":
    a=Trees()
    b=Herbs()
    print(a.information())
    print(b.information())

    
    
