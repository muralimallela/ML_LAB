total_Records = 10
numGolfRecords = 4
unConditionalprobGolf = numGolfRecords / total_Records
print("Unconditional probability of golf:={}".format(unConditionalprobGolf))
# conditional probability of 'single' given 'medRisk'
numMedRiskSingle = 2
numMedRisk = 3
probMedRiskSingle = numMedRiskSingle/total_Records
probMedRisk = numMedRisk/total_Records
conditionalProb = (probMedRiskSingle/probMedRisk)
print("Conditional probability of single given medRisk: ={}".format(conditionalProb))
