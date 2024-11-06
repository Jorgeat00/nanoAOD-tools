#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from .framework.postprocessor import PostProcessor

isData = 'data' in sys.argv[-1]

### INPUT FILE
#filepath = ['/afs/cern.ch/work/j/jrgonzal/public/pruebaNanoAOD/8EAB6B64-9210-E811-B19D-FA163E759AE3.root']
#filepath = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/2CE738F9-C212-E811-BD0E-EC0D9A8222CE.root']
#filepath = ['root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv4/b_bbar_4l_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/70000/F70304F1-D2DE-8F42-B08A-9DB82E9CA87E.root']#
#filepath = ['root://cms-xrd-global.cern.ch//store/data/Run2017B/DoubleMuon/NANOAOD/Nano14Dec2018-v1/280000/FB901F01-98AA-214F-A2C2-D67630861952.root']
#filepath = ['/nfs/fanae/user/juanr/nanoAOD/CMSSW_9_4_6/src/PhysicsTools/NanoAODTools/python/postprocessing/skimtree.root']
#filepath = ['/afs/cern.ch/work/j/jrgonzal/NanoAODtools/CMSSW_9_4_6/src/PhysicsTools/NanoAODTools/python/postprocessing/myNanoProdMc5TeV_singlemuon.root']
filepath = ['root://cms-xrd-global.cern.ch//store/user/jrgonzal/NANOAOD/HighEGJet/data5TeV_28ago2019_HighEGJet_Run2017G-17Nov2017-v2/190827_215958/0000/myNanoProdMc5TeV_NANO_10.root']

### OUTPUT
outdir = '.'

### SKIM 
cut = '(nElectron + nMuon) >= 2 && Jet_pt > 200' # nGenDressedLepton >= 2

### SLIM FILE
slimfile = "SlimFile.txt"
jecfile  = "Autumn18_V8_MC"

### MODULES
### Include modules to compute derivate quantities or calculate uncertainties
from .modules.jme.jetmetUncertainties import *
from .modules.common.puWeightProducer import *
from .modules.common.muonScaleResProducer import *
from .modules.skimNRecoLeps import *
from .modules.jme.jetRecalib import *
#from modules.addSUSYvar import *
#mod = [puAutoWeight(), skimRecoLeps(), addSUSYvarsMC()] # countHistogramsProducer(), jetmetUncertainties2017All()
mod = [skimRecoLeps(), jetRecalib('Spring18_ppRef5TeV_V2_DATA','Spring18_ppRef5TeV_V2_DATA')] # jetRecalib(jecfile), countHistogramsProducer(), jetmetUncertainties2017All()

p=PostProcessor(outdir,filepath,cut,slimfile,mod,provenance=True,outputbranchsel=slimfile)
p.run()
