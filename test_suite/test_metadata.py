import json
import requests
import pytest

'''This module will be testing success and error queries associated with GET
metadata  by checksum ID API. All the functions with 'test_' as prefix will be
treated as test cases by pytest.
'''
###############################################################################
# Successful Conditions


def get_metadata(seq):
    response = {
        "metadata": {
            "md5": seq.md5,
            "trunc512": seq.sha512,
            "length": seq.size,
            "aliases": []
        }
    }
    return json.dumps(response, sort_keys=True)


def check_complete_metdata_response(response, seq, checksum):
    '''check_complete_metdata_response is a utility function used by
    test_complete_metadata function to remove duplication of code. It takes
    response se,q object and checksum ID used to query as input parameter and
    assert for reponse header, status code and content
    '''
    metadata = response.json()
    metadata['metadata']['aliases'] = []
    assert json.dumps(metadata, sort_keys=True) == get_metadata(seq)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/vnd.ga4gh.refget.v1.0.0+json'


def test_complete_metadata(server, data):
    '''test_complete_metadata tests all the possible scenarios of successfully
    retrieving metadatas. It uses server and data fixture values from
    conftest.py module.
    '''

    api = 'sequence/'
    accept_header = {
        'Accept': 'application/vnd.ga4gh.refget.v1.0.0+json'
    }
    for seq in data:
        # using md5 with Accept header
        response = requests.get(
            server + api + seq.md5 + '/metadata', headers=accept_header)
        check_complete_metdata_response(response, seq, seq.md5)

        # using md5 without Accept header
        response = requests.get(server + api + seq.md5 + '/metadata')
        check_complete_metdata_response(response, seq, seq.md5)


###############################################################################
# Error Conditions


@pytest.mark.parametrize("_input, _output", [
    (['some1111garbage1111ID', {}], 404),
    (['some1111garbage1111ID', {'Accept': 'application/vnd.ga4gh.refget.v1.0.0+json'}], 404),
    (['some1111garbage1111ID', {'Accept': 'application/embl'}], 404),
    (['6681ac2f62509cfc220d78751b8dc524', {'Accept': 'application/embl'}], 415)

])
def test_metadata_generic_errors(server, data, _input, _output):
    '''test_metadata_generic_errors tests generic error codes associated with
    unknown checksum ID, unsupported encoding request in Accept header or both
    'parametrize' is used to test all the possible cases without duplication
    '''

    api = 'sequence/'
    response = requests.get(
        server + api + _input[0] + '/metadata', headers=_input[1])
    assert response.status_code == _output
