import argparse

def arguments_user():
    parser = argparse.ArgumentParser(description='This tool go to help in to take IOCs of Cyber Threat Intelligence databases or others sources')

    parser.add_argument('--target', help='Target for passing through command line ex: http://teste.com')

    # Create a separate mutually exclusive group for --vt, --tm, and --li
    extraction_group = parser.add_mutually_exclusive_group(required=False)
    extraction_group.add_argument('--ip', action='store_true', help='Extraction of addresses IP')
    extraction_group.add_argument('--md5', action='store_true', help='Extraction hashes MD5')
    extraction_group.add_argument('--sha1', action='store_true', help='Extraction hashes SHA1')
    extraction_group.add_argument('--sha256', action='store_true', help='Extraction hashes SHA256')
    extraction_group.add_argument('--domain', action='store_true', help='Extraction domain')
    extraction_group.add_argument('--uri', action='store_true', help='Extraction URIs')


    # Add the predefined extraction methods as separate options
    parser.add_argument('--vt', action='store_true', help='For take IOCs of virus total')
    parser.add_argument('--tm', action='store_true', help='For take IOCs of ThreatMiner')
    parser.add_argument('--li', action='store_true', help='For take IOCs of labs inquest')

    return parser.parse_args()

if __name__ == "__main__":
    print('Error! this not main script, execute script KillerKyuubi.py')