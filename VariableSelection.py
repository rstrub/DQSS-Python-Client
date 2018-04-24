
DQSS_URL_LOCATION = "http://airsl2.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?"

best=(
    "COVMRLevStd",
  )
  
good=(
  "CldFrcStd",
  "CldFrcTot",
  "TCldTop",
  "olr3x3",
  "olr",
  "clrolr",
  "CH4VMRLevStd",
  )

noscreening=(
  "CO_total_column",
  "PCldTop",
  )

donotinclude = (
  "CH4_total_column",
  "O3VMRLevStd",
  "O3VMRStd",
  "totO3Std",
  "GP_Surface",
  "EmisMWStd",
  "GP_Height",
  "GP_Tropopause",
  "GP_Height_MWOnly",
  "sfcTbMWStd",
  "emisIRStd",
  "TSurfStd",
  "TAirStd",
  "TAirMWOnlyStd",
  "TSurfAir",
  "H2OMMRStd",
  "H2OMMRLevStd",
  "H2OMMRSat",
  "RelHumSurf",
  "totCldH2OStd",
  "totH2OMWOnlyStd",
  "totH2OStd",
  "RelHum",
  "RelHumSurf_liquid",
  "RelHum_liquid",
  "H2OMMRSatSurf_liquid",
  "H2OMMRSatLevStd_liquid",
  "H2OMMRSatSurf",
  "H2OMMRSat_liquid", 
  "H2OMMRSurf",
  "H2OMMRSatLevStd")
  
  
  
ancillary_include = (
  'AMSU_Chans_Resid', 
  'CC1_Resid',
  )
  
ancillary_donotinclude = (
  'CC1_noise_eff_amp_factor', 
  'CC_noise_eff_amp_factor', 
  'CCfinal_Noise_Amp', 
  'CCfinal_Resid', 
  'Cloud_Resid_Ratio', 
  'EmisMWStd', 
  'EmisMWStdErr', 
  'GP_Height', 
  'GP_Height_MWOnly', 
  'GP_Surface', 
  'GP_Tropopause', 
  'Initial_CC_score', 
  'MW_ret_used', 
  'PTropopause', 
  'Qual_Guess_PSurf', 
  'RetQAFlag', 
  'Startup', 
  'Surf_Resid_Ratio', 
  'TSurfdiff_IR_4CC1', 
  'TSurfdiff_IR_4CC2', 
  'T_Tropopause', 
  'Tdiff_IR_4CC1', 
  'Tdiff_IR_MW_ret', 
  'Temp_Resid_Ratio', 
  'TotCld_4_CCfinal', 
  'Water_Resid_Ratio', 
  'all_spots_avg', 
  'demgeoqa', 
  'dust_flag', 
  'ftptgeoqa', 
  'glintgeoqa', 
  'glintlat', 
  'glintlon', 
  'landFrac', 
  'landFrac_err', 
  'moongeoqa', 
  'nadirTAI', 
  'numHingeSurf', 
  'num_clear_spectral_indicator', 
  'retrieval_type', 
  'sat_lat', 
  'sat_lon', 
  'satazi', 
  'satgeoqa', 
  'satheight', 
  'satpitch', 
  'satroll', 
  'satyaw', 
  'satzen', 
  'scan_node_type', 
  'sfcTbMWStd', 
  'solazi', 
  'solzen', 
  'spectral_clear_indicator', 
  'sun_glint_distance', 
  'topog', 
  'topog_err', 
  'zengeoqa')
