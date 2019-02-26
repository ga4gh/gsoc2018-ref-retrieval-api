There are three sequences used in the compliance documentation for sample queries and in the compliance test suite for API testing

 * NC_001422.1 Enterobacteria phage phiX174 sensu lato  
    [fasta sequnce](../compliance_suite/sequences/NC.faa)  
    Circular genome  
    Size : 5386  
    MD5 : 3332ed720ac7eaa9b3655c06f6b9e196  
    Tuncated SHA512 : 2085c82d80500a91dd0b8aa9237b0e43f1c07809bd6e6785  

 * I Saccharomyces_cerevisiae chromosome:R64-1-1:I:1:230218:1  
    [fasta sequence](../compliance_suite/sequences/I.faa)  
    Linear chromosome  
    Size : 230218  
    MD5 : 6681ac2f62509cfc220d78751b8dc524  
    Tuncated SHA512 : 959cb1883fc1ca9ae1394ceb475a356ead1ecceff5824ae7

 * VI Saccharomyces_cerevisiae chromosome:R64-1-1:VI:1:270161:1  
    [fasta sequence](../compliance_suite/sequences/VI.faa)  
    Linear chromosome  
    Size : 270161  
    MD5 : b7ebc601f9a7df2e1ec5863deeae88a3  
    Tuncated SHA512 : cfea89816a1a711055efbcdc32064df44feeb6b773990b07

Checksums will be used as identifiers in sequence retrieval and metadata retrieval APIs. There are currently two checksum algorithms in use:

 * MD5
 * Truncated SHA512

Implementation details of these algorithms are given in API specification doc [here](https://docs.google.com/document/d/1q2ZE9YewJTpaqQg82Nrz_jVy8KsDpKoG1T8RvCAAsbI/edit#heading=h.h66j2ox4ydtw).

**Server MUST implement MD5 while truncated SHA512 is optional**
