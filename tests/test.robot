*** Settings ***
Library           AvroLibrary
Library           OperatingSystem

*** Variables ***
&{ITEM}       name=Matti    favorite_color=red         favorite_number=${123}

*** Test Cases ***
Encode Test
    ${schema_json}=  Get File  ${CURDIR}${/}resources${/}example_avro.json
    ${schema}=  Parse Schema  ${schema_json}
    ${encoded_item}=  Get Binary File	${CURDIR}${/}resources${/}msg.bin

    ${encoded}=  Encode  ${ITEM}  ${schema}
    Should Be Equal  ${encoded}  ${encoded_item}

Decode Test
    ${schema_json}=  Get File  ${CURDIR}${/}resources${/}example_avro.json
    ${schema}=  Parse Schema  ${schema_json}
    ${encoded_item}=  Get Binary File	${CURDIR}${/}resources${/}msg.bin

    ${decoded}=  Decode  ${encoded_item}  ${schema}
    Should Be Equal  ${decoded}  ${ITEM}