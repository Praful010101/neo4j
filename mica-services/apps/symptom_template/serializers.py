from rest_framework import serializers 
import logging
from django.db import connection
from neo4j import GraphDatabase
 
logger = logging.getLogger(__name__)

NEO4J_URI = 'bolt://localhost:7687'
NEO4J_USER = "neo4juser"
NEO4J_PASS = "neo4jpass"

def query_neo4j(query):
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        with driver.session() as session:
            result = session.run(query)
            data = result.data()
            print('in')
        driver.close()
    except Exception as e:
        print('in this')
        logger.debug(f"Bad query or can't connect to \n "
                     f"NEO4J URI: {NEO4J_URI} \n "
                     f"PASS: {NEO4J_PASS} \n "
                     f"USER: {NEO4J_USER}"
                     f"CYPHER: {query}")
        data = {}
    return data


class TestNeo4jConnectionSerializer(serializers.Serializer):
    
    def parse_get_request(self, validated_data):

        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=('vaibhav', 'Windows@1234'))
            with driver.session() as session:
                result = session.run("Match () Return 1 Limit 1")
                data = f"Successfully connected to NEO4J URI: {NEO4J_URI}"
            driver.close()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}: can't connect to NEO4J database ! EXCEPTION: {e}")
            data = f"Can't connect to NEO4J URI: {NEO4J_URI} "

        return data

class SymptomTemplateSerializer(serializers.Serializer):
    
    def parse_get_request(self, validated_data):
        logger.info(f"hello") 
    
        data = query_neo4j(f'MATCH(smt:SymptomTemplate)'
                               f'return smt')                     
        logger.info(f"data: {data}")                 
        for st in data:
            logger.info(f"data_new: {st['smt']}")
        return data

       


