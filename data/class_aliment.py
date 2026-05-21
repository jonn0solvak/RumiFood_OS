from dataclasses import dataclass, fields

@dataclass
class aliment:
    type: str
    ms:float
    pdia:float
    pdi:float
    bpr:float
    cb:float
    ndf:float
    dndf:float
    adf:float
    ee:float
    pabs:float
    caabs:float
    em:float

@dataclass
class vache_viande(aliment):
    ufv:float
@dataclass
class vl(aliment):
    ufl:float

@dataclass
class fourrage_vl(vl):
    dcb:float
    dadf:float
@dataclass
class concentre_vl(vl): bvec:float
