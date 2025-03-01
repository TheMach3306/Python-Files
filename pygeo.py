from ip2geotools.databases.noncommercial import DbIpCity as DIP

class Geo:

    def __init__(self, ip_host_address: str, api_key: str = None):
        self.host = ip_host_address
        self.api = api_key
        self.resp = DIP.get(self.host, api_key=self.api)

    def get_geo(self, _key: str):
        """
        This function uses the basic non-commercial Database, it by no means retrieves data for ALL ip addresses
        and hostnames supplied to this class.

        :param _key:
                The key type to use to retrieve a specific data value. The '_key" begins with an underscore and ends
                with the value type character. (Examples):
                _c = City
                _C = Country
                _r = Region
                _l = Latitude
                _L = Longitude
                _j = JSON
                _x = XML
                _V = CSV
        :return:
            The data string for the requested key.
        """
        match _key:
            case '_c':
                # City
                return f"[+] '{self.host}' resides in [city]:\t {self.resp.city}"

            case '_r':
                # Region
                return f"[+] '{self.host}' resides in [region]:\t {self.resp.region}"

            case '_C':
                # Country
               return f"[+] '{self.host}' resides in [country]:\t {self.resp.country}"

            case '_l':
                # Latitude
                return f"[+] '{self.host}' resides in [latitude]:\t {self.resp.latitude}"

            case '_L':
                # Longitude
                return f"[+] '{self.host}' resides in [longitude]:\t {self.resp.longitude}"

            case '_j':
                # JSON
                return f"=>> Results in JSON Format:\n{'-' * 15}\n{self.resp.to_json()}\n{'-' * 15}"

            case '_x':
                # XML
                return f"=>> Results in XML Format:\n{'-' * 15}\n{self.resp.to_xml()}\n{'-' * 15}"

            case '_V':
                # CSV
                return f"=>> Results in CSV Format:\n{'-' * 15}\n{self.resp.to_csv()}\n{'-' * 15}"

            case _:
                pass