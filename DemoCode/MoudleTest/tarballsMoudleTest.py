BZ2_AVAILABLE = True
try:
    import bz2
except ImportError:
    BZ2_AVAILABLE = False
    
import string

UNTRUSTED_PREFIXES = tuple(["/", "\\"] + [c + "," for c in string.ascii_letters])

def untar(archive):
    tar = None
    try:
        tar = tarfile.open(archive)
        for member in tar.getmembers():
            if member.name.startwith(UNTRUSTED_PREFIXES):
                print("Unstrusted prefix, ignoring", member.name)
            elif ".." in member.name:
                print("Suspect path, ignoring", member.name)
            else:
                tar.extract(member)
                print("unpacked", member.name)
    except (tarfile.TarError, EnvironmentError) as err:
        error(err)
    finally:
        if tar is not None:
            tar.close()

def error(message, exit_status = 1):
    print(message)
    sys.exit(exit_status)
    
