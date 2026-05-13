#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Program Name : ardoq_sync.py
Description  : Synchronisation des données entre Ardoq et un
               système tiers (ex: LISA / NOVA).
Author       : Nicolas Correia
Email        : nicolas.correia@company.com
Organization : CMA CGM
Created      : 2026-04-27
Last Update  : 2026-04-27
Version      : 1.0.0
Status       : Development | Production | Deprecated
License      : MIT
Python       : >= 3.10
============================================================

Requirements :
--------------
- Python >= 3.10
- ardoqpy
- requests
- colorama
- logging

Environment Variables :
-----------------------
- ARDOQ_HOST       : https://app.ardoq.com or custom domain
- ARDOQ_API_TOKEN  : Ardoq API token
- ARDOQ_ORG_LABEL  : Organisation label (si pas de custom domain)

Usage :
-------
$ python3 ardoq.py

Notes :
-------
- Les secrets ne doivent jamais être hardcodés.
- Les logs sont affichés en console.
- Les erreurs critiques sont affichées en rouge (ANSI).

============================================================
"""
# =====================================================================
# Imports
# =====================================================================

from ardoqpy import ArdoqClient
from ardoqpy import ArdoqSyncClient
import os
import sys
import certifi
import requests
import json
import urllib.request
import urllib.parse
import example_ardoq_client
import argparse
import logging
from colorama import Fore, Style, init
from pprint import pprint

# -----------------------------
# Configuration
# -----------------------------
# You can set these as environment variables for security
API_TOKEN = os.getenv("ARDOQ_API_TOKEN")
ORG_NAME = os.getenv("ARDOQ_ORG_NAME")
BASE_URL = f"https://{ORG_NAME}.ardoq.com"

# Evite erreur de couleur
init(autoreset=True)

# =====================================================================
# Logging
# =====================================================================
class ColorFormatter(logging.Formatter):

    COLORS = {
        logging.INFO: Fore.GREEN,
        logging.ERROR: Fore.YELLOW,      # Orange (le plus proche en ANSI)
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        message = super().format(record)
        return f"{color}{message}{Style.RESET_ALL}"

def setup_logger(name: str = "app") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = ColorFormatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False

    return logger


logger = setup_logger()

logger.info("Synchronisation démarrée")
logger.error("Erreur de validation des données")
logger.critical("FATAL: Impossible de contacter l’API Ardoq")


# -----------------------------
# Input validation
# -----------------------------
if not API_TOKEN or API_TOKEN == "YOUR_API_TOKEN_HERE":
    logger.critical("Error: Please set your Ardoq API token in ARDOQ_API_TOKEN env variable.")
    sys.exit(1)

# -----------------------------
# Initialize client
# -----------------------------
try:
    logger.info("client V1")
    client = ArdoqClient(hosturl=BASE_URL, token=API_TOKEN)
except Exception as e:
    logger.critical("Failed to initialize Ardoq client: {e}")
    sys.exit(1)

# -----------------------------
# Initialize client V2
# -----------------------------
try:
    logger.info("client V2")
    clientV2 = ArdoqClient(hosturl=BASE_URL, token=API_TOKEN, version='v2')
except Exception as e:
    logger.critical("Failed to initialize Ardoq client: {e}")
    sys.exit(1)

# -----------------------------
# Initialize client Sync
# -----------------------------
try:
    logger.info("client Sync")
    clientSync = ArdoqSyncClient(hosturl=BASE_URL, token=API_TOKEN)
except Exception as e:
    logger.critical("Failed to initialize Ardoq Sync client: {e}")
    sys.exit(1)

# -----------------------------
# Initialize client Sync Simulate
# -----------------------------
try:
    logger.info("client Sync en Simulation")
    clientSync = ArdoqSyncClient(hosturl=BASE_URL, token=API_TOKEN, simulate=True)
except Exception as e:
    logger.critical("Failed to initialize Ardoq Sync client Simulate: {e}")
    sys.exit(1)

# -----------------------------
# List workspaces
# -----------------------------
try:
    logger.info("client get_workspaces()")
    workspaces = client.get_workspaces()
    for ws in workspaces:
        logger.info(f"- {ws['name']} (ID: {ws['_id']})")
except Exception as e:
    logger.info(f"Error fetching workspaces: {e}")
    sys.exit(1)

# -----------------------------
# Me
# -----------------------------
try:
    logger.info("client V2  get_workspaces()")
    workspaces = clientV2.get_workspaces()
    for ws in workspaces:
        logger.info(f"- {pprint(ws)} ")
except Exception as e:
    logger.critical(f"Error fetching workspaces: {e} ")
    sys.exit(1)

# -----------------------------
# Me
# -----------------------------
def ardoq_request(resource, method="GET", query_params=None, data=None):
    api_token = os.getenv("ARDOQ_API_TOKEN")
    org_label = os.getenv("ARDOQ_ORG_LABEL")
    host = f"https://{ORG_NAME}.ardoq.com"
    url = host + resource
    logger.info(f"{query_params}")
    # support optional query parameters {"foo":"bar","baz":2}
    if query_params:
       url = url + "?" + urllib.parse.urlencode(query_params)
       # url = url + "?" + query_params
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", "Bearer " + str(api_token))
    if org_label is not None:
        req.add_header("X-org", org_label)
    if data is not None:
        req.add_header("Content-Type", "application/json; charset=utf-8")
        data = json.dumps(data).encode("utf-8")
    with urllib.request.urlopen(req, data=data) as resp:
        return json.loads(resp.read().decode("utf-8"))

resp = ardoq_request("/api/v2/me")
logger.info(f"{resp}")

resp = ardoq_request("/api/v2/workspaces/bc1e510b4f37806a20208b5d")
logger.info(f"{resp}")


resp = ardoq_request("/api/v2/references/",query_params={"rootWorkspace" : "bc1e510b4f37806a20208b5d"})
logger.info(f"{resp}")


# -----------------------------
# Me V2
# -----------------------------
api = example_ardoq_client.API(
        ardoq_api_host=BASE_URL, ardoq_org_label=ORG_NAME, ardoq_api_token=API_TOKEN
    )
logger.info(f"{api.me()}")


# -----------------------------
# Report
# -----------------------------

def report_fn(report_id, view="objects"):
    """
    Generator function that yields items from a report.
    use the `view` parameter to specify which view to use.
    Valid values are `objects` and `tabular`.
    """
    try:
        url = "{}/api/v2/reports/{}/run/{}".format(BASE_URL, report_id, view)
        logger.info(url)
        while url:
            req = urllib.request.Request(url)
            req.add_header("X-org", ORG_NAME)
            req.add_header("Authorization", "Bearer " + str(API_TOKEN))
            with urllib.request.urlopen(req) as resp:
                report_data = json.loads(resp.read().decode("utf-8"))
                for row_data in report_data['values']:
                    yield row_data
            url = report_data.get("_links", {}).get("next", {}).get("href")
    except Exception as e:
        logger.critical(f"Error fetching url: {e} ")
        sys.exit(1)

def objects_report(report_id):
    return report_fn(report_id, view="objects")

def tabular_report(report_id):
    return report_fn(report_id, view="tabular")

report_id = "FIX_ME"

#for d in objects_report(report_id):
#    logger.info(d) 