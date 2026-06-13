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
class bv(aliment):
    ufv:float
@dataclass
class bl(aliment):
    ufl:float

@dataclass
class fourrage_bl(bl):
    dcb:float
    dadf:float
@dataclass
class concentre_bl(bl): bvec:float

@dataclass
class fourrage_bv(bv):
    dcb:float
    dadf:float
@dataclass
class concentre_bv(bv): bvec:float