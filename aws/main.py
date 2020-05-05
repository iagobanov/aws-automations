#!/usr/bin/env python

import sys 
import time

from tasks.discovery import get_ips
from tasks.route53_dump import get_records
from utils.regions import get_all_regions

def main():
    regions = get_all_regions ()
    get_ips (regions)
    get_records ()

if __name__ == "__main__":
    main ()