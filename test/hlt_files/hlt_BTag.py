# /cdaq/physics/Run2012/8e33/v2.1/HLT/V7 (CMSSW_5_2_7_HLT3)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/cdaq/physics/Run2012/8e33/v2.1/HLT/V7')
)

process.streams = cms.PSet( 
  A = cms.vstring( 'BJetPlusX',
    'BTag',
    'Commissioning',
    'Cosmics',
    'DoubleElectron',
    'DoubleMu',
    'DoubleMuParked',
    'DoublePhoton',
    'DoublePhotonHighPt',
    'ElectronHad',
    'FEDMonitor',
    'HLTPhysicsParked',
    'HTMHT',
    'HTMHTParked',
    'HcalHPDNoise',
    'HcalNZS',
    'JetHT',
    'JetMon',
    'LogMonitor',
    'MET',
    'METParked',
    'MinimumBias',
    'MuEG',
    'MuHad',
    'MuOnia',
    'MuOniaParked',
    'MultiJet',
    'MultiJet1Parked',
    'NoBPTX',
    'PhotonHad',
    'SingleElectron',
    'SingleMu',
    'SinglePhoton',
    'SinglePhotonParked',
    'Tau',
    'TauParked',
    'TauPlusX',
    'VBF1Parked',
    'ZeroBiasParked' ),
  ALCALUMIPIXELS = cms.vstring( 'AlCaLumiPixels' ),
  ALCAP0 = cms.vstring( 'AlCaP0' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  B = cms.vstring( 'ParkingMonitor' ),
  Calibration = cms.vstring( 'TestEnablesEcalHcalDT' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  Express = cms.vstring( 'ExpressPhysics' ),
  HLTDQM = cms.vstring( 'OnlineHltMonitor' ),
  HLTMON = cms.vstring( 'OfflineMonitor' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  PhysicsDST = cms.vstring( 'DataScouting' ),
  RPCMON = cms.vstring( 'RPCMonitor' ),
  TrackerCalibration = cms.vstring( 'TestEnablesTracker' )
)
process.datasets = cms.PSet( 
  AlCaLumiPixels = cms.vstring( 'AlCa_LumiPixels_Random_v1',
    'AlCa_LumiPixels_ZeroBias_v4',
    'AlCa_LumiPixels_v8' ),
  AlCaP0 = cms.vstring( 'AlCa_EcalEtaEBonly_v6',
    'AlCa_EcalEtaEEonly_v6',
    'AlCa_EcalPi0EBonly_v6',
    'AlCa_EcalPi0EEonly_v6' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v13' ),
  BJetPlusX = cms.vstring( 'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7',
    'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_L1DoubleJet36Central_v7',
    'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7',
    'HLT_QuadJet75_55_35_20_VBF_v1',
    'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7',
    'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6',
    'HLT_QuadPFJet78_61_44_31_VBF_v1',
    'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6' ),
  BTag = cms.vstring( 'HLT_BTagMu_DiJet110_Mu5_v6',
    'HLT_BTagMu_DiJet20_Mu5_v6',
    'HLT_BTagMu_DiJet40_Mu5_v6',
    'HLT_BTagMu_DiJet70_Mu5_v6',
    'HLT_BTagMu_Jet300_Mu5_v6' ),
  Commissioning = cms.vstring( 'HLT_Activity_Ecal_SC7_v13',
    'HLT_BeamGas_HF_Beam1_v5',
    'HLT_BeamGas_HF_Beam2_v5',
    'HLT_IsoTrackHB_v14',
    'HLT_IsoTrackHE_v15',
    'HLT_L1SingleEG12_v6',
    'HLT_L1SingleEG5_v6',
    'HLT_L1SingleJet16_v7',
    'HLT_L1SingleJet36_v7',
    'HLT_L1SingleMu12_v2',
    'HLT_L1SingleMuOpen_v7' ),
  Cosmics = cms.vstring( 'HLT_BeamHalo_v13',
    'HLT_L1SingleMuOpen_AntiBPTX_v7',
    'HLT_L1TrackerCosmics_v7' ),
  DataScouting = cms.vstring( 'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4',
    'DST_HT250_v4',
    'DST_L1HTT_Or_L1MultiJet_v4',
    'DST_Mu5_HT250_v4' ),
  DoubleElectron = cms.vstring( 'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12',
    'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6',
    'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8',
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6',
    'HLT_Ele5_SC5_Jpsi_Mass2to15_v4',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15',
    'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2',
    'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v18' ),
  DoubleMu = cms.vstring( 'HLT_DoubleMu11_Acoplanarity03_v5',
    'HLT_DoubleMu4_Acoplanarity03_v5',
    'HLT_DoubleMu5_IsoMu5_v20',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2DoubleMu23_NoVertex_v11',
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3',
    'HLT_Mu13_Mu8_NoDZ_v1',
    'HLT_Mu17_Mu8_v22',
    'HLT_Mu17_TkMu8_NoDZ_v1',
    'HLT_Mu17_TkMu8_v14',
    'HLT_Mu17_v5',
    'HLT_Mu22_TkMu22_v9',
    'HLT_Mu22_TkMu8_v9',
    'HLT_Mu8_v18',
    'HLT_TripleMu5_v19' ),
  DoubleMuParked = cms.vstring( 'HLT_DoubleMu11_Acoplanarity03_v5',
    'HLT_DoubleMu4_Acoplanarity03_v5',
    'HLT_DoubleMu5_IsoMu5_v20',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2DoubleMu23_NoVertex_v11',
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3',
    'HLT_Mu13_Mu8_NoDZ_v1',
    'HLT_Mu13_Mu8_v22',
    'HLT_Mu17_Mu8_v22',
    'HLT_Mu17_TkMu8_NoDZ_v1',
    'HLT_Mu17_TkMu8_v14',
    'HLT_Mu17_v5',
    'HLT_Mu22_TkMu22_v9',
    'HLT_Mu22_TkMu8_v9',
    'HLT_Mu8_v18',
    'HLT_TripleMu5_v19' ),
  DoublePhoton = cms.vstring( 'HLT_Photon26_Photon18_v12',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6',
    'HLT_Photon36_Photon22_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v4' ),
  DoublePhotonHighPt = cms.vstring( 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7',
    'HLT_DoubleEle33_CaloIdL_v14',
    'HLT_DoubleEle33_CaloIdT_v10',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6',
    'HLT_DoublePhoton48_HEVT_v8',
    'HLT_DoublePhoton53_HEVT_v2',
    'HLT_DoublePhoton70_v6',
    'HLT_DoublePhoton80_v7' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v3' ),
  ElectronHad = cms.vstring( 'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18' ),
  ExpressPhysics = cms.vstring( 'HLT_DoublePhoton80_v7',
    'HLT_EightJet30_eta3p0_v5',
    'HLT_EightJet35_eta3p0_v5',
    'HLT_MET400_v7',
    'HLT_Mu17_Mu8_v22',
    'HLT_Photon300_NoHE_v5',
    'HLT_ZeroBias_v7' ),
  FEDMonitor = cms.vstring( 'HLT_DTErrors_v3' ),
  HLTPhysicsParked = cms.vstring( 'HLT_Physics_Parked_v1' ),
  HTMHT = cms.vstring( 'HLT_HT250_AlphaT0p55_v8',
    'HLT_HT250_AlphaT0p57_v8',
    'HLT_HT300_AlphaT0p53_v8',
    'HLT_HT300_AlphaT0p54_v14',
    'HLT_HT350_AlphaT0p52_v8',
    'HLT_HT350_AlphaT0p53_v19',
    'HLT_HT400_AlphaT0p51_v19',
    'HLT_HT400_AlphaT0p52_v14',
    'HLT_HT450_AlphaT0p51_v14',
    'HLT_PFNoPUHT350_PFMET100_v4',
    'HLT_PFNoPUHT400_PFMET100_v4',
    'HLT_RsqMR40_Rsq0p04_v6',
    'HLT_RsqMR55_Rsq0p09_MR150_v6',
    'HLT_RsqMR60_Rsq0p09_MR150_v6',
    'HLT_RsqMR65_Rsq0p09_MR150_v5' ),
  HTMHTParked = cms.vstring( 'HLT_HT200_AlphaT0p57_v8',
    'HLT_HT250_AlphaT0p55_v8',
    'HLT_HT250_AlphaT0p57_v8',
    'HLT_HT300_AlphaT0p53_v8',
    'HLT_HT300_AlphaT0p54_v14',
    'HLT_HT350_AlphaT0p52_v8',
    'HLT_HT350_AlphaT0p53_v19',
    'HLT_HT400_AlphaT0p51_v19',
    'HLT_HT400_AlphaT0p52_v14',
    'HLT_HT450_AlphaT0p51_v14',
    'HLT_PFNoPUHT350_PFMET100_v4',
    'HLT_PFNoPUHT400_PFMET100_v4',
    'HLT_RsqMR40_Rsq0p04_v6',
    'HLT_RsqMR45_Rsq0p09_v5',
    'HLT_RsqMR55_Rsq0p09_MR150_v6',
    'HLT_RsqMR60_Rsq0p09_MR150_v6',
    'HLT_RsqMR65_Rsq0p09_MR150_v5' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise_v8',
    'HLT_L1Tech_HBHEHO_totalOR_v6',
    'HLT_L1Tech_HCAL_HF_single_channel_v4' ),
  HcalNZS = cms.vstring( 'HLT_HcalNZS_v10',
    'HLT_HcalPhiSym_v11',
    'HLT_HcalUTCA_v1' ),
  JetHT = cms.vstring( 'HLT_DiPFJetAve320_v10',
    'HLT_DiPFJetAve400_v10',
    'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10',
    'HLT_HT200_v6',
    'HLT_HT250_v7',
    'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_DoubleDisplacedPFJet60_v10',
    'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_SingleDisplacedPFJet60_v10',
    'HLT_HT300_v7',
    'HLT_HT350_v7',
    'HLT_HT400_v7',
    'HLT_HT450_v7',
    'HLT_HT500_v7',
    'HLT_HT550_v7',
    'HLT_HT650_Track50_dEdx3p6_v10',
    'HLT_HT650_Track60_dEdx3p7_v10',
    'HLT_HT650_v7',
    'HLT_HT750_v7',
    'HLT_Jet370_NoJetID_v15',
    'HLT_MET80_Track50_dEdx3p6_v6',
    'HLT_MET80_Track60_dEdx3p7_v6',
    'HLT_MET80_v5',
    'HLT_PFJet320_v9',
    'HLT_PFJet400_v9',
    'HLT_PFNoPUHT350_v4',
    'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4',
    'HLT_PFNoPUHT650_v4',
    'HLT_PFNoPUHT700_v4',
    'HLT_PFNoPUHT750_v4' ),
  JetMon = cms.vstring( 'HLT_DiPFJetAve140_v10',
    'HLT_DiPFJetAve200_v10',
    'HLT_DiPFJetAve260_v10',
    'HLT_DiPFJetAve40_v9',
    'HLT_DiPFJetAve80_v10',
    'HLT_PFJet140_v9',
    'HLT_PFJet200_v9',
    'HLT_PFJet260_v9',
    'HLT_PFJet40_v8',
    'HLT_PFJet80_v9',
    'HLT_SingleForJet15_v4',
    'HLT_SingleForJet25_v4' ),
  L1Accept = cms.vstring( 'DST_Physics_v5' ),
  LogMonitor = cms.vstring( 'HLT_LogMonitor_v4' ),
  MET = cms.vstring( 'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5',
    'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5',
    'HLT_DiCentralPFJet30_PFMET80_v6',
    'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9',
    'HLT_L1ETM100_v2',
    'HLT_L1ETM30_v2',
    'HLT_L1ETM40_v2',
    'HLT_L1ETM70_v2',
    'HLT_MET120_HBHENoiseCleaned_v6',
    'HLT_MET120_v13',
    'HLT_MET200_HBHENoiseCleaned_v5',
    'HLT_MET200_v12',
    'HLT_MET300_HBHENoiseCleaned_v5',
    'HLT_MET300_v4',
    'HLT_MET400_HBHENoiseCleaned_v5',
    'HLT_MET400_v7',
    'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4',
    'HLT_PFMET150_v7',
    'HLT_PFMET180_v7' ),
  METParked = cms.vstring( 'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5',
    'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5',
    'HLT_DiCentralPFJet30_PFMET80_v6',
    'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9',
    'HLT_L1ETM100_v2',
    'HLT_L1ETM30_v2',
    'HLT_L1ETM40_v2',
    'HLT_L1ETM70_v2',
    'HLT_MET100_HBHENoiseCleaned_v1',
    'HLT_MET120_HBHENoiseCleaned_v6',
    'HLT_MET120_v13',
    'HLT_MET200_HBHENoiseCleaned_v5',
    'HLT_MET200_v12',
    'HLT_MET300_HBHENoiseCleaned_v5',
    'HLT_MET300_v4',
    'HLT_MET400_HBHENoiseCleaned_v5',
    'HLT_MET400_v7',
    'HLT_MET80_Parked_v5',
    'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4',
    'HLT_PFMET150_v7',
    'HLT_PFMET180_v7' ),
  MinimumBias = cms.vstring( 'HLT_Physics_v5',
    'HLT_PixelTracks_Multiplicity70_v3',
    'HLT_PixelTracks_Multiplicity80_v12',
    'HLT_PixelTracks_Multiplicity90_v3',
    'HLT_Random_v2',
    'HLT_ZeroBiasPixel_DoubleTrack_v2',
    'HLT_ZeroBias_v7' ),
  MuEG = cms.vstring( 'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16',
    'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu22_Photon22_CaloIdL_v7',
    'HLT_Mu30_Ele30_CaloIdL_v8',
    'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7',
    'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7' ),
  MuHad = cms.vstring( 'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8',
    'HLT_DoubleMu14_Mass8_PFMET40_v8',
    'HLT_DoubleMu14_Mass8_PFMET50_v8',
    'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4',
    'HLT_IsoMu12_DoubleCentralJet65_v4',
    'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_Mu40_PFNoPUHT350_v4',
    'HLT_Mu60_PFNoPUHT350_v4',
    'HLT_Mu8_DiJet30_v7',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_Mu8_QuadJet30_v7',
    'HLT_Mu8_TriJet30_v7',
    'HLT_PFNoPUHT350_Mu15_PFMET45_v4',
    'HLT_PFNoPUHT350_Mu15_PFMET50_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET45_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET50_v4',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4' ),
  MuOnia = cms.vstring( 'HLT_Dimuon0_Jpsi_Muon_v18',
    'HLT_Dimuon0_Jpsi_NoVertexing_v14',
    'HLT_Dimuon0_Jpsi_v17',
    'HLT_Dimuon0_PsiPrime_v6',
    'HLT_Dimuon0_Upsilon_Muon_v18',
    'HLT_Dimuon0_Upsilon_v17',
    'HLT_Dimuon11_Upsilon_v6',
    'HLT_Dimuon3p5_SameSign_v6',
    'HLT_Dimuon7_Upsilon_v7',
    'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5',
    'HLT_DoubleMu4_JpsiTk_Displaced_v6',
    'HLT_DoubleMu4_Jpsi_Displaced_v12',
    'HLT_Mu5_L2Mu3_Jpsi_v8',
    'HLT_Mu5_Track2_Jpsi_v21',
    'HLT_Mu5_Track3p5_Jpsi_v7',
    'HLT_Mu7_Track7_Jpsi_v20',
    'HLT_Tau2Mu_ItTrack_v7' ),
  MuOniaParked = cms.vstring( 'HLT_BTagMu_Jet20_Mu4_v2',
    'HLT_BTagMu_Jet60_Mu4_v2',
    'HLT_Dimuon10_Jpsi_v6',
    'HLT_Dimuon5_PsiPrime_v6',
    'HLT_Dimuon5_Upsilon_v6',
    'HLT_Dimuon7_PsiPrime_v3',
    'HLT_Dimuon8_Jpsi_v7',
    'HLT_Dimuon8_Upsilon_v6',
    'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6',
    'HLT_DoubleMu3p5_LowMass_Displaced_v6',
    'HLT_Mu15_TkMu5_Onia_v1' ),
  MultiJet = cms.vstring( 'HLT_DiJet80_DiJet60_DiJet20_v6',
    'HLT_DoubleJet20_ForwardBackward_v4',
    'HLT_EightJet30_eta3p0_v5',
    'HLT_EightJet35_eta3p0_v5',
    'HLT_ExclDiJet35_HFAND_v4',
    'HLT_ExclDiJet35_HFOR_v4',
    'HLT_ExclDiJet80_HFAND_v4',
    'HLT_QuadJet60_DiJet20_v6',
    'HLT_QuadJet70_v6',
    'HLT_QuadJet80_v6',
    'HLT_QuadJet90_v6',
    'HLT_SixJet35_v6',
    'HLT_SixJet45_v6',
    'HLT_SixJet50_v6' ),
  MultiJet1Parked = cms.vstring( 'HLT_DiJet80_DiJet60_DiJet20_v6',
    'HLT_DoubleJet20_ForwardBackward_v4',
    'HLT_EightJet30_eta3p0_v5',
    'HLT_EightJet35_eta3p0_v5',
    'HLT_ExclDiJet35_HFAND_v4',
    'HLT_ExclDiJet35_HFOR_v4',
    'HLT_ExclDiJet80_HFAND_v4',
    'HLT_QuadJet45_v1',
    'HLT_QuadJet50_v5',
    'HLT_QuadJet60_DiJet20_v6',
    'HLT_QuadJet70_v6',
    'HLT_QuadJet80_v6',
    'HLT_QuadJet90_v6',
    'HLT_SixJet35_v6',
    'HLT_SixJet45_v6',
    'HLT_SixJet50_v6' ),
  NoBPTX = cms.vstring( 'HLT_JetE30_NoBPTX3BX_NoHalo_v16',
    'HLT_JetE30_NoBPTX_v14',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v13',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v5',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4',
    'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v2',
    'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1' ),
  OfflineMonitor = ( cms.vstring( 'AlCa_EcalEtaEBonly_v6',
    'AlCa_EcalEtaEEonly_v6',
    'AlCa_EcalPhiSym_v13',
    'AlCa_EcalPi0EBonly_v6',
    'AlCa_EcalPi0EEonly_v6',
    'AlCa_LumiPixels_Random_v1',
    'AlCa_LumiPixels_ZeroBias_v4',
    'AlCa_LumiPixels_v8',
    'AlCa_RPCMuonNoHits_v9',
    'AlCa_RPCMuonNoTriggers_v9',
    'AlCa_RPCMuonNormalisation_v9',
    'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4',
    'DST_HT250_v4',
    'DST_L1HTT_Or_L1MultiJet_v4',
    'DST_Mu5_HT250_v4',
    'HLT_Activity_Ecal_SC7_v13',
    'HLT_BTagMu_DiJet110_Mu5_v6',
    'HLT_BTagMu_DiJet20_Mu5_v6',
    'HLT_BTagMu_DiJet40_Mu5_v6',
    'HLT_BTagMu_DiJet70_Mu5_v6',
    'HLT_BTagMu_Jet20_Mu4_v2',
    'HLT_BTagMu_Jet300_Mu5_v6',
    'HLT_BTagMu_Jet60_Mu4_v2',
    'HLT_BeamGas_HF_Beam1_v5',
    'HLT_BeamGas_HF_Beam2_v5',
    'HLT_BeamHalo_v13',
    'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_DTErrors_v3',
    'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5',
    'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5',
    'HLT_DiCentralPFJet30_PFMET80_v6',
    'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4',
    'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1',
    'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1',
    'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7',
    'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7',
    'HLT_DiJet80_DiJet60_DiJet20_v6',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5',
    'HLT_DiPFJetAve140_v10',
    'HLT_DiPFJetAve200_v10',
    'HLT_DiPFJetAve260_v10',
    'HLT_DiPFJetAve320_v10',
    'HLT_DiPFJetAve400_v10',
    'HLT_DiPFJetAve40_v9',
    'HLT_DiPFJetAve80_v10',
    'HLT_Dimuon0_Jpsi_Muon_v18',
    'HLT_Dimuon0_Jpsi_NoVertexing_v14',
    'HLT_Dimuon0_Jpsi_v17',
    'HLT_Dimuon0_PsiPrime_v6',
    'HLT_Dimuon0_Upsilon_Muon_v18',
    'HLT_Dimuon0_Upsilon_v17',
    'HLT_Dimuon10_Jpsi_v6',
    'HLT_Dimuon11_Upsilon_v6',
    'HLT_Dimuon3p5_SameSign_v6',
    'HLT_Dimuon5_PsiPrime_v6',
    'HLT_Dimuon5_Upsilon_v6',
    'HLT_Dimuon7_PsiPrime_v3',
    'HLT_Dimuon7_Upsilon_v7',
    'HLT_Dimuon8_Jpsi_v7',
    'HLT_Dimuon8_Upsilon_v6',
    'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4',
    'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4',
    'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8',
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7',
    'HLT_DoubleEle33_CaloIdL_v14',
    'HLT_DoubleEle33_CaloIdT_v10',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12',
    'HLT_DoubleIsoL2Tau30_eta2p1_v1',
    'HLT_DoubleJet20_ForwardBackward_v4',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4',
    'HLT_DoubleMu11_Acoplanarity03_v5',
    'HLT_DoubleMu14_Mass8_PFMET40_v8',
    'HLT_DoubleMu14_Mass8_PFMET50_v8',
    'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6',
    'HLT_DoubleMu3p5_LowMass_Displaced_v6',
    'HLT_DoubleMu4_Acoplanarity03_v5',
    'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5',
    'HLT_DoubleMu4_JpsiTk_Displaced_v6',
    'HLT_DoubleMu4_Jpsi_Displaced_v12',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16',
    'HLT_DoubleMu5_IsoMu5_v20',
    'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6',
    'HLT_DoublePhoton48_HEVT_v8',
    'HLT_DoublePhoton53_HEVT_v2',
    'HLT_DoublePhoton70_v6',
    'HLT_DoublePhoton80_v7',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4',
    'HLT_EightJet30_eta3p0_v5',
    'HLT_EightJet35_eta3p0_v5',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1',
    'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6',
    'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v6',
    'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7',
    'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8',
    'HLT_Ele27_WP80_CentralPFJet80_v9',
    'HLT_Ele27_WP80_PFMET_MT50_v7',
    'HLT_Ele27_WP80_WCandPt80_v9',
    'HLT_Ele27_WP80_v11',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8',
    'HLT_Ele30_CaloIdVT_TrkIdT_v6',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6',
    'HLT_Ele5_SC5_Jpsi_Mass2to15_v4',
    'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2',
    'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2',
    'HLT_ExclDiJet35_HFAND_v4',
    'HLT_ExclDiJet35_HFOR_v4',
    'HLT_ExclDiJet80_HFAND_v4',
    'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10',
    'HLT_GlobalRunHPDNoise_v8',
    'HLT_HT200_AlphaT0p57_v8',
    'HLT_HT200_v6',
    'HLT_HT250_AlphaT0p55_v8',
    'HLT_HT250_AlphaT0p57_v8',
    'HLT_HT250_v7',
    'HLT_HT300_AlphaT0p53_v8',
    'HLT_HT300_AlphaT0p54_v14',
    'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_DoubleDisplacedPFJet60_v10',
    'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_SingleDisplacedPFJet60_v10',
    'HLT_HT300_v7',
    'HLT_HT350_AlphaT0p52_v8',
    'HLT_HT350_AlphaT0p53_v19',
    'HLT_HT350_v7',
    'HLT_HT400_AlphaT0p51_v19',
    'HLT_HT400_AlphaT0p52_v14',
    'HLT_HT400_v7',
    'HLT_HT450_AlphaT0p51_v14',
    'HLT_HT450_v7',
    'HLT_HT500_v7',
    'HLT_HT550_v7',
    'HLT_HT650_Track50_dEdx3p6_v10',
    'HLT_HT650_Track60_dEdx3p7_v10',
    'HLT_HT650_v7',
    'HLT_HT750_v7',
    'HLT_HcalCalibration_v3',
    'HLT_HcalNZS_v10',
    'HLT_HcalPhiSym_v11',
    'HLT_HcalUTCA_v1',
    'HLT_IsoMu12_DoubleCentralJet65_v4',
    'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_IsoMu15_eta2p1_L1ETM20_v7',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10',
    'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4',
    'HLT_IsoMu20_WCandPt80_v4',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v9',
    'HLT_IsoMu20_eta2p1_v7',
    'HLT_IsoMu24_eta2p1_v15',
    'HLT_IsoMu24_v17',
    'HLT_IsoMu30_eta2p1_v15',
    'HLT_IsoMu30_v11',
    'HLT_IsoMu34_eta2p1_v13',
    'HLT_IsoMu40_eta2p1_v10',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1',
    'HLT_IsoTrackHB_v14',
    'HLT_IsoTrackHE_v15',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7',
    'HLT_Jet370_NoJetID_v15',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v16',
    'HLT_JetE30_NoBPTX_v14',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v13',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v5',
    'HLT_L1DoubleEG3_FwdVeto_v2',
    'HLT_L1DoubleJet36Central_v7',
    'HLT_L1ETM100_v2',
    'HLT_L1ETM30_v2',
    'HLT_L1ETM40_v2',
    'HLT_L1ETM70_v2',
    'HLT_L1SingleEG12_v6',
    'HLT_L1SingleEG5_v6',
    'HLT_L1SingleJet16_v7',
    'HLT_L1SingleJet36_v7')+cms.vstring( 'HLT_L1SingleMu12_v2',
    'HLT_L1SingleMuOpen_AntiBPTX_v7',
    'HLT_L1SingleMuOpen_v7',
    'HLT_L1Tech_HBHEHO_totalOR_v6',
    'HLT_L1Tech_HCAL_HF_single_channel_v4',
    'HLT_L1TrackerCosmics_v7',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2DoubleMu23_NoVertex_v11',
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4',
    'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v2',
    'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8',
    'HLT_LogMonitor_v4',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_v10',
    'HLT_MET100_HBHENoiseCleaned_v1',
    'HLT_MET120_HBHENoiseCleaned_v6',
    'HLT_MET120_v13',
    'HLT_MET200_HBHENoiseCleaned_v5',
    'HLT_MET200_v12',
    'HLT_MET300_HBHENoiseCleaned_v5',
    'HLT_MET300_v4',
    'HLT_MET400_HBHENoiseCleaned_v5',
    'HLT_MET400_v7',
    'HLT_MET80_Parked_v5',
    'HLT_MET80_Track50_dEdx3p6_v6',
    'HLT_MET80_Track60_dEdx3p7_v6',
    'HLT_MET80_v5',
    'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4',
    'HLT_Mu12_eta2p1_DiCentral_20_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_v8',
    'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7',
    'HLT_Mu12_v18',
    'HLT_Mu13_Mu8_NoDZ_v1',
    'HLT_Mu13_Mu8_v22',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_Mu15_TkMu5_Onia_v1',
    'HLT_Mu15_eta2p1_DiCentral_20_v1',
    'HLT_Mu15_eta2p1_DiCentral_40_20_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v5',
    'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8',
    'HLT_Mu15_eta2p1_v5',
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu17_Mu8_v22',
    'HLT_Mu17_TkMu8_NoDZ_v1',
    'HLT_Mu17_TkMu8_v14',
    'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Mu17_v5',
    'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_Mu22_Photon22_CaloIdL_v7',
    'HLT_Mu22_TkMu22_v9',
    'HLT_Mu22_TkMu8_v9',
    'HLT_Mu24_eta2p1_v5',
    'HLT_Mu24_v16',
    'HLT_Mu30_Ele30_CaloIdL_v8',
    'HLT_Mu30_eta2p1_v5',
    'HLT_Mu30_v16',
    'HLT_Mu40_PFNoPUHT350_v4',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5',
    'HLT_Mu40_eta2p1_v11',
    'HLT_Mu40_v14',
    'HLT_Mu50_eta2p1_v8',
    'HLT_Mu5_L2Mu3_Jpsi_v8',
    'HLT_Mu5_Track2_Jpsi_v21',
    'HLT_Mu5_Track3p5_Jpsi_v7',
    'HLT_Mu5_v20',
    'HLT_Mu60_PFNoPUHT350_v4',
    'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7',
    'HLT_Mu7_Track7_Jpsi_v20',
    'HLT_Mu8_DiJet30_v7',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7',
    'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_Mu8_QuadJet30_v7',
    'HLT_Mu8_TriJet30_v7',
    'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1',
    'HLT_Mu8_v18',
    'HLT_PFJet140_v9',
    'HLT_PFJet200_v9',
    'HLT_PFJet260_v9',
    'HLT_PFJet320_v9',
    'HLT_PFJet400_v9',
    'HLT_PFJet40_v8',
    'HLT_PFJet80_v9',
    'HLT_PFMET150_v7',
    'HLT_PFMET180_v7',
    'HLT_PFNoPUHT350_Mu15_PFMET45_v4',
    'HLT_PFNoPUHT350_Mu15_PFMET50_v4',
    'HLT_PFNoPUHT350_PFMET100_v4',
    'HLT_PFNoPUHT350_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET45_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET50_v4',
    'HLT_PFNoPUHT400_PFMET100_v4',
    'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4',
    'HLT_PFNoPUHT650_v4',
    'HLT_PFNoPUHT700_v4',
    'HLT_PFNoPUHT750_v4',
    'HLT_Photon135_v7',
    'HLT_Photon150_v4',
    'HLT_Photon160_v4',
    'HLT_Photon20_CaloIdVL_IsoL_v16',
    'HLT_Photon20_CaloIdVL_v4',
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon26_Photon18_v12',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5',
    'HLT_Photon300_NoHE_v5',
    'HLT_Photon30_CaloIdVL_v14',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1',
    'HLT_Photon30_v1',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6',
    'HLT_Photon36_Photon22_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v4',
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6',
    'HLT_Photon50_CaloIdVL_IsoL_v17',
    'HLT_Photon50_CaloIdVL_v10',
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon60_CaloIdL_HT300_v4',
    'HLT_Photon60_CaloIdL_MHT70_v11',
    'HLT_Photon70_CaloIdXL_PFMET100_v7',
    'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4',
    'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4',
    'HLT_Photon75_CaloIdVL_v13',
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon90_CaloIdVL_v10',
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Physics_v5',
    'HLT_PixelTracks_Multiplicity70_v3',
    'HLT_PixelTracks_Multiplicity80_v12',
    'HLT_PixelTracks_Multiplicity90_v3',
    'HLT_QuadJet45_v1',
    'HLT_QuadJet50_v5',
    'HLT_QuadJet60_DiJet20_v6',
    'HLT_QuadJet70_v6',
    'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7',
    'HLT_QuadJet75_55_35_20_VBF_v1',
    'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7',
    'HLT_QuadJet80_v6',
    'HLT_QuadJet90_v6',
    'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6',
    'HLT_QuadPFJet78_61_44_31_VBF_v1',
    'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6',
    'HLT_Random_v2',
    'HLT_RelIso1p0Mu20_v3',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_RelIso1p0Mu5_v6',
    'HLT_RsqMR40_Rsq0p04_v6',
    'HLT_RsqMR45_Rsq0p09_v5',
    'HLT_RsqMR55_Rsq0p09_MR150_v6',
    'HLT_RsqMR60_Rsq0p09_MR150_v6',
    'HLT_RsqMR65_Rsq0p09_MR150_v5',
    'HLT_SingleForJet15_v4',
    'HLT_SingleForJet25_v4',
    'HLT_SixJet35_v6',
    'HLT_SixJet45_v6',
    'HLT_SixJet50_v6',
    'HLT_Tau2Mu_ItTrack_v7',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v18',
    'HLT_TripleMu5_v19',
    'HLT_ZeroBiasPixel_DoubleTrack_v2',
    'HLT_ZeroBias_v7') ),
  OnlineHltMonitor = cms.vstring( 'HLT_DiJet80_DiJet60_DiJet20_v6',
    'HLT_DiPFJetAve140_v10',
    'HLT_DiPFJetAve200_v10',
    'HLT_DiPFJetAve260_v10',
    'HLT_DiPFJetAve320_v10',
    'HLT_DiPFJetAve400_v10',
    'HLT_DiPFJetAve40_v9',
    'HLT_DiPFJetAve80_v10',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v6',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele27_WP80_PFMET_MT50_v7',
    'HLT_Ele27_WP80_v11',
    'HLT_Ele30_CaloIdVT_TrkIdT_v6',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2',
    'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2',
    'HLT_IsoMu20_eta2p1_v7',
    'HLT_IsoMu24_eta2p1_v15',
    'HLT_IsoMu30_eta2p1_v15',
    'HLT_IsoMu34_eta2p1_v13',
    'HLT_IsoMu40_eta2p1_v10',
    'HLT_Jet370_NoJetID_v15',
    'HLT_Mu12_v18',
    'HLT_Mu15_eta2p1_v5',
    'HLT_Mu17_v5',
    'HLT_Mu24_eta2p1_v5',
    'HLT_Mu30_eta2p1_v5',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5',
    'HLT_Mu40_eta2p1_v11',
    'HLT_Mu5_v20',
    'HLT_Mu8_v18',
    'HLT_PFJet140_v9',
    'HLT_PFJet200_v9',
    'HLT_PFJet260_v9',
    'HLT_PFJet320_v9',
    'HLT_PFJet400_v9',
    'HLT_PFJet40_v8',
    'HLT_PFJet80_v9',
    'HLT_RelIso1p0Mu20_v3',
    'HLT_RelIso1p0Mu5_v6',
    'HLT_SingleForJet15_v4',
    'HLT_SingleForJet25_v4' ),
  OnlineMonitor = ( cms.vstring( 'HLT_Activity_Ecal_SC7_v13',
    'HLT_BTagMu_DiJet110_Mu5_v6',
    'HLT_BTagMu_DiJet20_Mu5_v6',
    'HLT_BTagMu_DiJet40_Mu5_v6',
    'HLT_BTagMu_DiJet70_Mu5_v6',
    'HLT_BTagMu_Jet300_Mu5_v6',
    'HLT_BeamGas_HF_Beam1_v5',
    'HLT_BeamGas_HF_Beam2_v5',
    'HLT_BeamHalo_v13',
    'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3',
    'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3',
    'HLT_DTErrors_v3',
    'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5',
    'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5',
    'HLT_DiCentralPFJet30_PFMET80_v6',
    'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4',
    'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7',
    'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7',
    'HLT_DiJet80_DiJet60_DiJet20_v6',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9',
    'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5',
    'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5',
    'HLT_DiPFJetAve140_v10',
    'HLT_DiPFJetAve200_v10',
    'HLT_DiPFJetAve260_v10',
    'HLT_DiPFJetAve320_v10',
    'HLT_DiPFJetAve400_v10',
    'HLT_DiPFJetAve40_v9',
    'HLT_DiPFJetAve80_v10',
    'HLT_Dimuon0_Jpsi_Muon_v18',
    'HLT_Dimuon0_Jpsi_NoVertexing_v14',
    'HLT_Dimuon0_Jpsi_v17',
    'HLT_Dimuon0_PsiPrime_v6',
    'HLT_Dimuon0_Upsilon_Muon_v18',
    'HLT_Dimuon0_Upsilon_v17',
    'HLT_Dimuon11_Upsilon_v6',
    'HLT_Dimuon3p5_SameSign_v6',
    'HLT_Dimuon7_Upsilon_v7',
    'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4',
    'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4',
    'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8',
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7',
    'HLT_DoubleEle33_CaloIdL_v14',
    'HLT_DoubleEle33_CaloIdT_v10',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12',
    'HLT_DoubleIsoL2Tau30_eta2p1_v1',
    'HLT_DoubleJet20_ForwardBackward_v4',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4',
    'HLT_DoubleMu11_Acoplanarity03_v5',
    'HLT_DoubleMu14_Mass8_PFMET40_v8',
    'HLT_DoubleMu14_Mass8_PFMET50_v8',
    'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5',
    'HLT_DoubleMu4_Acoplanarity03_v5',
    'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5',
    'HLT_DoubleMu4_JpsiTk_Displaced_v6',
    'HLT_DoubleMu4_Jpsi_Displaced_v12',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16',
    'HLT_DoubleMu5_IsoMu5_v20',
    'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6',
    'HLT_DoublePhoton48_HEVT_v8',
    'HLT_DoublePhoton53_HEVT_v2',
    'HLT_DoublePhoton70_v6',
    'HLT_DoublePhoton80_v7',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4',
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4',
    'HLT_EightJet30_eta3p0_v5',
    'HLT_EightJet35_eta3p0_v5',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1',
    'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6',
    'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v6',
    'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7',
    'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8',
    'HLT_Ele27_WP80_CentralPFJet80_v9',
    'HLT_Ele27_WP80_PFMET_MT50_v7',
    'HLT_Ele27_WP80_WCandPt80_v9',
    'HLT_Ele27_WP80_v11',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8',
    'HLT_Ele30_CaloIdVT_TrkIdT_v6',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6',
    'HLT_Ele5_SC5_Jpsi_Mass2to15_v4',
    'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v17',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18',
    'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2',
    'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7',
    'HLT_Ele8_CaloIdT_TrkIdVL_v5',
    'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2',
    'HLT_ExclDiJet35_HFAND_v4',
    'HLT_ExclDiJet35_HFOR_v4',
    'HLT_ExclDiJet80_HFAND_v4',
    'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10',
    'HLT_GlobalRunHPDNoise_v8',
    'HLT_HT200_v6',
    'HLT_HT250_AlphaT0p55_v8',
    'HLT_HT250_AlphaT0p57_v8',
    'HLT_HT250_v7',
    'HLT_HT300_AlphaT0p53_v8',
    'HLT_HT300_AlphaT0p54_v14',
    'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_DoubleDisplacedPFJet60_v10',
    'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10',
    'HLT_HT300_SingleDisplacedPFJet60_v10',
    'HLT_HT300_v7',
    'HLT_HT350_AlphaT0p52_v8',
    'HLT_HT350_AlphaT0p53_v19',
    'HLT_HT350_v7',
    'HLT_HT400_AlphaT0p51_v19',
    'HLT_HT400_AlphaT0p52_v14',
    'HLT_HT400_v7',
    'HLT_HT450_AlphaT0p51_v14',
    'HLT_HT450_v7',
    'HLT_HT500_v7',
    'HLT_HT550_v7',
    'HLT_HT650_Track50_dEdx3p6_v10',
    'HLT_HT650_Track60_dEdx3p7_v10',
    'HLT_HT650_v7',
    'HLT_HT750_v7',
    'HLT_HcalNZS_v10',
    'HLT_HcalPhiSym_v11',
    'HLT_HcalUTCA_v1',
    'HLT_IsoMu12_DoubleCentralJet65_v4',
    'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4',
    'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4',
    'HLT_IsoMu15_eta2p1_L1ETM20_v7',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10',
    'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4',
    'HLT_IsoMu20_WCandPt80_v4',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v9',
    'HLT_IsoMu20_eta2p1_v7',
    'HLT_IsoMu24_eta2p1_v15',
    'HLT_IsoMu24_v17',
    'HLT_IsoMu30_eta2p1_v15',
    'HLT_IsoMu30_v11',
    'HLT_IsoMu34_eta2p1_v13',
    'HLT_IsoMu40_eta2p1_v10',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1',
    'HLT_IsoTrackHB_v14',
    'HLT_IsoTrackHE_v15',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7',
    'HLT_Jet370_NoJetID_v15',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v16',
    'HLT_JetE30_NoBPTX_v14',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v13',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v5',
    'HLT_L1DoubleEG3_FwdVeto_v2',
    'HLT_L1DoubleJet36Central_v7',
    'HLT_L1ETM100_v2',
    'HLT_L1ETM30_v2',
    'HLT_L1ETM40_v2',
    'HLT_L1ETM70_v2',
    'HLT_L1SingleEG12_v6',
    'HLT_L1SingleEG5_v6',
    'HLT_L1SingleJet16_v7',
    'HLT_L1SingleJet36_v7',
    'HLT_L1SingleMu12_v2',
    'HLT_L1SingleMuOpen_AntiBPTX_v7',
    'HLT_L1SingleMuOpen_v7',
    'HLT_L1Tech_HBHEHO_totalOR_v6',
    'HLT_L1Tech_HCAL_HF_single_channel_v4',
    'HLT_L1TrackerCosmics_v7',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2DoubleMu23_NoVertex_v11',
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4',
    'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v2',
    'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_v10',
    'HLT_MET120_HBHENoiseCleaned_v6',
    'HLT_MET120_v13',
    'HLT_MET200_HBHENoiseCleaned_v5',
    'HLT_MET200_v12',
    'HLT_MET300_HBHENoiseCleaned_v5',
    'HLT_MET300_v4',
    'HLT_MET400_HBHENoiseCleaned_v5',
    'HLT_MET400_v7',
    'HLT_MET80_Track50_dEdx3p6_v6',
    'HLT_MET80_Track60_dEdx3p7_v6',
    'HLT_MET80_v5',
    'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4',
    'HLT_Mu12_eta2p1_DiCentral_20_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8')+cms.vstring( 'HLT_Mu12_eta2p1_DiCentral_40_20_v8',
    'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7',
    'HLT_Mu12_v18',
    'HLT_Mu13_Mu8_NoDZ_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8',
    'HLT_Mu15_eta2p1_DiCentral_20_v1',
    'HLT_Mu15_eta2p1_DiCentral_40_20_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v5',
    'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8',
    'HLT_Mu15_eta2p1_v5',
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu17_Mu8_v22',
    'HLT_Mu17_TkMu8_NoDZ_v1',
    'HLT_Mu17_TkMu8_v14',
    'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Mu17_v5',
    'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_Mu22_Photon22_CaloIdL_v7',
    'HLT_Mu22_TkMu22_v9',
    'HLT_Mu22_TkMu8_v9',
    'HLT_Mu24_eta2p1_v5',
    'HLT_Mu24_v16',
    'HLT_Mu30_Ele30_CaloIdL_v8',
    'HLT_Mu30_eta2p1_v5',
    'HLT_Mu30_v16',
    'HLT_Mu40_PFNoPUHT350_v4',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5',
    'HLT_Mu40_eta2p1_v11',
    'HLT_Mu40_v14',
    'HLT_Mu50_eta2p1_v8',
    'HLT_Mu5_L2Mu3_Jpsi_v8',
    'HLT_Mu5_Track2_Jpsi_v21',
    'HLT_Mu5_Track3p5_Jpsi_v7',
    'HLT_Mu5_v20',
    'HLT_Mu60_PFNoPUHT350_v4',
    'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7',
    'HLT_Mu7_Track7_Jpsi_v20',
    'HLT_Mu8_DiJet30_v7',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7',
    'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_Mu8_QuadJet30_v7',
    'HLT_Mu8_TriJet30_v7',
    'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1',
    'HLT_Mu8_v18',
    'HLT_PFJet140_v9',
    'HLT_PFJet200_v9',
    'HLT_PFJet260_v9',
    'HLT_PFJet320_v9',
    'HLT_PFJet400_v9',
    'HLT_PFJet40_v8',
    'HLT_PFJet80_v9',
    'HLT_PFMET150_v7',
    'HLT_PFMET180_v7',
    'HLT_PFNoPUHT350_Mu15_PFMET45_v4',
    'HLT_PFNoPUHT350_Mu15_PFMET50_v4',
    'HLT_PFNoPUHT350_PFMET100_v4',
    'HLT_PFNoPUHT350_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET45_v4',
    'HLT_PFNoPUHT400_Mu5_PFMET50_v4',
    'HLT_PFNoPUHT400_PFMET100_v4',
    'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4',
    'HLT_PFNoPUHT650_v4',
    'HLT_PFNoPUHT700_v4',
    'HLT_PFNoPUHT750_v4',
    'HLT_Photon135_v7',
    'HLT_Photon150_v4',
    'HLT_Photon160_v4',
    'HLT_Photon20_CaloIdVL_IsoL_v16',
    'HLT_Photon20_CaloIdVL_v4',
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon26_Photon18_v12',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5',
    'HLT_Photon300_NoHE_v5',
    'HLT_Photon30_CaloIdVL_v14',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6',
    'HLT_Photon36_Photon22_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v4',
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6',
    'HLT_Photon50_CaloIdVL_IsoL_v17',
    'HLT_Photon50_CaloIdVL_v10',
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon60_CaloIdL_HT300_v4',
    'HLT_Photon60_CaloIdL_MHT70_v11',
    'HLT_Photon70_CaloIdXL_PFMET100_v7',
    'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4',
    'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4',
    'HLT_Photon75_CaloIdVL_v13',
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Photon90_CaloIdVL_v10',
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5',
    'HLT_Physics_v5',
    'HLT_PixelTracks_Multiplicity70_v3',
    'HLT_PixelTracks_Multiplicity80_v12',
    'HLT_PixelTracks_Multiplicity90_v3',
    'HLT_QuadJet60_DiJet20_v6',
    'HLT_QuadJet70_v6',
    'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7',
    'HLT_QuadJet75_55_35_20_VBF_v1',
    'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7',
    'HLT_QuadJet80_v6',
    'HLT_QuadJet90_v6',
    'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6',
    'HLT_QuadPFJet78_61_44_31_VBF_v1',
    'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6',
    'HLT_Random_v2',
    'HLT_RelIso1p0Mu20_v3',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4',
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4',
    'HLT_RelIso1p0Mu5_v6',
    'HLT_RsqMR40_Rsq0p04_v6',
    'HLT_RsqMR55_Rsq0p09_MR150_v6',
    'HLT_RsqMR60_Rsq0p09_MR150_v6',
    'HLT_RsqMR65_Rsq0p09_MR150_v5',
    'HLT_SingleForJet15_v4',
    'HLT_SingleForJet25_v4',
    'HLT_SixJet35_v6',
    'HLT_SixJet45_v6',
    'HLT_SixJet50_v6',
    'HLT_Tau2Mu_ItTrack_v7',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v18',
    'HLT_TripleMu5_v19',
    'HLT_ZeroBiasPixel_DoubleTrack_v2',
    'HLT_ZeroBias_v7') ),
  ParkingMonitor = cms.vstring( 'HLT_BTagMu_Jet20_Mu4_v2',
    'HLT_BTagMu_Jet60_Mu4_v2',
    'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1',
    'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1',
    'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5',
    'HLT_Dimuon10_Jpsi_v6',
    'HLT_Dimuon5_PsiPrime_v6',
    'HLT_Dimuon5_Upsilon_v6',
    'HLT_Dimuon7_PsiPrime_v3',
    'HLT_Dimuon8_Jpsi_v7',
    'HLT_Dimuon8_Upsilon_v6',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4',
    'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6',
    'HLT_DoubleMu3p5_LowMass_Displaced_v6',
    'HLT_HT200_AlphaT0p57_v8',
    'HLT_MET100_HBHENoiseCleaned_v1',
    'HLT_MET80_Parked_v5',
    'HLT_Mu13_Mu8_v22',
    'HLT_Mu15_TkMu5_Onia_v1',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1',
    'HLT_Photon30_v1',
    'HLT_Physics_Parked_v1',
    'HLT_QuadJet45_v1',
    'HLT_QuadJet50_v5',
    'HLT_RsqMR45_Rsq0p09_v5',
    'HLT_ZeroBias_Parked_v1' ),
  PhotonHad = cms.vstring( 'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6',
    'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6',
    'HLT_Photon60_CaloIdL_HT300_v4',
    'HLT_Photon60_CaloIdL_MHT70_v11',
    'HLT_Photon70_CaloIdXL_PFMET100_v7',
    'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4',
    'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v9',
    'AlCa_RPCMuonNoTriggers_v9',
    'AlCa_RPCMuonNormalisation_v9' ),
  SingleElectron = cms.vstring( 'HLT_Ele22_CaloIdL_CaloIsoVL_v6',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1',
    'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1',
    'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele27_WP80_CentralPFJet80_v9',
    'HLT_Ele27_WP80_PFMET_MT50_v7',
    'HLT_Ele27_WP80_WCandPt80_v9',
    'HLT_Ele27_WP80_v11',
    'HLT_Ele30_CaloIdVT_TrkIdT_v6',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11',
    'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2',
    'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2' ),
  SingleMu = cms.vstring( 'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4',
    'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1',
    'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu20_WCandPt80_v4',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v9',
    'HLT_IsoMu20_eta2p1_v7',
    'HLT_IsoMu24_eta2p1_v15',
    'HLT_IsoMu24_v17',
    'HLT_IsoMu30_eta2p1_v15',
    'HLT_IsoMu30_v11',
    'HLT_IsoMu34_eta2p1_v13',
    'HLT_IsoMu40_eta2p1_v10',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2',
    'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2',
    'HLT_Mu12_eta2p1_DiCentral_20_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8',
    'HLT_Mu12_eta2p1_DiCentral_40_20_v8',
    'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7',
    'HLT_Mu12_v18',
    'HLT_Mu15_eta2p1_DiCentral_20_v1',
    'HLT_Mu15_eta2p1_DiCentral_40_20_v1',
    'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8',
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8',
    'HLT_Mu15_eta2p1_v5',
    'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4',
    'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2',
    'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1',
    'HLT_Mu24_eta2p1_v5',
    'HLT_Mu24_v16',
    'HLT_Mu30_eta2p1_v5',
    'HLT_Mu30_v16',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5',
    'HLT_Mu40_eta2p1_v11',
    'HLT_Mu40_v14',
    'HLT_Mu50_eta2p1_v8',
    'HLT_Mu5_v20',
    'HLT_RelIso1p0Mu20_v3',
    'HLT_RelIso1p0Mu5_v6' ),
  SinglePhoton = cms.vstring( 'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4',
    'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4',
    'HLT_L1DoubleEG3_FwdVeto_v2',
    'HLT_Photon135_v7',
    'HLT_Photon150_v4',
    'HLT_Photon160_v4',
    'HLT_Photon20_CaloIdVL_IsoL_v16',
    'HLT_Photon20_CaloIdVL_v4',
    'HLT_Photon300_NoHE_v5',
    'HLT_Photon30_CaloIdVL_v14',
    'HLT_Photon50_CaloIdVL_IsoL_v17',
    'HLT_Photon50_CaloIdVL_v10',
    'HLT_Photon75_CaloIdVL_v13',
    'HLT_Photon90_CaloIdVL_v10' ),
  SinglePhotonParked = cms.vstring( 'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4',
    'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4',
    'HLT_L1DoubleEG3_FwdVeto_v2',
    'HLT_Photon135_v7',
    'HLT_Photon150_v4',
    'HLT_Photon160_v4',
    'HLT_Photon20_CaloIdVL_IsoL_v16',
    'HLT_Photon20_CaloIdVL_v4',
    'HLT_Photon300_NoHE_v5',
    'HLT_Photon30_CaloIdVL_v14',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1',
    'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1',
    'HLT_Photon30_v1',
    'HLT_Photon50_CaloIdVL_IsoL_v17',
    'HLT_Photon50_CaloIdVL_v10',
    'HLT_Photon75_CaloIdVL_v13',
    'HLT_Photon90_CaloIdVL_v10' ),
  Tau = cms.vstring( 'HLT_DoubleIsoL2Tau30_eta2p1_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_v10' ),
  TauParked = cms.vstring( 'HLT_DoubleIsoL2Tau30_eta2p1_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1',
    'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10',
    'HLT_LooseIsoPFTau35_Trk20_Prong1_v10' ),
  TauPlusX = cms.vstring( 'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1',
    'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1',
    'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7',
    'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7',
    'HLT_IsoMu15_eta2p1_L1ETM20_v7',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1',
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1',
    'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v5',
    'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7',
    'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1' ),
  TestEnablesEcalHcalDT = cms.vstring( 'HLT_DTCalibration_v2',
    'HLT_EcalCalibration_v3',
    'HLT_HcalCalibration_v3' ),
  TestEnablesTracker = cms.vstring( 'HLT_TrackerCalibration_v3' ),
  VBF1Parked = cms.vstring( 'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1',
    'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1',
    'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5',
    'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5' ),
  ZeroBiasParked = cms.vstring( 'HLT_ZeroBias_Parked_v1' )
)

process.GlobalTag = cms.ESSource( "PoolDBESSource",
    globaltag = cms.string( "GR_H_V32::All" ),
    RefreshEachRun = cms.untracked.bool( True ),
    RefreshOpenIOVs = cms.untracked.bool( False ),
    toGet = cms.VPSet( 
    ),
    DBParameters = cms.PSet( 
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialPeriod = cms.untracked.int32( 10 )
    ),
    RefreshAlways = cms.untracked.bool( False ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG" ),
    ReconnectEachRun = cms.untracked.bool( True ),
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    timetype = cms.string( "runnumber" )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalMappingRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool( False ),
    toGet = cms.untracked.vstring( 'GainWidths' )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring( 'Geometry/CMSCommonData/data/normal/cmsextent.xml',
      'Geometry/CMSCommonData/data/cms.xml',
      'Geometry/CMSCommonData/data/cmsMagneticField.xml',
      'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml',
      'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml' ),
    rootNodeName = cms.string( "cmsMagneticField:MAGF" )
)

process.hltIter4ESPTrajectoryBuilderITReg = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter4ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter4ESPTrajectoryBuilderITReg" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter4ESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClustersReg" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter4SiStripClustersReg" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter4ESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter4ClustersRefRemovalReg" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter3ESPTrajectoryBuilderITReg = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter3ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryBuilderITReg" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter3ESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClustersReg" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter3SiStripClustersReg" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter3ESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter3ClustersRefRemovalReg" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter3ESPLayerTripletsReg = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix2+FPix1_pos+FPix2_pos',
    'BPix2+FPix1_neg+FPix2_neg',
    'FPix1_pos+FPix2_pos+TEC1_pos',
    'FPix1_neg+FPix2_neg+TEC1_neg',
    'FPix2_pos+TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC2_neg+TEC3_neg',
    'BPix2+BPix3+TIB1',
    'BPix2+BPix3+TIB2',
    'BPix1+BPix3+TIB1',
    'BPix1+BPix3+TIB2',
    'BPix1+BPix2+TIB1',
    'BPix1+BPix2+TIB2' ),
  ComponentName = cms.string( "hltIter3ESPLayerTripletsReg" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
process.hltIter2ESPTrajectoryBuilderITReg = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter2ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryBuilderITReg" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter2ESPPixelLayerPairsReg = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter2ESPPixelLayerPairsReg" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter2ESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClustersReg" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter2SiStripClustersReg" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter2ESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalReg" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1ESPTrajectoryBuilderITReg = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter1ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryBuilderITReg" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter1ESPPixelLayerTripletsReg = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter1ESPPixelLayerTripletsReg" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalReg" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter1ESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClustersReg" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter1SiStripClustersReg" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter1ESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalReg" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltESPTrajectoryBuilderITReg = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderITReg" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClustersReg" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltSiStripClustersReg" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
process.AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
  valueOverride = cms.int32( -1 ),
  mapLabels = cms.untracked.vstring( '090322_3_8t',
    '0t',
    '071212_2t',
    '071212_3t',
    '071212_3_5t',
    '090322_3_8t',
    '071212_4t' )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  useRealWireGeometry = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  alignmentsLabel = cms.string( "" ),
  useGangedStripsInME1a = cms.bool( True ),
  debugV = cms.untracked.bool( False ),
  useOnlyWiresInME1a = cms.bool( False ),
  useDDD = cms.bool( False ),
  useCentreTIOffsets = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
process.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder" )
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService" )
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  CalibRHAlgo = cms.PSet( 
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 7, 7, 7, 8, 9 ),
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    killDeadChannels = cms.bool( True ),
    ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14 ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    EELaserMIN = cms.double( 0.5 ),
    EBLaserMAX = cms.double( 2.0 ),
    EELaserMAX = cms.double( 3.0 )
  ),
  ComponentName = cms.string( "" ),
  UncalibRHAlgo = cms.PSet(  Type = cms.string( "EcalUncalibRecHitWorkerWeights" ) ),
  DCCDataUnpacker = cms.PSet( 
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    tccUnpacking = cms.bool( False ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    feIdCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    forceKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
  ),
  ElectronicsMapper = cms.PSet( 
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP" )
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  useDDD = cms.untracked.bool( False ),
  compatibiltyWith11 = cms.untracked.bool( True )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  printDebug = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  APVGain = cms.VPSet( 
    cms.PSet(  Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(  Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  ),
  AutomaticNormalization = cms.bool( False )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  PrintDebug = cms.untracked.bool( False ),
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    )
  ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 )
)
process.SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
  ZFieldInTesla = cms.double( 0.0 ),
  label = cms.untracked.string( "slave_0" )
)
process.SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "2_0T" ) ),
  label = cms.untracked.string( "slave_20" )
)
process.SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_0T" ) ),
  label = cms.untracked.string( "slave_30" )
)
process.SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_5T" ) ),
  label = cms.untracked.string( "slave_35" )
)
process.SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_8T" ) ),
  label = cms.untracked.string( "slave_38" )
)
process.SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "4_0T" ) ),
  label = cms.untracked.string( "slave_40" )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
process.StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEESProducer",
  TanDiffusionAngle = cms.double( 0.01 ),
  UncertaintyScaling = cms.double( 1.42 ),
  ThicknessRelativeUncertainty = cms.double( 0.02 ),
  MaybeNoiseThreshold = cms.double( 3.5 ),
  ComponentName = cms.string( "StripCPEfromTrackAngle" ),
  MinimumUncertainty = cms.double( 0.01 ),
  NoiseThreshold = cms.double( 2.3 )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  fromDDD = cms.bool( False )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
process.VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "0t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_0" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_2t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_20" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3t" ),
  version = cms.string( "grid_1103l_071212_3t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_30" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3_5t" ),
  version = cms.string( "grid_1103l_071212_3_5t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_35" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  overrideMasterSector = cms.bool( False ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  label = cms.untracked.string( "090322_3_8t" ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_38" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_4t" ),
  version = cms.string( "grid_1103l_071212_4t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_40" ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vuint32( 0 ),
    kProblematic = cms.vuint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
    kRecovered = cms.vuint32(  ),
    kTime = cms.vuint32(  ),
    kWeird = cms.vuint32(  ),
    kBad = cms.vuint32( 11, 12, 13, 14, 15, 16 )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HFDigiTime',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHEFlatNoise',
  'HBHESpikeNoise',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFS8S1Ratio',
  'HFPET' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer" )
process.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  categoryVariableName = cms.string( "vertexCategory" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  correctVertexMass = cms.bool( True ),
  trackSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
process.hltESPAK5CaloL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL1FastJetCorrectionESProducer',
    'hltESPL2RelativeCorrectionESProducer',
    'hltESPL3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPAK5CaloL2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL2RelativeCorrectionESProducer',
    'hltESPL3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPAK5PFL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL1PFFastJetCorrectionESProducer',
    'hltESPL2PFRelativeCorrectionESProducer',
    'hltESPL3PFAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPAK5PFNoPUL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL1PFNoPUFastJetCorrectionESProducer',
    'hltESPL2PFNoPURelativeCorrectionESProducer',
    'hltESPL3PFNoPUAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
process.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" )
)
process.hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" )
)
process.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
process.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
process.hltESPCkf3HitTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPCkf3HitTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryFilter" )
)
process.hltESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPCkfTrajectoryBuilderForHI = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilterForHI" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilderForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPCkfTrajectoryFilter" )
)
process.hltESPCkfTrajectoryFilterForHI = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 6 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 11.0 )
  ),
  ComponentName = cms.string( "hltESPCkfTrajectoryFilterForHI" )
)
process.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPESUnpackerWorker = cms.ESProducer( "ESUnpackerWorkerESProducer",
  RHAlgo = cms.PSet( 
    ESRecoAlgo = cms.int32( 0 ),
    Type = cms.string( "ESRecHitWorker" )
  ),
  DCCDataUnpacker = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) ),
  ComponentName = cms.string( "hltESPESUnpackerWorker" )
)
process.hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" )
)
process.hltESPElectronChi2 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 2000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPElectronChi2" )
)
process.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
process.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 10.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" )
process.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
process.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
process.hltESPHIMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg',
    'FPix2_pos+TEC1_pos',
    'FPix2_pos+TEC2_pos',
    'TEC1_pos+TEC2_pos',
    'TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC1_neg',
    'FPix2_neg+TEC2_neg',
    'TEC1_neg+TEC2_neg',
    'TEC2_neg+TEC3_neg' ),
  ComponentName = cms.string( "hltESPHIMixedLayerPairs" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPHIPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPHIPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "Fake" ),
  ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKSmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
process.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
process.hltESPL1FastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( 'hltKT6CaloJets','rho' ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L1FastJet" )
)
process.hltESPL1PFFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( 'hltKT6PFJets','rho' ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L1FastJet" )
)
process.hltESPL1PFNoPUFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( 'hltKT6PFJets','rho' ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L1FastJet" )
)
process.hltESPL2PFNoPURelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L2Relative" )
)
process.hltESPL2PFRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L2Relative" )
)
process.hltESPL2RelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L2Relative" )
)
process.hltESPL3AbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L3Absolute" )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPL3PFAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L3Absolute" )
)
process.hltESPL3PFNoPUAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L3Absolute" )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltESPMeasurementTrackerForHI = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( False ),
  Regional = cms.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripRawToDigi' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltHISiStripClustersNonRegional" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerForHI" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltESPMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg',
    'FPix2_pos+TEC1_pos',
    'FPix2_pos+TEC2_pos',
    'TEC1_pos+TEC2_pos',
    'TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC1_neg',
    'FPix2_neg+TEC2_neg',
    'TEC1_neg+TEC2_neg',
    'TEC2_neg+TEC3_neg' ),
  ComponentName = cms.string( "hltESPMixedLayerPairs" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPMuTrackJpsiEffTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiEffTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPMuTrackJpsiEffTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPMuTrackJpsiEffTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 9 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPMuTrackJpsiEffTrajectoryFilter" )
)
process.hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" )
)
process.hltESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPMuonCkfTrajectoryBuilderSeedHit = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilderSeedHit" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPMuonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryFilter" )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer" )
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  EdgeClusterErrorX = cms.double( 50.0 ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  UseErrorsFromTemplates = cms.bool( True ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  IrradiationBiasCorrection = cms.bool( False ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  inflate_errors = cms.bool( False ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True )
)
process.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
process.hltESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPPixelLayerTripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3' ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHB" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPPixelLayerTripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHE" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPPixelLayerTripletsReg = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsReg" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    useErrorsFromParam = cms.bool( True ),
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    useErrorsFromParam = cms.bool( True ),
    HitProducer = cms.string( "hltSiPixelRecHitsReg" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.03 ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKSmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
process.hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
process.hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
process.hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  ipSign = cms.string( "any" )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
process.hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
process.hltESPTrackCounting3D1st = cms.ESProducer( "TrackCountingESProducer",
  deltaR = cms.double( -1.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  maximumDecayLength = cms.double( 5.0 ),
  nthTrack = cms.int32( 1 )
)
process.hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  deltaR = cms.double( -1.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  maximumDecayLength = cms.double( 5.0 ),
  nthTrack = cms.int32( 2 )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" ),
  trackerGeometryLabel = cms.untracked.string( "" )
)
process.hltESPTrajectoryBuilderForElectrons = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterForElectrons" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderForElectrons" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPElectronChi2" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
process.hltESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPTrajectoryBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterL3" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderL3" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTrajectoryFilterForElectrons = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    minPt = cms.double( 2.0 ),
    minHitsMinPt = cms.int32( -1 ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterForElectrons" )
)
process.hltESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterIT" )
)
process.hltESPTrajectoryFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 1000000000 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterL3" )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPbJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryFilter" )
)
process.hltHIAllESPCkf3HitTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPCkf3HitTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltHIAllESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltHIAllESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltHISiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltHISiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltHIAllESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltHIAllESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPMuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltHIAllESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter1ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter1SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter1ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1ESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter1ESPPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter1ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter1ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter1ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.2 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryFilterIT" )
)
process.hltIter3ESPLayerTripletsPA = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix2+FPix1_pos+FPix2_pos',
    'BPix2+FPix1_neg+FPix2_neg',
    'FPix1_pos+FPix2_pos+TEC1_pos',
    'FPix1_neg+FPix2_neg+TEC1_neg',
    'FPix2_pos+TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC2_neg+TEC3_neg',
    'BPix2+BPix3+TIB1',
    'BPix2+BPix3+TIB2',
    'BPix1+BPix3+TIB1',
    'BPix1+BPix3+TIB2',
    'BPix1+BPix2+TIB1',
    'BPix1+BPix2+TIB2' ),
  ComponentName = cms.string( "hltIter3ESPLayerTripletsPA" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
process.hltIter3ESPTrajectoryBuilderITPA = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter3ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryBuilderITPA" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter3ESPMeasurementTrackerPA = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltPAFullTrackIter3SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter3ESPMeasurementTrackerPA" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltPAFullTrackIter3ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1ESPPixelLayerTripletsPA = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter1ESPPixelLayerTripletsPA" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter2ESPPixelLayerPairsPA = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter2ESPPixelLayerPairsPA" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltPAFullTrackIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter2ESPTrajectoryBuilderITPA = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter2ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryBuilderITPA" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter2ESPMeasurementTrackerPA = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltPAFullTrackIter2SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter2ESPMeasurementTrackerPA" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltPAFullTrackIter2ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1ESPTrajectoryBuilderITPA = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter1ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryBuilderITPA" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter1ESPMeasurementTrackerPA = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltPAFullTrackIter1SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter1ESPMeasurementTrackerPA" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltPAFullTrackIter1ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1Tau3MuESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter1Tau3MuSiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter1Tau3MuESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter1Tau3MuClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter1Tau3MuESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter1Tau3MuESPPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter1Tau3MuESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter1ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter1Tau3MuESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter2ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter2SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter2ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter2ESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter2ESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter2ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter2ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter2ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryFilterIT" )
)
process.hltIter2Tau3MuESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter2SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter2Tau3MuESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter2Tau3MuClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter2Tau3MuESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter2Tau3MuESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
process.hltIter2Tau3MuESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter2ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter2Tau3MuESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter3ESPLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix2+FPix1_pos+FPix2_pos',
    'BPix2+FPix1_neg+FPix2_neg',
    'FPix1_pos+FPix2_pos+TEC1_pos',
    'FPix1_neg+FPix2_neg+TEC1_neg',
    'FPix2_pos+TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC2_neg+TEC3_neg',
    'BPix2+BPix3+TIB1',
    'BPix2+BPix3+TIB2',
    'BPix1+BPix3+TIB1',
    'BPix1+BPix3+TIB2',
    'BPix1+BPix2+TIB1',
    'BPix1+BPix2+TIB2' ),
  ComponentName = cms.string( "hltIter3ESPLayerTriplets" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
process.hltIter3ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter3SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter3ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter3ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter3ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter3ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 0 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryFilterIT" )
)
process.hltIter3Tau3MuESPLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix2+FPix1_pos+FPix2_pos',
    'BPix2+FPix1_neg+FPix2_neg',
    'FPix1_pos+FPix2_pos+TEC1_pos',
    'FPix1_neg+FPix2_neg+TEC1_neg',
    'FPix2_pos+TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC2_neg+TEC3_neg',
    'BPix2+BPix3+TIB1',
    'BPix2+BPix3+TIB2',
    'BPix1+BPix3+TIB1',
    'BPix1+BPix3+TIB2',
    'BPix1+BPix2+TIB1',
    'BPix1+BPix2+TIB2' ),
  ComponentName = cms.string( "hltIter3Tau3MuESPLayerTriplets" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3Tau3MuClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
process.hltIter3Tau3MuESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter3Tau3MuSiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter3Tau3MuESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter3Tau3MuClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter3Tau3MuESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter3ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter3Tau3MuESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltIter4ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter4SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter4ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter4ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter4ESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'TIB1+TIB2' ),
  ComponentName = cms.string( "hltIter4ESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet(  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet(  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
process.hltIter4ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter4ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter4ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
process.hltIter4ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 0 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 6 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter4ESPTrajectoryFilterIT" )
)
process.hltIter4Tau3MuESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter4Tau3MuSiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter4Tau3MuESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter4Tau3MuClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
process.hltIter4Tau3MuESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter4ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter4Tau3MuESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
process.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )

process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    luminosityProduct = cms.untracked.InputTag( "hltScalersRawToDigi" ),
    enableTimingExclusive = cms.untracked.bool( False ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    enableDQMbyModule = cms.untracked.bool( False ),
    dqmLuminosityResolution = cms.untracked.double( 1.0E31 ),
    skipFirstPath = cms.untracked.bool( False ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( False ),
    enableDQMbyPathTotal = cms.untracked.bool( False ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( False ),
    enableDQMbyLuminosity = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    supportedProcesses = cms.untracked.vuint32( 8, 12, 16, 24, 32 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    dqmLuminosityRange = cms.untracked.double( 1.0E34 ),
    enableDQMbyPathActive = cms.untracked.bool( False ),
    enableDQMbyPathDetails = cms.untracked.bool( False ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMbyPathCounters = cms.untracked.bool( False )
)
process.DQM = cms.Service( "DQM",
    publishFrequency = cms.untracked.double( 5.0 ),
    debug = cms.untracked.bool( False ),
    collectorPort = cms.untracked.int32( 0 ),
    collectorHost = cms.untracked.string( "" )
)
process.DQMStore = cms.Service( "DQMStore",
)
process.DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
    processingMode = cms.untracked.string( "HLT" ),
    fedIntegrityFolder = cms.untracked.string( "DT/FEDIntegrity_EvF" ),
    getSCInfo = cms.untracked.bool( True )
)
process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet( 
      threshold = cms.untracked.string( "ERROR" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)
process.MicroStateService = cms.Service( "MicroStateService",
)
process.ModuleWebRegistry = cms.Service( "ModuleWebRegistry",
)
process.PrescaleService = cms.Service( "PrescaleService",
    forceDefault = cms.bool( False ),
    prescaleTable = cms.VPSet(  *(
      cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet20_Mu5_v6" ),
        prescales = cms.vuint32( 10, 8, 8, 7, 4, 4, 4, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet40_Mu5_v6" ),
        prescales = cms.vuint32( 2, 2, 2, 2, 1, 1, 1, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet70_Mu5_v6" ),
        prescales = cms.vuint32( 11, 10, 10, 8, 5, 5, 5, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet110_Mu5_v6" ),
        prescales = cms.vuint32( 3, 2, 2, 2, 1, 1, 1, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_BTagMu_Jet300_Mu5_v6" ),
        prescales = cms.vuint32( 1, 1, 1, 1, 1, 1, 1, 0, 0 )
      ),
) ),
    lvl1DefaultLabel = cms.string( "3e33" ),
    lvl1Labels = cms.vstring( '9e33nopark',
      '8e33nopark',
      '8e33',
      '7e33',
      '6e33',
      '4e33',
      '2e33',
      '5e32',
      'CirculatingBeam' )
)
process.UpdaterService = cms.Service( "UpdaterService",
)

process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    unpackSharedRegions = cms.bool( False ),
    numberOfGctSamplesToUnpack = cms.uint32( 1 ),
    verbose = cms.untracked.bool( False ),
    numberOfRctSamplesToUnpack = cms.uint32( 1 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    unpackerVersion = cms.uint32( 0 ),
    gctFedId = cms.untracked.int32( 745 ),
    hltMode = cms.bool( True )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltGctDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltGctDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltGctDigis" ),
    etTotalSource = cms.InputTag( "hltGctDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltGctDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltGctDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltGctDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltGctDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltGctDigis" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sL1Mu3JetC16WdEtaPhi2 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_JetC16_WdEtaPhi2" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreBTagMuDiJet20Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    workerName = cms.string( "" )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    JetJobPSet = cms.VPSet( 
    ),
    sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
    doES = cms.bool( False ),
    type = cms.string( "all" ),
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    EmJobPSet = cms.VPSet( 
    ),
    CandJobPSet = cms.VPSet( 
    ),
    MuonJobPSet = cms.PSet(  ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    splitOutput = cms.bool( True ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    sourceTag = cms.InputTag( "hltEcalRegionalRestFEDs" ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    UnpackZDC = cms.untracked.bool( True ),
    FilterDataQuality = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    firstSample = cms.int32( 0 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HBHE" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet( 
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet( 
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    hscpParameters = cms.PSet( 
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet( 
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet( 
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    digistat = cms.PSet( 
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HF" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHitAll:EcalRecHitsEB','hltEcalRecHitAll:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltKT6CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 1 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 5.0 ),
    doRhoFastjet = cms.bool( True ),
    jetAlgorithm = cms.string( "Kt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.6 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
process.hltAntiKT5CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.5 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
process.hltCaloJetIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltAntiKT5CaloJets" ),
    JetIDParams = cms.PSet( 
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
process.hltCaloJetL1FastJetCorrected = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( "hltCaloJetIDPassed" ),
    correctors = cms.vstring( 'hltESPAK5CaloL1L2L3' )
)
process.hltBDiJet20L1FastJetCentral = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    dataType = cms.string( "DDU" ),
    fedbyType = cms.bool( False ),
    readOutParameters = cms.PSet( 
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet( 
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( False ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet( 
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( False ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet( 
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    UseSelectiveUnpacking = cms.bool( True ),
    UseExaminer = cms.bool( True ),
    ErrorMask = cms.uint32( 0x0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    UseFormatStatus = cms.bool( True ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    Debug = cms.untracked.bool( False ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.0070 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( True ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.0020, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.0020, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.0040, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.0080, 0.0 ),
    CSC_24 = cms.vdouble( 0.0040, 0.021, -0.0020, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.0030, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.0040, -0.013, 0.029, 0.0030, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.0040, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.0030, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.0030, 0.0050, 0.0050, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.0030, 0.0050, 0.0050, 0.608, 0.076, 0.0 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.0010, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.0080, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.0020, 0.111, -0.0030, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.0050, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.0070, 0.0 )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL1extraParticles" ),
    L1MaxEta = cms.double( 2.5 ),
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 1 ),
    GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
    UseOfflineSeed = cms.untracked.bool( True ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 2 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True )
    )
)
process.hltBSoftMuonGetJetsFromDiJet20L1FastJet = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltBDiJet20L1FastJetCentral" )
)
process.hltSelector4JetsDiJet20L1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltBSoftMuonGetJetsFromDiJet20L1FastJet" )
)
process.hltBSoftMuonDiJet20L1FastJetL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelector4JetsDiJet20L1FastJet" ),
    etMin = cms.double( 20.0 )
)
process.hltBSoftMuonDiJet20L1FastJetL25TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltL2Muons" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet20L1FastJetL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet20L1FastJetL25TagInfos' )
)
process.hltBSoftMuonDiJet20L1FastJetL25FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( False ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetL25BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    CheckPixelOrder = cms.bool( False ),
    IncludeErrors = cms.bool( False ),
    UseCablingTree = cms.untracked.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True )
    )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
    InputModuleLabel = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet( 
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIState" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilderSeedHit" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" ),
      iterativeTSG = cms.PSet( 
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "unused" ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet( 
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet( 
            pf3_V12 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V13 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V11 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V14 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V15 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V33 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            pf3_V44 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            pf3_V22 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V23 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V45 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V55 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V34 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V35 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V25 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V24 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" ),
      iterativeTSG = cms.PSet( 
        firstTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet( 
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 0 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 ),
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
            ),
            SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet( 
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet( 
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet( 
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
              useOnDemandTracker = cms.untracked.int32( 0 )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" )
        ),
        secondTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            SeedingLayers = cms.string( "hltESPPixelLayerPairs" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet( 
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      Eta_min = cms.double( 0.1 ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.0010 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3TkTracksFromL2IOHit','hltL3TkTracksFromL2OIHit','hltL3TkTracksFromL2OIState' )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltBSoftMuonMu5L3 = cms.EDFilter( "RecoTrackRefSelector",
    src = cms.InputTag( "hltL3Muons" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    algorithm = cms.vstring(  ),
    maxChi2 = cms.double( 10000.0 ),
    tip = cms.double( 120.0 ),
    quality = cms.vstring(  ),
    minRapidity = cms.double( -5.0 ),
    lip = cms.double( 300.0 ),
    ptMin = cms.double( 5.0 ),
    maxRapidity = cms.double( 5.0 ),
    min3DHit = cms.int32( 0 ),
    minHit = cms.int32( 0 )
)
process.hltBSoftMuonDiJet20L1FastJetMu5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltBSoftMuonMu5L3" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet20L1FastJetMu5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet20L1FastJetMu5SelL3TagInfos' )
)
process.hltBSoftMuonDiJet20L1FastJetMu5L3FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetMu5SelL3BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet20L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreBTagMuDiJet40Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBDiJet40L1FastJetCentral = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
process.hltBSoftMuonGetJetsFromDiJet40L1FastJet = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltBDiJet40L1FastJetCentral" )
)
process.hltSelector4JetsDiJet40L1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltBSoftMuonGetJetsFromDiJet40L1FastJet" )
)
process.hltBSoftMuonDiJet40L1FastJetL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelector4JetsDiJet40L1FastJet" ),
    etMin = cms.double( 40.0 )
)
process.hltBSoftMuonDiJet40L1FastJetL25TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltL2Muons" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet40L1FastJetL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet40L1FastJetL25TagInfos' )
)
process.hltBSoftMuonDiJet40L1FastJetL25FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( False ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetL25BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltBSoftMuonDiJet40L1FastJetMu5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltBSoftMuonMu5L3" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet40L1FastJetMu5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet40L1FastJetMu5SelL3TagInfos' )
)
process.hltBSoftMuonDiJet40L1FastJetMu5L3FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetMu5SelL3BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet40L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltL1sL1Mu3JetC52WdEtaPhi2 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_JetC52_WdEtaPhi2" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreBTagMuDiJet70Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBDiJet70L1FastJetCentral = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 70.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
process.hltBSoftMuonGetJetsFromDiJet70L1FastJet = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltBDiJet70L1FastJetCentral" )
)
process.hltSelector4JetsDiJet70L1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltBSoftMuonGetJetsFromDiJet70L1FastJet" )
)
process.hltBSoftMuonDiJet70L1FastJetL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelector4JetsDiJet70L1FastJet" ),
    etMin = cms.double( 70.0 )
)
process.hltBSoftMuonDiJet70L1FastJetL25TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltL2Muons" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet70L1FastJetL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet70L1FastJetL25TagInfos' )
)
process.hltBSoftMuonDiJet70L1FastJetL25FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( False ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetL25BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltBSoftMuonDiJet70L1FastJetMu5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltBSoftMuonMu5L3" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet70L1FastJetMu5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet70L1FastJetMu5SelL3TagInfos' )
)
process.hltBSoftMuonDiJet70L1FastJetMu5L3FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetMu5SelL3BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet70L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreBTagMuDiJet110Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBDiJet110L1FastJetCentral = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 110.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
process.hltBSoftMuonGetJetsFromDiJet110L1FastJet = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltBDiJet110L1FastJetCentral" )
)
process.hltSelector4JetsDiJet110L1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltBSoftMuonGetJetsFromDiJet110L1FastJet" )
)
process.hltBSoftMuonDiJet110L1FastJetL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelector4JetsDiJet110L1FastJet" ),
    etMin = cms.double( 110.0 )
)
process.hltBSoftMuonDiJet110L1FastJetL25TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltL2Muons" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet110L1FastJetL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet110L1FastJetL25TagInfos' )
)
process.hltBSoftMuonDiJet110L1FastJetL25FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( False ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetL25BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltBSoftMuonDiJet110L1FastJetMu5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltBSoftMuonMu5L3" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonDiJet110L1FastJetMu5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonDiJet110L1FastJetMu5SelL3TagInfos' )
)
process.hltBSoftMuonDiJet110L1FastJetMu5L3FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetMu5SelL3BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonDiJet110L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltL1sL1SingleJet128 = cms.EDFilter( "HLTLevel1GTSeed",
    saveTags = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet128" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreBTagMuJet300Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBJet300L1FastJetCentral = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 300.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
process.hltBSoftMuonGetJetsFromJet300L1FastJet = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 86 ),
    HLTObject = cms.InputTag( "hltBJet300L1FastJetCentral" )
)
process.hltSelector4JetsJet300L1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltBSoftMuonGetJetsFromJet300L1FastJet" )
)
process.hltBSoftMuonJet300L1FastJetL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelector4JetsJet300L1FastJet" ),
    etMin = cms.double( 300.0 )
)
process.hltBSoftMuonJet300L1FastJetL25TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltL2Muons" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonJet300L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonJet300L1FastJetL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonJet300L1FastJetL25TagInfos' )
)
process.hltBSoftMuonJet300L1FastJetL25FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( False ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonJet300L1FastJetL25BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonJet300L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltBSoftMuonJet300L1FastJetMu5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    muonSelection = cms.uint32( 0 ),
    leptons = cms.InputTag( "hltBSoftMuonMu5L3" ),
    primaryVertex = cms.InputTag( "nominal" ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    jets = cms.InputTag( "hltBSoftMuonJet300L1FastJetL25Jets" ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 )
)
process.hltBSoftMuonJet300L1FastJetMu5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonJet300L1FastJetMu5SelL3TagInfos' )
)
process.hltBSoftMuonJet300L1FastJetMu5L3FilterByDR = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltBSoftMuonJet300L1FastJetMu5SelL3BJetTagsByDR" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltBSoftMuonJet300L1FastJetL25Jets" ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTRecoJetSequenceAK5L1FastJetCorrected = cms.Sequence( process.HLTDoCaloSequence + process.hltKT6CaloJets + process.hltAntiKT5CaloJets + process.hltCaloJetIDPassed + process.hltCaloJetL1FastJetCorrected )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTMuonLocalRecoSequence + process.hltL2OfflineMuonSeeds + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTBTagMuDiJet20L1FastJetSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltBSoftMuonGetJetsFromDiJet20L1FastJet + process.hltSelector4JetsDiJet20L1FastJet + process.hltBSoftMuonDiJet20L1FastJetL25Jets + process.hltBSoftMuonDiJet20L1FastJetL25TagInfos + process.hltBSoftMuonDiJet20L1FastJetL25BJetTagsByDR )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajSeedOIState + process.hltL3TrackCandidateFromL2OIState + process.hltL3TkTracksFromL2OIState + process.hltL3MuonsOIState + process.hltL3TrajSeedOIHit + process.hltL3TrackCandidateFromL2OIHit + process.hltL3TkTracksFromL2OIHit + process.hltL3MuonsOIHit + process.hltL3TkFromL2OICombination + process.hltL3TrajSeedIOHit + process.hltL3TrackCandidateFromL2IOHit + process.hltL3TkTracksFromL2IOHit + process.hltL3MuonsIOHit + process.hltL3TrajectorySeed + process.hltL3TrackCandidateFromL2 )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence + process.hltL3TkTracksFromL2 + process.hltL3MuonsLinksCombination + process.hltL3Muons )
process.HLTBTagMuDiJet20L1FastJetMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonMu5L3 + process.hltBSoftMuonDiJet20L1FastJetMu5SelL3TagInfos + process.hltBSoftMuonDiJet20L1FastJetMu5SelL3BJetTagsByDR )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTBTagMuDiJet40L1FastJetSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltBSoftMuonGetJetsFromDiJet40L1FastJet + process.hltSelector4JetsDiJet40L1FastJet + process.hltBSoftMuonDiJet40L1FastJetL25Jets + process.hltBSoftMuonDiJet40L1FastJetL25TagInfos + process.hltBSoftMuonDiJet40L1FastJetL25BJetTagsByDR )
process.HLTBTagMuDiJet40L1FastJetMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonMu5L3 + process.hltBSoftMuonDiJet40L1FastJetMu5SelL3TagInfos + process.hltBSoftMuonDiJet40L1FastJetMu5SelL3BJetTagsByDR )
process.HLTBTagMuDiJet70L1FastJetSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltBSoftMuonGetJetsFromDiJet70L1FastJet + process.hltSelector4JetsDiJet70L1FastJet + process.hltBSoftMuonDiJet70L1FastJetL25Jets + process.hltBSoftMuonDiJet70L1FastJetL25TagInfos + process.hltBSoftMuonDiJet70L1FastJetL25BJetTagsByDR )
process.HLTBTagMuDiJet70L1FastJetMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonMu5L3 + process.hltBSoftMuonDiJet70L1FastJetMu5SelL3TagInfos + process.hltBSoftMuonDiJet70L1FastJetMu5SelL3BJetTagsByDR )
process.HLTBTagMuDiJet110L1FastJetSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltBSoftMuonGetJetsFromDiJet110L1FastJet + process.hltSelector4JetsDiJet110L1FastJet + process.hltBSoftMuonDiJet110L1FastJetL25Jets + process.hltBSoftMuonDiJet110L1FastJetL25TagInfos + process.hltBSoftMuonDiJet110L1FastJetL25BJetTagsByDR )
process.HLTBTagMuDiJet110L1FastJetMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonMu5L3 + process.hltBSoftMuonDiJet110L1FastJetMu5SelL3TagInfos + process.hltBSoftMuonDiJet110L1FastJetMu5SelL3BJetTagsByDR )
process.HLTBTagMuJet300L1FastJetSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltBSoftMuonGetJetsFromJet300L1FastJet + process.hltSelector4JetsJet300L1FastJet + process.hltBSoftMuonJet300L1FastJetL25Jets + process.hltBSoftMuonJet300L1FastJetL25TagInfos + process.hltBSoftMuonJet300L1FastJetL25BJetTagsByDR )
process.HLTBTagMuJet300L1FastJetMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonMu5L3 + process.hltBSoftMuonJet300L1FastJetMu5SelL3TagInfos + process.hltBSoftMuonJet300L1FastJetMu5SelL3BJetTagsByDR )

process.HLT_BTagMu_DiJet20_Mu5_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3JetC16WdEtaPhi2 + process.hltPreBTagMuDiJet20Mu5 + process.HLTRecoJetSequenceAK5L1FastJetCorrected + process.hltBDiJet20L1FastJetCentral + process.HLTBTagMuDiJet20L1FastJetSequenceL25 + process.hltBSoftMuonDiJet20L1FastJetL25FilterByDR + process.HLTBTagMuDiJet20L1FastJetMu5SelSequenceL3 + process.hltBSoftMuonDiJet20L1FastJetMu5L3FilterByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet40_Mu5_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3JetC16WdEtaPhi2 + process.hltPreBTagMuDiJet40Mu5 + process.HLTRecoJetSequenceAK5L1FastJetCorrected + process.hltBDiJet40L1FastJetCentral + process.HLTBTagMuDiJet40L1FastJetSequenceL25 + process.hltBSoftMuonDiJet40L1FastJetL25FilterByDR + process.HLTBTagMuDiJet40L1FastJetMu5SelSequenceL3 + process.hltBSoftMuonDiJet40L1FastJetMu5L3FilterByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet70_Mu5_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3JetC52WdEtaPhi2 + process.hltPreBTagMuDiJet70Mu5 + process.HLTRecoJetSequenceAK5L1FastJetCorrected + process.hltBDiJet70L1FastJetCentral + process.HLTBTagMuDiJet70L1FastJetSequenceL25 + process.hltBSoftMuonDiJet70L1FastJetL25FilterByDR + process.HLTBTagMuDiJet70L1FastJetMu5SelSequenceL3 + process.hltBSoftMuonDiJet70L1FastJetMu5L3FilterByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet110_Mu5_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3JetC52WdEtaPhi2 + process.hltPreBTagMuDiJet110Mu5 + process.HLTRecoJetSequenceAK5L1FastJetCorrected + process.hltBDiJet110L1FastJetCentral + process.HLTBTagMuDiJet110L1FastJetSequenceL25 + process.hltBSoftMuonDiJet110L1FastJetL25FilterByDR + process.HLTBTagMuDiJet110L1FastJetMu5SelSequenceL3 + process.hltBSoftMuonDiJet110L1FastJetMu5L3FilterByDR + process.HLTEndSequence )
process.HLT_BTagMu_Jet300_Mu5_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet128 + process.hltPreBTagMuJet300Mu5 + process.HLTRecoJetSequenceAK5L1FastJetCorrected + process.hltBJet300L1FastJetCentral + process.HLTBTagMuJet300L1FastJetSequenceL25 + process.hltBSoftMuonJet300L1FastJetL25FilterByDR + process.HLTBTagMuJet300L1FastJetMu5SelSequenceL3 + process.hltBSoftMuonJet300L1FastJetMu5L3FilterByDR + process.HLTEndSequence )


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:RelVal_Raw_GRun_DATA.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# Enable HF Noise filters in GRun menu
if 'hltHfreco' in process.__dict__:
    process.hltHfreco.setNoiseFlags = cms.bool( True )

# CMSSW version specific customizations
import os
cmsswVersion = os.environ['CMSSW_VERSION']

# customization for CMSSW_5_2_X
if cmsswVersion.startswith('CMSSW_5_2_'):

    # force the use of the correct calo jet energy corrections
    if 'hltESPL1FastJetCorrectionESProducer' in process.__dict__:
        process.hltESPL1FastJetCorrectionESProducer.algorithm  = "AK5CaloHLT"

    if 'hltESPL2RelativeCorrectionESProducer' in process.__dict__:
        process.hltESPL2RelativeCorrectionESProducer.algorithm = "AK5CaloHLT"

    if 'hltESPL3AbsoluteCorrectionESProducer' in process.__dict__:
        process.hltESPL3AbsoluteCorrectionESProducer.algorithm = "AK5CaloHLT"


# customization for CMSSW_5_3_X
if cmsswVersion.startswith('CMSSW_5_3_'):

    # do not override the calo jet energy corrections in 5.3.x for consistency with the current MC samples
    pass


# customization for CMSSW_6_1_X and 6_2_X
if cmsswVersion.startswith('CMSSW_6_1_') or cmsswVersion.startswith('CMSSW_6_2_'):

    # force the use of the correct calo jet energy corrections
    if 'hltESPL1FastJetCorrectionESProducer' in process.__dict__:
        process.hltESPL1FastJetCorrectionESProducer.algorithm  = "AK5CaloHLT"

    if 'hltESPL2RelativeCorrectionESProducer' in process.__dict__:
        process.hltESPL2RelativeCorrectionESProducer.algorithm = "AK5CaloHLT"

    if 'hltESPL3AbsoluteCorrectionESProducer' in process.__dict__:
        process.hltESPL3AbsoluteCorrectionESProducer.algorithm = "AK5CaloHLT"

    # adapt the HLT menu to the "prototype for Event Interpretation" development
    if 'hltPFPileUp' in process.__dict__:
        # define new PFCandidateFwdPtrProducer module
        process.hltParticleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
            src = cms.InputTag('hltParticleFlow')
        )
        # add the new module before the hltPFPileUp module
        _sequence = None
        for _sequence in [ _sequence for _sequence in process.__dict__.itervalues() if isinstance(_sequence, cms._ModuleSequenceType)]:
            try:
                _sequence.insert( _sequence.index(process.hltPFPileUp), process.hltParticleFlowPtrs )
            except ValueError:
                pass
        # reconfigure hltPFPileUp and hltPFNoPileUp to use the new module
        process.hltPFPileUp.PFCandidates       = cms.InputTag( "hltParticleFlowPtrs" )
        process.hltPFNoPileUp.bottomCollection = cms.InputTag( "hltParticleFlowPtrs" )


# customization for CMSSW_6_2_X only
if cmsswVersion.startswith('CMSSW_6_2_'):
    # /Geometry/TrackerNumberingBuilder/trackerTopologyConstants_cfi.py
    process.trackerTopologyConstants = cms.ESProducer('TrackerTopologyEP',
      pxb_layerStartBit = cms.uint32(16),
      pxb_ladderStartBit = cms.uint32(8),
      pxb_moduleStartBit = cms.uint32(2),
      pxb_layerMask = cms.uint32(15),
      pxb_ladderMask = cms.uint32(255),
      pxb_moduleMask = cms.uint32(63),
      pxf_sideStartBit = cms.uint32(23),
      pxf_diskStartBit = cms.uint32(16),
      pxf_bladeStartBit = cms.uint32(10),
      pxf_panelStartBit = cms.uint32(8),
      pxf_moduleStartBit = cms.uint32(2),
      pxf_sideMask = cms.uint32(3),
      pxf_diskMask = cms.uint32(15),
      pxf_bladeMask = cms.uint32(63),
      pxf_panelMask = cms.uint32(3),
      pxf_moduleMask = cms.uint32(63),
      tec_sideStartBit = cms.uint32(18),
      tec_wheelStartBit = cms.uint32(14),
      tec_petal_fw_bwStartBit = cms.uint32(12),
      tec_petalStartBit = cms.uint32(8),
      tec_ringStartBit = cms.uint32(5),
      tec_moduleStartBit = cms.uint32(2),
      tec_sterStartBit = cms.uint32(0),
      tec_sideMask = cms.uint32(3),
      tec_wheelMask = cms.uint32(15),
      tec_petal_fw_bwMask = cms.uint32(3),
      tec_petalMask = cms.uint32(15),
      tec_ringMask = cms.uint32(7),
      tec_moduleMask = cms.uint32(7),
      tec_sterMask = cms.uint32(3),
      tib_layerStartBit = cms.uint32(14),
      tib_str_fw_bwStartBit = cms.uint32(12),
      tib_str_int_extStartBit = cms.uint32(10),
      tib_strStartBit = cms.uint32(4),
      tib_moduleStartBit = cms.uint32(2),
      tib_sterStartBit = cms.uint32(0),
      tib_layerMask = cms.uint32(7),
      tib_str_fw_bwMask = cms.uint32(3),
      tib_str_int_extMask = cms.uint32(3),
      tib_strMask = cms.uint32(63),
      tib_moduleMask = cms.uint32(3),
      tib_sterMask = cms.uint32(3),
      tid_sideStartBit = cms.uint32(13),
      tid_wheelStartBit = cms.uint32(11),
      tid_ringStartBit = cms.uint32(9),
      tid_module_fw_bwStartBit = cms.uint32(7),
      tid_moduleStartBit = cms.uint32(2),
      tid_sterStartBit = cms.uint32(0),
      tid_sideMask = cms.uint32(3),
      tid_wheelMask = cms.uint32(3),
      tid_ringMask = cms.uint32(3),
      tid_module_fw_bwMask = cms.uint32(3),
      tid_moduleMask = cms.uint32(31),
      tid_sterMask = cms.uint32(3),
      tob_layerStartBit = cms.uint32(14),
      tob_rod_fw_bwStartBit = cms.uint32(12),
      tob_rodStartBit = cms.uint32(5),
      tob_moduleStartBit = cms.uint32(2),
      tob_sterStartBit = cms.uint32(0),
      tob_layerMask = cms.uint32(7),
      tob_rod_fw_bwMask = cms.uint32(3),
      tob_rodMask = cms.uint32(127),
      tob_moduleMask = cms.uint32(7),
      tob_sterMask = cms.uint32(3),
      appendToDataLabel = cms.string('')
    )


# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.TriggerResultsTag = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.TriggerResultsTag        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.TriggerResultsTag       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.TriggerResultsTag  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.TriggerResultsTag         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:hltonline')

# customize the L1 emulator to run customiseL1GtEmulatorFromRaw with HLT to switchToSimGtDigis
process.load( 'Configuration.StandardSequences.RawToDigi_Data_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
process = L1Trigger.Configuration.L1Trigger_custom.customiseL1GtEmulatorFromRaw( process )
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )

# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimGtDigis( process )

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

