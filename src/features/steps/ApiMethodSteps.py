import os, time
import allure
import json
import requests
from allure_commons.types import AttachmentType
from behave import *
from dotenv import load_dotenv

dirlogs = "logs/"

global_Variable = {}


class ApiMethodSteps():

    @step('Wait "{seg}" seconds')
    def step_impl(self, seg):
        time.sleep(int(seg))

    @given('Set URL API: "{url}"')
    def setEnvironment(self, url):
        global_Variable['urlapi'] = url

    @given('Set Environment EndPoint: "{env}"')
    def setEnvironmentEndPoint(self, env):
        load_dotenv()
        global_Variable['urlapi'] = os.getenv(env)
        self.variablesTemp['id'] = ""
        global_Variable['params'] = ""

    @given('Set api endpoint as: "{api_endpoint}"')
    def endPointLogname(self, api_endpoint):
        global_Variable['Endpoint'] = api_endpoint

    @given('Set api endpoint params: "{endpoint_params}"')
    def endPointLogname(self, endpoint_params):
        global_Variable['params'] = endpoint_params

    @then('Response http code should be "{StatusCode}"')
    def assertStatusCode(self, StatusCode):

        time.sleep(2)
        if global_Variable['Status_Code'] == StatusCode:
            print('The code status is CORRECT: ' + global_Variable['Status_Code'])
        else:
            raise ValueError('The code status is INCORRECT: ' + global_Variable['Status_Code'])

    @then('Get Response Body, set Name: {logname}')
    def getLog(self, logname):
        global_Variable['Status_Code'] = str(self.response.status_code)
        response = json.loads(self.response.text)
        responsejson = json.dumps(response, indent=4)
        # if self.isRemote:
        #     allure.attach(responsejson, name='Response Body',
        #                   attachment_type=AttachmentType.JSON)
        # else:
        f = open(dirlogs + logname + " - Status Code " + global_Variable['Status_Code'] + ".json", "w+")
        f.write(responsejson)
        f.close()

    @given('Set HEADER key: "{key}" - value: "{header_value}"')
    def setHeaders(self, key, header_value):
        self.http_request_header[key] = header_value

    @step('Clear HEADER key: "{key}"')
    def clearHeaders(self, key):
        self.http_request_header.pop(key)

    @then('Get access Token')
    def getToken(self):
        global_Variable['ACToken'] = self.responseParse['data']['access_token']
        self.http_request_header['Authorization'] = "Bearer " + global_Variable['ACToken']

    @given('X-Token: "{token}"')
    def token(self, token):
        self.http_request_header['X-Token'] = token

    @given('load jsonpath: "{path}"')
    def getJsonPath(self, path):
        with open(path,encoding='utf-8') as file:
            self.http_request_body = json.load(file)

    @given('load json key: "{key}" - value: "{value}"')
    def setBody(self, key, value):
        self.http_request_body[key] = value


    # METHODS
    @when('Set Method "{method_api}"')
    def methods(self, method_api):
        self.methodApi = method_api
        if method_api == "POST":
            self.response = requests.post(global_Variable['urlapi'] + global_Variable['Endpoint'] + str(self.variablesTemp['id']) + global_Variable['params'],
                                          json=self.http_request_body, headers=self.http_request_header)
            if self.response.status_code != 204:
                self.responseParse = self.response.json()
            else:
                global_Variable['Status_Code'] = str(self.response.status_code)

        elif method_api == "GET":
            self.response = requests.get(url=global_Variable['urlapi'] + global_Variable['Endpoint'] + str(self.variablesTemp['id']) + global_Variable['params'],
                                         headers=self.http_request_header)
            self.responseParse = self.response.json()

        elif method_api == "PUT":
            self.response = requests.put(global_Variable['urlapi'] + global_Variable['Endpoint'],
                                          json=self.http_request_body, headers=self.http_request_header)
            self.responseParse = self.response.json()

        elif method_api == "DELETE":
            self.response = requests.delete(url=global_Variable['urlapi'] + global_Variable['Endpoint'] + str(self.variablesTemp['id']) + global_Variable['params'],
                                            headers=self.http_request_header)
            if self.response.status_code != 204:
                self.responseParse = self.response.json()
            else:
                global_Variable['Status_Code'] = str(self.response.status_code)


