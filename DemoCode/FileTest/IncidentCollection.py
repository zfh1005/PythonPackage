import gzip
import pickle
import os
import sys
import struct
import xml
from Incident import Incident

NumbersStruct = struct.Struct("<Idi?")

class IncidentCollection(dict):    
    
    def values(self):
        for report_id in self.keys():
            yield self[report_id]

    def items(self):
        for report_id in self.keys():
            yield (report_id, self[report_id])

    def __iter__(self):
        for report_id in sorted(super().keys()):
            yield report_id

    keys = __iter__

    def export_pickle(self, filename, compress = False):
        fh = None
        try:
            if compress:
                fh = gzip.open(filename, 'wb')
            else:
                fh = open(filename, 'wb')
            pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)#HIGHEST_PROTOCOL just used for Python 3.x
            return true
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: export error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_pickle(self, filename):
        fh = None
        try:
            fh = open(filename, 'rb')
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename, 'rb')
            else:
                fh.seek(0)
            self.clear()
            self.update(pickle.load(fh))
            return true
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    MAGIC = b'AIB\x00'
    FORMAT_VERSION = b'\x00\x01'          
    def export_binary(self, filename, compress = False):
        def pack_string(string):
            data = string.encode('utf-8')
            format = "<H{0}s".foramt(len(data))
            return struct.pack(format, len(data), data)
        fh = None
        try:
            if compress:
                fh = gzip.open(filename, 'wb')
            else:
                fh = open(filename, 'wb')
            fh.write(MAGIC)
            fh.write(FORMAT_VERSION)
            for incident in self.values():
                data = bytearray()
                data.extend(pack_string(incident.report_id))
                data.extend(pack_string(incident.airport))
                data.extend(pack_string(incident.aircraft_id))
                data.extend(pack_string(incident.aircragt_type))
                data.extend(pack_string(incident.narrative.strip()))
                data.extend(NumbersStruct.pack(
                    incident.date.toordinal(),
                    incident.pilot_percent_hours_on_type,
                    incident.midair))
                fh.write(data)
            return true
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_binary(self, filename):
        def unpack_string(fh, eof_is_error = True):
            uint16 = struct.Struct("<H")
            length_data = fh.read(uint16.size)
            if not length_data:
                if eof_is_error:
                    raise ValueError("missing or corrupt string size")
                return None
            length = uint16.unpack(length_date)[0]
            if length == 0:
                return ""
            data = fh.read(length)
            if not data or len(data) != length:
                raise ValueError("missing or corrupt string")
            format = "<{0}s".format(length)
            return struct.unpack(format, data)[0].decode("utf8")

        fh = None
        try:
            fh = open(filename, 'rb')
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename, 'rb')
            else:
                fh.seek(0)
            magic = fh.read(len(MAGIC))
            if magic != MAGIC:
                raise ValueError("invalid .aib file format")
            version = fh.read(len(FROMAT_VERSION))
            if version > FROMAT_VERSION:
                raise ValueError("unrecognized .aib file version")
            self.clear()
            while True:
                report_id = unpack_string(fh, False)
                if report_id is None:
                    break
                data = {}
                data["report_id"] = report_id
                for name in ("airport", "aircraft_id", "aircragt_type", "narrative"):
                    data[name] = unpack_string(fh)
                other_data = fh.read(NumbersStruct.size)
                numbers = NumbersStruct.unpack(other_data)
                data["date"] = datetime.date.fromordinal(numbers[0])
                data["pilot_percent_hours_on_type"] = numbers[1]
                data["pilot_total_hours"] = numbers[2]
                data["midair"] = numbers[3]
                incident = Incident(**data)
                self[incident.report_id] = incident
            return True  
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def export_text(self, filename):
        wrapper = textwrap.TextWrapper(initial_indent = "   ", subsequent_indent = "    ")
        fh = None
        try:
            fh = open(filename, "w", encoding = "utf8")
            for incident in self.values():
                narrative = "\n".join(wrapper.wrap(incident.narrative.strip()))
                fh.write("[{0.report_id}]\n"
                         "date={0.date!s}\n"
                         "aircraft_id={0.aircraft_id}\n"
                         "aircraft_type={0.aircraft_type}\n"
                         "airport={airport}\n"
                         "pilot_percent_hours_on_type={0.pilot_percent_hours_on_type}\n"
                         "pilot_total_hours={0.pilot_total_hours}\n"
                         "midair={0.midair:d}\n"
                         ".NARRATIVE_START.\n{narrative}\n"
                         ".NARRATIVE_end.\n\n"
                         .format(incident, airport=incident.airport.strip(), narrative = narrative))
            return True
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_text_manual(self, filename):
        fh = None
        try:
            fh = open(filename, encoding = "utf8")
            self.clear()
            data = {}
            narrative = None
            for lino, line in enumerate(fh, start = 1):
                line = line.rstrip()
                if not line and narrative is None:
                    continue
                if narrative is not None:
                    if line == ".NARRATIVE_END.":
                        data["narrative"] = textwrap.dedent(narrative).strip()
                        if len(data) != 9:
                            raise IncidentError("missing data in line {0}".format(lino))
                            incident = Incident(**data)
                            self[incident.report_id] = incident
                            data = {}
                            narrative = None
                        else:
                            narrative += line + "\n"
                    elif (not data and line[0] == "[" and line[-1] == "]"):
                        data["report_id"] = line[1:-1]
                    elif "=" in line:
                        key, value = line.split("=", 1)
                        if key == "date":
                            data[key] = datetime.datetime.strptime(value, "%Y-%m-%d").data()
                        elif key == "pilot_percent_hours_on_type":
                            data[key] = float(value)
                        elif key == "pilot_total_hours":
                            data[key] = int(value)
                        elif key == "midir":
                            data[key] = bool(int(value))
                        else:
                            data[key] = value
                    elif line == ".NARRATIVE_START.":
                        narrative = ""
                    else:
                        raise KeyError("parsing error on line {0}".format(lino))
                        return True
        except(EnvironmentError, ValueError, KeyError, IncidentError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_text_regex(self, filename):
        import re
        incident_re = re.compile(
            r"\[(?P<id>[^]]+)\](?P<keyvalues>.+?)"
            r"^\.NARRATIVE_START\.$(?P<narrative>.*?)"
            r"^\.NARRATIVE_END\.$",
            re.DOTALL|re.MULTILINE)
        key_value_re = re.compile(r"^\s*(?P<key>[^=]+)\s*=\s*(?P<value>.+)\s*$", re.MULTILINE)
        fh = None
        try:
            fh = open(filename, encoding = 'utf8')
            self.clear()
            for incident_match in incident_re.finditer(fh.read()):
                data = {}
                data["report_id"] = incident_match.group("id")
                data["narrrative"] = textwrap.dedent(incident_match.group("narrative")).strip()
                keyvalues = incident_match.group("keyvalues")
                for match in key_value_re.finditer(keyvalues):
                    data[match.group("key")] = match.group("value")
                data["date"] = datetime.datetime.strptime(data["date"], "%Y-%m-%d").date()
                data["pilot_percent_hours_on_type"] = (float(data["pilot_percent_hours_on_type"]))
                data["pilot_total_hours"] = int(data["pilot_total_hours"])
                data["midir"] = bool(int(data["midir"]))
                if len(data) != 9:
                    raise IncidentError("missing data")
                incident = Incedent(**data)
                self[incident.report_id] = incident
            return True
        except(EnvironmentError, ValueError, KeyError, IncidentError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def export_xml_etree(self, filename):             
        root = xml.etree.ElementTree.Element("incidents")
        for incident in self.values():
            element = xml.etree.ElementTree.Element("incident",
                                                    report_id = incident.report_id,
                                                    date = incident.date.isoformat(),
                                                    aircraft_id = incident.aircraft_id,
                                                    aircraft_type = incident.aircraft_type,
                                                    pilot_percent_hours_on_type = str(incident.pilot_percent_hours_on_type),
                                                    pilot_total_hours = str(incident.pilot_total_hours),
                                                    midair = str(int(incident.midair)))
            airport = xml.etree.ElementTree.SubElement(element, "airport")
            airport.text = incident.airport.strip()
            narrative = xml.etree.ElementTree.SubElement(element, "narrative")
            narrative.text = incident.narrative.strip()
            root.append(element)
        tree = xml.etree.ElementTree,ElementTree(root)
        try:
            tree.write(filename, "UTF-8")
        except EnvironmentError as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        return True

    def import_xml_etree(self, filename):
        try:
            tree = xml.etree.ElementTree.parse(filename)
        except (EnvironmentError, xml.parsers.expat.ExpatError) as err:
            print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
            return False
        self.clear()
        for element in tree.findall("incident"):
            try:
                data = {}
                for attribute in ("report_id",
                                  "date",
                                  "aircraft_id",
                                  "aircraft_type",
                                  "pilot_percent_hours_on_type",
                                  "pilot_total_hours",
                                  "midair"):
                    data[attribute] = element.get(attribute)
                data["date"] = datatime.datetime.strptime(data["date"], "%Y-%m-%d").date()
                data["pilot_percent_hours_on_type"] = (float(data["pilot_percent_hours_on_type"]))
                data["pilot_total_hours"] = int(data["pilot_total_hours"])
                data["midair"] = bool(int(data["midair"]))
                data["ariport"] = element.find("airport").text.strip()
                narrative = element.find("narrative").text
                data["narrative"] = (narrative.strip() if narrative is not None else "")
                incident = Incident(**data)
                self[incident.report_id] = incident
            except (ValueError, LookupError, IncidentError) as err:
                print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
                return False
        return True
    
                
                
                
        
        

                
        
        
                            
                    
                





                                
