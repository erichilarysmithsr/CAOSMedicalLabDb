#  
#  DB Script Tool
#  Python - 2021-05-03 17:11:25
#  
#  MODEL CLASSES FOR CAOS_Medical_Lab DATABASE
#



# CAOS.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.CAOS
# 2021-03-02 16:03:55
#
class CAOS(Object):

    #
    # Constructor
    #
    # Example: 
    # myCAOS = CAOS( val1, val2,.. )
    #
    def __init__(self, _id = None, chemspider = None, volume = None, water = None, urineph = None, animalmodels = None, chimpanzeeanimalmodels = None, batanimalmodels = None, temperaturedegreescelsius = None, sodium = None, glucose = None, molecularweight = None):
        self.___id = _id
        self.__chemspider = chemspider
        self.__volume = volume
        self.__water = water
        self.__urineph = urineph
        self.__animalmodels = animalmodels
        self.__chimpanzeeanimalmodels = chimpanzeeanimalmodels
        self.__batanimalmodels = batanimalmodels
        self.__temperaturedegreescelsius = temperaturedegreescelsius
        self.__sodium = sodium
        self.__glucose = glucose
        self.__molecularweight = molecularweight


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def chemspider(self):
        return self.__chemspider

    @chemspider.setter
    def chemspider(self, chemspider):
        self.__chemspider = chemspider

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, water):
        self.__water = water

    @property
    def urineph(self):
        return self.__urineph

    @urineph.setter
    def urineph(self, urineph):
        self.__urineph = urineph

    @property
    def animalmodels(self):
        return self.__animalmodels

    @animalmodels.setter
    def animalmodels(self, animalmodels):
        self.__animalmodels = animalmodels

    @property
    def chimpanzeeanimalmodels(self):
        return self.__chimpanzeeanimalmodels

    @chimpanzeeanimalmodels.setter
    def chimpanzeeanimalmodels(self, chimpanzeeanimalmodels):
        self.__chimpanzeeanimalmodels = chimpanzeeanimalmodels

    @property
    def batanimalmodels(self):
        return self.__batanimalmodels

    @batanimalmodels.setter
    def batanimalmodels(self, batanimalmodels):
        self.__batanimalmodels = batanimalmodels

    @property
    def temperaturedegreescelsius(self):
        return self.__temperaturedegreescelsius

    @temperaturedegreescelsius.setter
    def temperaturedegreescelsius(self, temperaturedegreescelsius):
        self.__temperaturedegreescelsius = temperaturedegreescelsius

    @property
    def sodium(self):
        return self.__sodium

    @sodium.setter
    def sodium(self, sodium):
        self.__sodium = sodium

    @property
    def glucose(self):
        return self.__glucose

    @glucose.setter
    def glucose(self, glucose):
        self.__glucose = glucose

    @property
    def molecularweight(self):
        return self.__molecularweight

    @molecularweight.setter
    def molecularweight(self, molecularweight):
        self.__molecularweight = molecularweight



    #
    # Methods
    #

    def __str__ (self):
        return ""



# IMHOTEP_Bizarros.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.IMHOTEP_Bizarros
# 2021-03-02 16:20:32
#
class IMHOTEP_Bizarros(Object):

    #
    # Constructor
    #
    # Example: 
    # myIMHOTEP_Bizarros = IMHOTEP_Bizarros( val1, val2,.. )
    #
    def __init__(self, _id = None, hospital = None, clinic = None, patient = None, diagnosis = None, diabetes = None, prediabetes = None, acutenephritis = None, type1diabetes = None, type2diabetes = None, hypertension = None, patientheight = None, patientweight = None):
        self.___id = _id
        self.__hospital = hospital
        self.__clinic = clinic
        self.__patient = patient
        self.__diagnosis = diagnosis
        self.__diabetes = diabetes
        self.__prediabetes = prediabetes
        self.__acutenephritis = acutenephritis
        self.__type1diabetes = type1diabetes
        self.__type2diabetes = type2diabetes
        self.__hypertension = hypertension
        self.__patientheight = patientheight
        self.__patientweight = patientweight


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def hospital(self):
        return self.__hospital

    @hospital.setter
    def hospital(self, hospital):
        self.__hospital = hospital

    @property
    def clinic(self):
        return self.__clinic

    @clinic.setter
    def clinic(self, clinic):
        self.__clinic = clinic

    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self, patient):
        self.__patient = patient

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis

    @property
    def diabetes(self):
        return self.__diabetes

    @diabetes.setter
    def diabetes(self, diabetes):
        self.__diabetes = diabetes

    @property
    def prediabetes(self):
        return self.__prediabetes

    @prediabetes.setter
    def prediabetes(self, prediabetes):
        self.__prediabetes = prediabetes

    @property
    def acutenephritis(self):
        return self.__acutenephritis

    @acutenephritis.setter
    def acutenephritis(self, acutenephritis):
        self.__acutenephritis = acutenephritis

    @property
    def type1diabetes(self):
        return self.__type1diabetes

    @type1diabetes.setter
    def type1diabetes(self, type1diabetes):
        self.__type1diabetes = type1diabetes

    @property
    def type2diabetes(self):
        return self.__type2diabetes

    @type2diabetes.setter
    def type2diabetes(self, type2diabetes):
        self.__type2diabetes = type2diabetes

    @property
    def hypertension(self):
        return self.__hypertension

    @hypertension.setter
    def hypertension(self, hypertension):
        self.__hypertension = hypertension

    @property
    def patientheight(self):
        return self.__patientheight

    @patientheight.setter
    def patientheight(self, patientheight):
        self.__patientheight = patientheight

    @property
    def patientweight(self):
        return self.__patientweight

    @patientweight.setter
    def patientweight(self, patientweight):
        self.__patientweight = patientweight



    #
    # Methods
    #

    def __str__ (self):
        return ""



# GENE_CRISpy.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.GENE_CRISpy
# 
#
class GENE_CRISpy(Object):

    #
    # Constructor
    #
    # Example: 
    # myGENE_CRISpy = GENE_CRISpy( val1, val2,.. )
    #
    def __init__(self, _id = None, gene = None, virus = None, cancer = None, protein = None, humancellmodel = None, coronavirus = None, sarscov2 = None, kidneystones = None, pneumonia = None, humanenzymes = None, ghrelin = None, obestatin = None, breastcancergene = None, disease = None, cardiovasculardisease = None, grampositivestain = None, gramnegativestain = None, denaturation = None, dna = None, rna = None, lcarnitine = None, aminoacid = None, kyotoencyclopediagenesgenomes = None):
        self.___id = _id
        self.__gene = gene
        self.__virus = virus
        self.__cancer = cancer
        self.__protein = protein
        self.__humancellmodel = humancellmodel
        self.__coronavirus = coronavirus
        self.__sarscov2 = sarscov2
        self.__kidneystones = kidneystones
        self.__pneumonia = pneumonia
        self.__humanenzymes = humanenzymes
        self.__ghrelin = ghrelin
        self.__obestatin = obestatin
        self.__breastcancergene = breastcancergene
        self.__disease = disease
        self.__cardiovasculardisease = cardiovasculardisease
        self.__grampositivestain = grampositivestain
        self.__gramnegativestain = gramnegativestain
        self.__denaturation = denaturation
        self.__dna = dna
        self.__rna = rna
        self.__lcarnitine = lcarnitine
        self.__aminoacid = aminoacid
        self.__kyotoencyclopediagenesgenomes = kyotoencyclopediagenesgenomes


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def gene(self):
        return self.__gene

    @gene.setter
    def gene(self, gene):
        self.__gene = gene

    @property
    def virus(self):
        return self.__virus

    @virus.setter
    def virus(self, virus):
        self.__virus = virus

    @property
    def cancer(self):
        return self.__cancer

    @cancer.setter
    def cancer(self, cancer):
        self.__cancer = cancer

    @property
    def protein(self):
        return self.__protein

    @protein.setter
    def protein(self, protein):
        self.__protein = protein

    @property
    def humancellmodel(self):
        return self.__humancellmodel

    @humancellmodel.setter
    def humancellmodel(self, humancellmodel):
        self.__humancellmodel = humancellmodel

    @property
    def coronavirus(self):
        return self.__coronavirus

    @coronavirus.setter
    def coronavirus(self, coronavirus):
        self.__coronavirus = coronavirus

    @property
    def sarscov2(self):
        return self.__sarscov2

    @sarscov2.setter
    def sarscov2(self, sarscov2):
        self.__sarscov2 = sarscov2

    @property
    def kidneystones(self):
        return self.__kidneystones

    @kidneystones.setter
    def kidneystones(self, kidneystones):
        self.__kidneystones = kidneystones

    @property
    def pneumonia(self):
        return self.__pneumonia

    @pneumonia.setter
    def pneumonia(self, pneumonia):
        self.__pneumonia = pneumonia

    @property
    def humanenzymes(self):
        return self.__humanenzymes

    @humanenzymes.setter
    def humanenzymes(self, humanenzymes):
        self.__humanenzymes = humanenzymes

    @property
    def ghrelin(self):
        return self.__ghrelin

    @ghrelin.setter
    def ghrelin(self, ghrelin):
        self.__ghrelin = ghrelin

    @property
    def obestatin(self):
        return self.__obestatin

    @obestatin.setter
    def obestatin(self, obestatin):
        self.__obestatin = obestatin

    @property
    def breastcancergene(self):
        return self.__breastcancergene

    @breastcancergene.setter
    def breastcancergene(self, breastcancergene):
        self.__breastcancergene = breastcancergene

    @property
    def disease(self):
        return self.__disease

    @disease.setter
    def disease(self, disease):
        self.__disease = disease

    @property
    def cardiovasculardisease(self):
        return self.__cardiovasculardisease

    @cardiovasculardisease.setter
    def cardiovasculardisease(self, cardiovasculardisease):
        self.__cardiovasculardisease = cardiovasculardisease

    @property
    def grampositivestain(self):
        return self.__grampositivestain

    @grampositivestain.setter
    def grampositivestain(self, grampositivestain):
        self.__grampositivestain = grampositivestain

    @property
    def gramnegativestain(self):
        return self.__gramnegativestain

    @gramnegativestain.setter
    def gramnegativestain(self, gramnegativestain):
        self.__gramnegativestain = gramnegativestain

    @property
    def denaturation(self):
        return self.__denaturation

    @denaturation.setter
    def denaturation(self, denaturation):
        self.__denaturation = denaturation

    @property
    def dna(self):
        return self.__dna

    @dna.setter
    def dna(self, dna):
        self.__dna = dna

    @property
    def rna(self):
        return self.__rna

    @rna.setter
    def rna(self, rna):
        self.__rna = rna

    @property
    def lcarnitine(self):
        return self.__lcarnitine

    @lcarnitine.setter
    def lcarnitine(self, lcarnitine):
        self.__lcarnitine = lcarnitine

    @property
    def aminoacid(self):
        return self.__aminoacid

    @aminoacid.setter
    def aminoacid(self, aminoacid):
        self.__aminoacid = aminoacid

    @property
    def kyotoencyclopediagenesgenomes(self):
        return self.__kyotoencyclopediagenesgenomes

    @kyotoencyclopediagenesgenomes.setter
    def kyotoencyclopediagenesgenomes(self, kyotoencyclopediagenesgenomes):
        self.__kyotoencyclopediagenesgenomes = kyotoencyclopediagenesgenomes



    #
    # Methods
    #

    def __str__ (self):
        return ""



# ED_T_DOIDE.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.ED_T_DOIDE
# 
#
class ED_T_DOIDE(Object):

    #
    # Constructor
    #
    # Example: 
    # myED_T_DOIDE = ED_T_DOIDE( val1, val2,.. )
    #
    def __init__(self, _id = None, nutritionix = None, mcdata = None, kentuckyfriedchicken = None, dominospizza = None, edamam = None, houndify = None):
        self.___id = _id
        self.__nutritionix = nutritionix
        self.__mcdata = mcdata
        self.__kentuckyfriedchicken = kentuckyfriedchicken
        self.__dominospizza = dominospizza
        self.__edamam = edamam
        self.__houndify = houndify


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def nutritionix(self):
        return self.__nutritionix

    @nutritionix.setter
    def nutritionix(self, nutritionix):
        self.__nutritionix = nutritionix

    @property
    def mcdata(self):
        return self.__mcdata

    @mcdata.setter
    def mcdata(self, mcdata):
        self.__mcdata = mcdata

    @property
    def kentuckyfriedchicken(self):
        return self.__kentuckyfriedchicken

    @kentuckyfriedchicken.setter
    def kentuckyfriedchicken(self, kentuckyfriedchicken):
        self.__kentuckyfriedchicken = kentuckyfriedchicken

    @property
    def dominospizza(self):
        return self.__dominospizza

    @dominospizza.setter
    def dominospizza(self, dominospizza):
        self.__dominospizza = dominospizza

    @property
    def edamam(self):
        return self.__edamam

    @edamam.setter
    def edamam(self, edamam):
        self.__edamam = edamam

    @property
    def houndify(self):
        return self.__houndify

    @houndify.setter
    def houndify(self, houndify):
        self.__houndify = houndify



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Hysteria_P_TRANCE.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.Hysteria_P_TRANCE
# 
#
class Hysteria_P_TRANCE(Object):

    #
    # Constructor
    #
    # Example: 
    # myHysteria_P_TRANCE = Hysteria_P_TRANCE( val1, val2,.. )
    #
    def __init__(self, _id = None, fitbit = None, sleep = None, weight = None, heartrate = None, dailyactivity = None, waterintake = None, tictok = None, unity3d = None, cosinemudbox = None):
        self.___id = _id
        self.__fitbit = fitbit
        self.__sleep = sleep
        self.__weight = weight
        self.__heartrate = heartrate
        self.__dailyactivity = dailyactivity
        self.__waterintake = waterintake
        self.__tictok = tictok
        self.__unity3d = unity3d
        self.__cosinemudbox = cosinemudbox


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def fitbit(self):
        return self.__fitbit

    @fitbit.setter
    def fitbit(self, fitbit):
        self.__fitbit = fitbit

    @property
    def sleep(self):
        return self.__sleep

    @sleep.setter
    def sleep(self, sleep):
        self.__sleep = sleep

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def heartrate(self):
        return self.__heartrate

    @heartrate.setter
    def heartrate(self, heartrate):
        self.__heartrate = heartrate

    @property
    def dailyactivity(self):
        return self.__dailyactivity

    @dailyactivity.setter
    def dailyactivity(self, dailyactivity):
        self.__dailyactivity = dailyactivity

    @property
    def waterintake(self):
        return self.__waterintake

    @waterintake.setter
    def waterintake(self, waterintake):
        self.__waterintake = waterintake

    @property
    def tictok(self):
        return self.__tictok

    @tictok.setter
    def tictok(self, tictok):
        self.__tictok = tictok

    @property
    def unity3d(self):
        return self.__unity3d

    @unity3d.setter
    def unity3d(self, unity3d):
        self.__unity3d = unity3d

    @property
    def cosinemudbox(self):
        return self.__cosinemudbox

    @cosinemudbox.setter
    def cosinemudbox(self, cosinemudbox):
        self.__cosinemudbox = cosinemudbox



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Dexcom.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.Dexcom
# 
#
class Dexcom(Object):

    #
    # Constructor
    #
    # Example: 
    # myDexcom = Dexcom( val1, val2,.. )
    #
    def __init__(self, _id = None, devices = None, event = None, calibrations = None):
        self.___id = _id
        self.__devices = devices
        self.__event = event
        self.__calibrations = calibrations


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def devices(self):
        return self.__devices

    @devices.setter
    def devices(self, devices):
        self.__devices = devices

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        self.__event = event

    @property
    def calibrations(self):
        return self.__calibrations

    @calibrations.setter
    def calibrations(self, calibrations):
        self.__calibrations = calibrations



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Sifidious.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - CAOS_Medical_Lab.Sifidious
# 
#
class Sifidious(Object):

    #
    # Constructor
    #
    # Example: 
    # mySifidious = Sifidious( val1, val2,.. )
    #
    def __init__(self, _id = None, picturehumanmodelsubjects = None, pictureAnimalModels = None, witai = None):
        self.___id = _id
        self.__picturehumanmodelsubjects = picturehumanmodelsubjects
        self.__pictureAnimalModels = pictureAnimalModels
        self.__witai = witai


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def picturehumanmodelsubjects(self):
        return self.__picturehumanmodelsubjects

    @picturehumanmodelsubjects.setter
    def picturehumanmodelsubjects(self, picturehumanmodelsubjects):
        self.__picturehumanmodelsubjects = picturehumanmodelsubjects

    @property
    def pictureAnimalModels(self):
        return self.__pictureAnimalModels

    @pictureAnimalModels.setter
    def pictureAnimalModels(self, pictureAnimalModels):
        self.__pictureAnimalModels = pictureAnimalModels

    @property
    def witai(self):
        return self.__witai

    @witai.setter
    def witai(self, witai):
        self.__witai = witai



    #
    # Methods
    #

    def __str__ (self):
        return ""