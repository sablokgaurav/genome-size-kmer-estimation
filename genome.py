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
