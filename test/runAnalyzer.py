import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
options.parseArguments()

process = cms.Process("Validation")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles
                                                              # replace 'myfile.root' with the source file you want to use
                                                              #fileNames = cms.untracked.vstring(
                                                              #'file:/afs/cern.ch/work/l/lata/grid_pack/genproductions/bin/JHUGen/production_validation_HIG/susy_gridpack_validation/2016_LHEs/HIG-RunIISummer15wmLHEGS-01479.root'
                                                          )
                        )


ntuple_genHiggs = cms.PSet(
     NtupleName = cms.string('NtupleGenJet'),
     genParticles = cms.InputTag('genParticles'),
)
process.demo = cms.EDAnalyzer(
    "NtupleGenJet",
    Ntuples = cms.VPSet(
	ntuple_genHiggs,
    )
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( options.outputFile )
)
#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string("out_tree_susy_M200_2016.root"
#))
process.p = cms.Path(process.demo)
process.MessageLogger.cerr.FwkReport.reportEvery = 100


