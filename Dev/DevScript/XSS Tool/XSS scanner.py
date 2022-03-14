#''' XSS Scanner '''

#installin libraries
#pip3 install requests bs4
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import sys,re,random, requests, os
import tkinter as tk 
from tkinter import font  as tkfont  
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

def get_forms_on_page (url):
    #Enter the 'URL' of a webpage that returns the form from HTML content
    BeautifulSoup = bs(requests.get(url).content, "html.paser")
    return BeautifulSoup.find_all("form")

# This function extracts all details about an HTML 'form'
def get_form_dets (form):
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# submits a form and also scans for vulnerability
def submit_form(form_details, url, value):
    '''Params:
            form_details (list): a dictionary that contain form information
            url (str): the original URL that contain that form
            value (str): this will be replaced to all text and search inputs
    '''
    #construct the full URL 
    target_url = urljoin(url, form_details["action"])

    #get the inputs
    inputs = form_details["inputs"]
    data = {}

    #replace all text and search values with 'value'
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
        #if input name and value are not null, then add them to the data of form submission
        if input_name and input_value:
            data[input_name] = input_value
    # POST request
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    # GET request
    else:
        return requests.get(target_url, params=data)


# This function extracts all details about an HTML 'form'
def get_form_dets (form):
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# submits a form and also scans for vulnerability
def submit_form(form_details, url, value):
    '''Params:
            form_details (list): a dictionary that contain form information
            url (str): the original URL that contain that form
            value (str): this will be replaced to all text and search inputs
    <<<<<<< HEAD
        Returns the HTTP Response after form submission 
    =======

    >>>>>>> NancyWorkBranch
    '''
    #construct the full URL 
    attack_url = urljoin(url, form_details["action"])

    #get the inputs
    inputs = form_details["inputs"]
    data = {}

    #replace all text and search values with 'value'
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
                input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        #if input name and value are not null, then add them to the data of form submission
        if input_name and input_value:
            data[input_name] = input_value
    # POST request
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    # GET request
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
    # returning value
    is_vulnerable = False

    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
            # won't break because we want to print available vulnerable forms
    return is_vulnerable



#
#'''Reference
#
#
