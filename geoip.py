import re
from argparse import ArgumentParser as AP
from ip2geotools.databases.noncommercial import DbIpCity

'''
Geo IP, get basic geo data on an IP address (Color removed for platform latency)
- Version: 0.1
- Author: Mach.3306
'''

class App:
    
    def __init__(self) -> None:
        self.__APP__ = "Geo IP"
        self.__VERSION__ = "0.1"
        self.__AUTHOR__ = "Mach.3306"
        self.__DESC__ = """
        Geo IP, get basic geo data on an IP address
        """
        
    def put_banner(self):
        print(f"{"#" * 35}\n** Version: {self.__VERSION__}\t\t **\n** Description: {self.__DESC__}\t\t **\n{"#" * 35}"); pass
    

class Checks:
    def __init__(self, ip_address=None, host_url=None) -> None:
        pass

class Geo:
    
    def __init__(self, ip_address) -> None:
        self.addr = ip_address
        self.drv = DbIpCity.get(ip_address=self.addr, api_key="free")
    
    def get_geo_data(self, _code):
        # Check to see if the IP address is up
        
        """Gets basic GEO data on an IP address

        Args:
            _code (character): The GEO code. _c = Country, _C = City, _r = Region, _l = Latitude, _L = Longitude
        """
        match _code:
            case "_c":
                # Get City of address
                print(f"=> [City] {self.addr} resides in: [{self.drv.city}] ..."); pass
            
            case "_C":
                # Get Country of address
                print(f"=> [Country] {self.addr} resides in: [{self.drv.country}] ..."); pass
                
            case "_r":
                # Get Region of address
                print(f"=> [Region] {self.addr} resides in: [{self.drv.region}] ..."); pass
                
            case "_l":
                # Get latitude data
                print(f"=> [Latitude] {self.addr} resides at: [{self.drv.latitude}] ..."); pass
                
            case "_L":
                # Get longitude data
                print(f"=> [Longitude] {self.addr} resides at: [{self.drv.longitude}] ..."); pass


def main():
    # Parser driver
    parse = AP(usage="python3 geoip.py -i <IP Address} [OPTIONS]", conflict_handler="resolve")
    parse.add_argument("-i", '--ip-address', type=str, metavar="", required=True, dest="_ip_addr", help="The address to probe.")
    parse.add_argument('--check-addr', action="store_true", dest="_check_addr", help="Check if the address responds to a connection.")
    parse.add_argument("-v", '--version', action="store_true", dest="_ver", help="Print version and exit")
    parse.add_argument("-b", '--banner', action="store_true", dest="_banner", help="Print a banner and exit")
    
    # Basic GEO group
    ag1 = parse.add_argument_group("Basic GEO Options")
    ag1.add_argument("-c", '--city', action='store_true', dest="_city", help="Get city name")
    ag1.add_argument("-C", '--country', action="store_true", dest="_country", help="Get country name")
    ag1.add_argument("-r", '--region', action="store_true", dest="_region", help="Get region name")
    ag1.add_argument("-l", '--latitude', action="store_true", dest="_lat", help="Get latitude coordinate")
    ag1.add_argument("-L", '--longitude', action="store_true", dest="_lon", help="Get longitude coordinate")
    
    args = parse.parse_args()
    geo = Geo(ip_address=args._ip_addr)
    app = App()
    
    if args._banner:
        app.put_banner(); pass
    
    if args._ip_addr:
        if args._city:
            geo.get_geo_data("_C"); pass
        
        if args._country:
            geo.get_geo_data("_c"); pass
            
        if args._region:
            geo.get_geo_data("_r"); pass
            
        if args._lat:
            geo.get_geo_data("_l"); pass
            
        if args._lon:
            geo.get_geo_data("_L"); pass
            


main()