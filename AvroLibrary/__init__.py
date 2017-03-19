# -*- coding: utf-8 -*-
import avro.schema
import avro.io
import io
import avro.datafile
import avro.schema


class AvroLibrary(object):

    def parse_schema(self, schema_json):
        return avro.schema.parse(schema_json)

    def decode(self, encoded, writers_schema=None, readers_schema=None):
        bytes_reader = io.BytesIO(encoded)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(writers_schema=writers_schema, readers_schema=readers_schema)
        decoded = reader.read(decoder)
        return decoded

    def encode(self, item, writers_schema=None):
        writer = avro.io.DatumWriter(writers_schema=writers_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(item, encoder)
        encoded = bytes_writer.getvalue()
        return encoded
