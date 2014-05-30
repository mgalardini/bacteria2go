bacteria2go
===========

Quick and dirty script to download and analyse bacterial genomes from NCBI

Installation
------------

There's no need to install any of the scripts, but some of them rely on the presence of the bacteria2go package

Dependencies
------------

* NumPy
* BioPython
* orthoxml.py (https://github.com/jhcepas/phylogenetic-XML-python-parsers[available here])
* BeautifulSoup v4 (for ftp2Metadata)

* An internet connection (for some scripts accessing NCBI)
* A UNIX environment (for ftp2faa)

Scripts description
-------------------

* ftp2Genome: Stay up to date with the available genomic sequences of a species
    * Downloads gbk, faa and frn files from NCBI ftp
    * Uses the Entrez interface to download taxonomy data for each strain
    * Outputs summary and taxonomy data in JSON format
* ftp2Literature: fetches the pubmed entries associated with a certain bacterial species
* genome2Author: look for most recurring submitters in genbank files from NCBI
* ftp2Complete: Fetch the complete genomes from a NCBI ftp directory
* ftp2Metadata: Fetch metadata from NCBI BioProject and update JSON files
* ftp216s: Extract the 16s from NCBI FTP genbanks
* ftp2IGS: Extract the IGS spacer(s) from NCBI FTP genbanks
* ftp2faa: Convert faa files downloaded from NCBI FTP into a single faa file
* bioproject2Genbank: fetch Genbank files from BioProject IDs
    * Some bioproject IDs are not (yet) present in the NCBI FTP
* purgeFtp: Tell which genomes are abnormal, based on genome statistics and the absence of 16s/IGS data
* treeDist: Create a distance matrix from Newick trees
* omag2tsv: Convert OMA plain "OrthologousGroups" text files into a pangenome tsv file
* omah2tsv: Convert OMA orthoxml files into a pangenome tsv file
* getUniprot: get cross-references from Uniprot flat files
* getUnannotated: get OGs that lack Uniprot cross-reference IDs
* og2faa: pangenome to protein fasta files
* grepGO: parse Interproscan files and get GO terms
