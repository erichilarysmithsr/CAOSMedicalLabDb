/\* \* DB Script Tool \* MySQL - 2021-03-31 09:30:30 \* 2021-03-02
16:03:45 \* \* SQL COMMANDS FOR CAOS\_Medical\_Lab DATABASE \*/

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.CAOS \*/ SELECT *id, chemspider, volume, water,
urineph, animalmodels, chimpanzeeanimalmodels, batanimalmodels,
temperaturedegreescelsius, sodium, glucose, molecularweight FROM CAOS
WHERE *id=? ORDER BY \_id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.CAOS \*/ INSERT INTO
CAOS(\_id, chemspider, volume, water, urineph, animalmodels,
chimpanzeeanimalmodels, batanimalmodels, temperaturedegreescelsius,
sodium, glucose, molecularweight) VALUES(0, true, 0.0, 0.0, 0.0, 0, 0,
0, 0.0, 0.0, 0.0, 0.0);

/\* \* Update command - CAOS\_Medical\_Lab.CAOS \*/ UPDATE CAOS SET
chemspider=true, volume=0.0, water=0.0, urineph=0.0, animalmodels=0,
chimpanzeeanimalmodels=0, batanimalmodels=0,
temperaturedegreescelsius=0.0, sodium=0.0, glucose=0.0,
molecularweight=0.0 WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.CAOS \*/ DELETE FROM CAOS WHERE
\_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.IMHOTEP\_Bizarros \*/ SELECT *id, hospital, clinic,
patient, diagnosis, diabetes, prediabetes, acutenephritis,
type1diabetes, type2diabetes, hypertension, patientheight, patientweight
FROM IMHOTEP*Bizarros WHERE *id=? ORDER BY *id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.IMHOTEP\_Bizarros \*/ INSERT
INTO IMHOTEP\_Bizarros(\_id, hospital, clinic, patient, diagnosis,
diabetes, prediabetes, acutenephritis, type1diabetes, type2diabetes,
hypertension, patientheight, patientweight) VALUES(0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0.0, 0.0, 0.0);

/\* \* Update command - CAOS\_Medical\_Lab.IMHOTEP\_Bizarros \*/ UPDATE
IMHOTEP\_Bizarros SET hospital=0, clinic=0, patient=0, diagnosis=0,
diabetes=0, prediabetes=0, acutenephritis=0, type1diabetes=0,
type2diabetes=0, hypertension=0.0, patientheight=0.0, patientweight=0.0
WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.IMHOTEP\_Bizarros \*/ DELETE
FROM IMHOTEP\_Bizarros WHERE \_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.GENE\_CRISpy \*/ SELECT *id, gene, virus, cancer,
protein, humancellmodel, coronavirus, sarscov2, kidneystones, pneumonia,
humanenzymes, ghrelin, obestatin, breastcancergene, disease,
cardiovasculardisease, grampositivestain, gramnegativestain,
denaturation, dna, rna, lcarnitine, aminoacid,
kyotoencyclopediagenesgenomes FROM GENE*CRISpy WHERE *id=? ORDER BY *id
ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.GENE\_CRISpy \*/ INSERT INTO
GENE\_CRISpy(\_id, gene, virus, cancer, protein, humancellmodel,
coronavirus, sarscov2, kidneystones, pneumonia, humanenzymes, ghrelin,
obestatin, breastcancergene, disease, cardiovasculardisease,
grampositivestain, gramnegativestain, denaturation, dna, rna,
lcarnitine, aminoacid, kyotoencyclopediagenesgenomes) VALUES(0, 0.0, 0,
0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0.0, 0.0,
0.0, 0.0, 0.0, 0);

/\* \* Update command - CAOS\_Medical\_Lab.GENE\_CRISpy \*/ UPDATE
GENE\_CRISpy SET gene=0.0, virus=0, cancer=0, protein=0.0,
humancellmodel=0.0, coronavirus=0.0, sarscov2=0.0, kidneystones=0.0,
pneumonia=0, humanenzymes=0.0, ghrelin=0.0, obestatin=0.0,
breastcancergene=0.0, disease=0, cardiovasculardisease=0,
grampositivestain=0, gramnegativestain=0, denaturation=0.0, dna=0.0,
rna=0.0, lcarnitine=0.0, aminoacid=0.0, kyotoencyclopediagenesgenomes=0
WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.GENE\_CRISpy \*/ DELETE FROM
GENE\_CRISpy WHERE \_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.ED\_T\_DOIDE \*/ SELECT *id, nutritionix, mcdata,
kentuckyfriedchicken, dominospizza FROM ED*T\_DOIDE WHERE *id=? ORDER BY
*id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.ED\_T\_DOIDE \*/ INSERT INTO
ED\_T\_DOIDE(\_id, nutritionix, mcdata, kentuckyfriedchicken,
dominospizza) VALUES(NULL, 0.0, 0.0, 0.0, 0.0);

/\* \* Update command - CAOS\_Medical\_Lab.ED\_T\_DOIDE \*/ UPDATE
ED\_T\_DOIDE SET nutritionix=0.0, mcdata=0.0, kentuckyfriedchicken=0.0,
dominospizza=0.0 WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.ED\_T\_DOIDE \*/ DELETE FROM
ED\_T\_DOIDE WHERE \_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.Hysteria\_P\_TRANCE \*/ SELECT *id, fitbit, sleep,
weight, heartrate, dailyactivity, waterintake, tictok, unity3d,
cosinemudbox FROM Hysteria*P\_TRANCE WHERE *id=? ORDER BY *id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.Hysteria\_P\_TRANCE \*/
INSERT INTO Hysteria\_P\_TRANCE(\_id, fitbit, sleep, weight, heartrate,
dailyactivity, waterintake, tictok, unity3d, cosinemudbox) VALUES(NULL,
true, 0.0, 0.0, 0, 0.0, 0.0, 0, 0, 0);

/\* \* Update command - CAOS\_Medical\_Lab.Hysteria\_P\_TRANCE \*/
UPDATE Hysteria\_P\_TRANCE SET fitbit=true, sleep=0.0, weight=0.0,
heartrate=0, dailyactivity=0.0, waterintake=0.0, tictok=0, unity3d=0,
cosinemudbox=0 WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.Hysteria\_P\_TRANCE \*/ DELETE
FROM Hysteria\_P\_TRANCE WHERE \_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.Dexcom \*/ SELECT *id, devices, event, calibrations
FROM Dexcom WHERE *id=? ORDER BY \_id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.Dexcom \*/ INSERT INTO
Dexcom(\_id, devices, event, calibrations) VALUES(NULL, '2021-03-31
09:30:31', '?', 0.0);

/\* \* Update command - CAOS\_Medical\_Lab.Dexcom \*/ UPDATE Dexcom SET
devices='2021-03-31 09:30:31', event='?', calibrations=0.0 WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.Dexcom \*/ DELETE FROM Dexcom
WHERE \_id=?;

/\* ----------------------------------- \* Select command -
CAOS\_Medical\_Lab.Sifidious \*/ SELECT *id, picturehumanmodelsubjects,
pictureAnimalModels FROM Sifidious WHERE *id=? ORDER BY \_id ASC;

/\* \* Insert command - CAOS\_Medical\_Lab.Sifidious \*/ INSERT INTO
Sifidious(\_id, picturehumanmodelsubjects, pictureAnimalModels)
VALUES(NULL, true, true);

/\* \* Update command - CAOS\_Medical\_Lab.Sifidious \*/ UPDATE
Sifidious SET picturehumanmodelsubjects=true, pictureAnimalModels=true
WHERE \_id=?;

/* * Delete command - CAOS\_Medical\_Lab.Sifidious \*/ DELETE FROM
Sifidious WHERE \_id=?;
