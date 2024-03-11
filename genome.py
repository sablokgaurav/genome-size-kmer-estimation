def genomesize(sampleG1peaks, 
                  standardG1peaks, 
                           genomeStandard):
    # Universitat Potsdam
    # Author Gaurav Sablok
    # date: 2024-3-11
    """"
    estimating the genome size post calibration from the 
    genome size estimations.You can give all the peaks of
    the unknown samples and the peaks of the known and the 
    size estimate of the standard.  
    """
    import pandas as pd
    if sampleG1peaks and standardG1peaks and genomesize is not None:
        unknownpeaks = pd.read_csv(sampleG1peaks, sep = "\t")
        knownpeaks = pd.read_csv(standardG1peaks, sep = "\t")
        estimatingmean = unknownpeaks//knownpeaks
    return estimatingmean*genomeStandard


def C1estimates(samplecount):
  """
  a 1C function estimates which will take into account the 
  1C estimates for the modelling of the values and the sequence encoding.
  """
        estimates = {}
        while len(estimates.keys()) <= int(samplecount):
              takeestimates = input("please provide the 1cestimates:")
              takesamples = input("please provide the samples:")
              estimates[takeestimates] = takesamples
              if len(list(estimates.keys())) == int(samplecount):
                    break
        return [(int(i)*978000000)/2 for i in list(estimates.keys())]
