#!/usr/bin/python

import logging
from BeautifulSoup import BeautifulSoup

logger = logging.getLogger('bacteria2go.gold')

def mineGold(shtml):
    '''Parse the wonderful Genomes Online Database'''
    d = {}

    b = BeautifulSoup(shtml)

    for t in b.findAll('table'):
        title = t.findAll('thead')[0].findAll('th')[0].text

        d[title] = {}

        try:
            for trow in t.findAll('tr')[1:]:
                column = trow.findAll('th')[1].text
                # Clean the &nbsp; mess
                column = column.replace('&nbsp;', '')

                value = trow.findAll('td')[0].text
                value = value.replace('&nbsp;', '')

                d[title][column] = value
        except:
            logger.debug('Could not parse this table line: %s'%trow)

    return d
