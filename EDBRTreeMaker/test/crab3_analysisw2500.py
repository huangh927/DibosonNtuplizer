from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'WJets2500_weight25test-v'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Fall15_25nsV2_MC_L1FastJet_AK4PFchs.txt','Fall15_25nsV2_MC_L2Relative_AK4PFchs.txt','Fall15_25nsV2_MC_L3Absolute_AK4PFchs.txt','Fall15_25nsV2_MC_L1FastJet_AK8PFchs.txt','Fall15_25nsV2_MC_L2Relative_AK8PFchs.txt','Fall15_25nsV2_MC_L3Absolute_AK8PFchs.txt']
# Name of the CMSSW configuration file
#config.JobType.psetName    = 'bkg_ana.py'
config.JobType.psetName    = 'analysis.py'
#config.JobType.allowUndistributedCMSSW = True
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.inputDataset = '/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDataset = '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 15 
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 10000
config.Data.totalUnits = -1
config.Data.publication = False

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'WJets2500_weight25test'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
