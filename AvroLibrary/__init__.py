# -*- coding: utf-8 -*-
import avro.schema
import avro.io
import io
import avro.datafile
import avro.schema
from version import VERSION

__version__ = VERSION


class AvroLibrary(object):

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def parse_schema(self, schema_json):
        """Constructs and returns the Schema from the JSON text.
        - ``schema_json``: avro schema as json 
        """
        return avro.schema.parse(schema_json)

    def decode(self, encoded, writers_schema=None, readers_schema=None):
        """Reruns decoded data according to schema
        
        - ``encoded``: encoded data
        - ``writers_schema``: avro writers schema
        - ``readers_schema``: avro readers schema
        :return: 
        """
        bytes_reader = io.BytesIO(encoded)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(writers_schema=writers_schema, readers_schema=readers_schema)
        decoded = reader.read(decoder)
        return decoded

    def encode(self, item, writers_schema=None):
        """Returns encoded data
        
        - ``item``: item to be encoded according to schma 
        - ``writers_schema``: avro writers schema 
        """
        writer = avro.io.DatumWriter(writers_schema=writers_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(item, encoder)
        encoded = bytes_writer.getvalue()
        return encoded
