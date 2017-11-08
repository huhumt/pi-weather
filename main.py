#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from auth_id import auth_method

def main():

    """
    this is the main entry of the project
    """

    yahoo_auth = auth_method("./config.json")
    yahoo_auth.auth_server()

if __name__ == "__main__":
    main()
