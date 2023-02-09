from behave import *

@step('load modify pet json')
def step_impl(self):
    self.http_request_body = {
                              "id": self.variablesTemp['petID'],
                              "category": {
                                "id": 0,
                                "name": "string"
                              },
                              "name": "Golden",
                              "photoUrls": [
                                "string"
                              ],
                              "tags": [
                                {
                                  "id": 0,
                                  "name": "string"
                                }
                              ],
                              "status": "available"
                            }