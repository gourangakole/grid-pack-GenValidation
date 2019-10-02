import FWCore.ParameterSet.Config as cms

process = cms.Process("Validation")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(101) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0001/B2G-RunIIFall18GS-00005_3_1000.root' #good file
#'/store/mc/RunIIFall17MiniAODv2/TprimeTprime_M-700_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/50000/020878DA-708E-E811-AE7A-008CFAF74E6A.root' #to test miniAODD MG
#'file:/afs/cern.ch/user/g/gkole/public/B2G-RunIIFall17wmLHEGS-00150.root' # genarated MG GENSIM 

#'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0000/B2G-RunIIFall18GS-00005_3_999.root ',
#'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0000/B2G-RunIIFall18GS-00005_3_998.root',
#'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0000/B2G-RunIIFall18GS-00005_3_997.root', # had some problem 
#'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0000/B2G-RunIIFall18GS-00005_3_996.root',
#'/store/user/gkole/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190817_164543/0000/B2G-RunIIFall18GS-00005_3_995.root'
#'/store/user/spoddar/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190828_121700/0000/B2G-RunIIFall18GS-00005_3_175.root'
        #'file:/afs/cern.ch/work/l/lata/grid_pack/genproductions/bin/JHUGen/production_validation_HIG/susy_gridpack_validation/2016_LHEs/HIG-RunIISummer15wmLHEGS-01479.root'
#'/store/user/spoddar/TprimeTPrimeTotGammatGluon/TprimeTPrimeTotGammatGluon_cfg_GEN-SIM/190903_061149/0000/B2G-RunIIFall18GS-00005_3_8.root' # crashing
        
#'file:/afs/cern.ch/user/g/gkole/work/public/HIG-RunIISummer15wmLHEGS-01479.root' # for bbHToTauTau 
#'file:/eos/user/g/gkole/PostDoc/temp/B2G-RunIIFall18GS-00005_3_nEvents500.root' # for tprimeToTGamma

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
    fileName = cms.string("out_tree_TPrime_M500_2018.root"
))
process.p = cms.Path(process.demo)
process.MessageLogger.cerr.FwkReport.reportEvery = 100


