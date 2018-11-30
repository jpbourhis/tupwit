# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from wit import Wit


print("Starting bot Function .... ")

#Token is OQX3PQEHBTPX53BIBCCUTWDOLTO5MGP2
"""
if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

"""

access_token='OQX3PQEHBTPX53BIBCCUTWDOLTO5MGP2'

def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def handle_message(response):

   # return  "current response {}" .format(response)

    {u'entities': {u'table': [{u'confidence': 1, u'type': u'value', u'value': u'products'}], u'verb': [{u'confidence': 0.97334078474831, u'type': u'value', u'value': u'Count'}, {u'confidence': 1, u'type': u'value', u'value': u'Count'}]}, u'msg_id': u'1hsH0GFH6FSB0j1Rk', u'_text': u'how many articles do I have ?'}

    entities = response['entities']



    print (len(entities))

    for entity in entities:
        print(entity)

    table= first_entity_value(entities,'table')

    print ("table name is:")
    print(table)

    return "Hello"

    #greetings = first_entity_value(entities, 'greetings')
    #celebrity = first_entity_value(entities, 'notable_person')




client = Wit(access_token=access_token)
client.interactive(handle_message=handle_message)






