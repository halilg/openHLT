OpenHLT 

 The OpenHLT tool is used to determine the optimal parameters for the filters of the HLT paths (of the CMS experiment at the LHC/CERN). It provides direct access to the filter parameters which can be varied to check their effect on the paths output rate as well as the correlation between separate paths. 

 OpenHLT allows one to factor their HLT studies into production and filtering stages. In the production stage, raw data is taken as input and all the HLT objects are produced and made persistent. This time consuming step is typically run only once and no filtering is applied. The user can also customize the output of this step which reduces the file size allowing to run over large number of events for higher statistical accuracy. 

 In the filtering stage, the output of the production step is taken as input and all the filters are run on the already reconstructed objects. In this step, the user has direct access to the filter modules and can change the parameters to optimize the path of interest. Since the filter modules are not CPU intensive, this step can be repeated with ease until the optimal parameters are achieved. The output of this step is in the standard CMSSW format which allows the users to run their physics analysis directly on the output.

For additional information: https://twiki.cern.ch/twiki/bin/viewauth/CMS/NewOpenHLT
