"""
Module that holds all hard-coded parameters
"""

init_subtract = {
'split' : {'columnname': 'CORRECTED_DATA'}, # outcol is DATA
'imagerh' : {'niter': 10000,
             'imsize': 6250,
             'mscale': False,
             'cell': '7.5arcsec',
             'uvrange': "0.08~7.0klambda",
             'minuv': '80',
             'maxuv': '7000',
             'wplanes': 700,
             'nterms': 1,
             'ncycles': 4,
             'threshold': '0mJy',
             'threshpix': 4,
             'threshisl': 2.5,
             'atrous_do': False,
             'rmsbox': '(60, 20)',
             'adaptive_rmsbox': False,
             'use_rms': False,
             'image_final': False,
             'iterate_threshold': False,
             'n_per_node': 1},
'calibh' : {'incol': 'DATA',
            'outcol1': 'SUBTRACTED_DATA',
            'outcol2': 'CORRECTED_SUBTRACTED_DATA',
            'flags': '--replace-sourcedb'},
'avgl' : {'columnname': 'CORRECTED_SUBTRACTED_DATA', # outcol is DATA
          'freqstep': 5,
          'timestep': 2},
'imagerl' : {'niter' : 5000,
             'imsize': 4800,
             'mscale': False,
             'cell': '25arcsec',
             'uvrange': "0.08~2.0klambda",
             'minuv': '80',
             'maxuv': '2000',
             'wplanes': 700,
             'nterms': 1,
             'ncycles': 2,
             'threshold': '0mJy',
             'threshisl': 5,
             'threshpix': 5,
             'atrous_do': False,
             'rmsbox': '(60, 20)',
             'adaptive_rmsbox': False,
             'use_rms': False,
             'image_final': False,
             'iterate_threshold': False,
             'n_per_node': 1},
'calibl' : {'incol': 'SUBTRACTED_DATA',
            'outcol': 'SUBTRACTED_DATA_ALL',
            'flags': '--replace-sourcedb'},
'merge' : {'matchby': 'name',
           'keep': 'all',
           'radius': 0}
}

facet_add_cal = {
'select' : {},
'add' : {'incol': 'SUBTRACTED_DATA_ALL',
         'outcol': 'FACET_DATA',
         'flags': '--replace-sourcedb'},
'split' : {'columnname': 'FACET_DATA'}, # outcol is DATA
'shift' : {'columnname': 'FACET_DATA'} # outcol is DATA
}

facet_setup = {
'apply' : {'incol': 'DATA',
           'outcol': 'CORRECTED_DATA'},
'avg1' : {'columnname': 'DATA', # outcol is DATA
          'freqstep': 20,
          'timestep': 1},
'avg2' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 20,
          'timestep': 1},
'concat1' : {'columnname': 'DATA'}, # outcol is DATA
'concat2' : {'columnname': 'DATA'}, # outcol is DATA
'copy' : {'incol': 'DATA',
          'outcol': 'CORRECTED_DATA'}
}

facet_selfcal = {
'shift_fft' : {'columnname': 'MODEL_DATA'}, # outcol is DATA
'avg_fft': {'columnname': 'DATA', # outcol is DATA
            'freqstep': 20,
            'timestep': 1},
'copy_fft' : {'incol': 'DATA',
              'outcol': 'MODEL_DATA'}
'avg0' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 1,
          'timestep': 12},
'imager0' : {'niter': 500,
             'imsize': 1024,
             'mscale': True,
             'cell': '1.5arcsec',
             'uvrange': '>80lambda',
             'minuv': '80',
             'maxuv': '1000000',
             'threshpix': 10.0,
             'threshisl': 6.0,
             'atrous_do': True,
             'rmsbox': '(50, 20)',
             'adaptive_rmsbox': False,
             'threshold': '0mJy',
             'nterms' : 2,
             'ncycles' : 3,
             'use_rms' : True,
             'image_final': False,
             'iterate_threshold' : True,
             'n_per_node': 1},
'solve_phaseonly1' : {'incol': 'DATA',
                      'outcol': 'CORRECTED_DATA',
                      'chunksize': 200,
                      'uvrange': 80,
                      'flags': '-f'},
'avg1' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 1,
          'timestep': 12},
'imager1' : {'niter': 500,
             'imsize': 1024,
             'mscale': True,
             'cell': '1.5arcsec',
             'uvrange': '>80lambda',
             'minuv': '80',
             'maxuv': '1000000',
             'threshpix': 10.0,
             'threshisl': 10.0,
             'atrous_do': True,
             'rmsbox': '(60, 20)',
             'adaptive_rmsbox': False,
             'threshold': '0mJy',
             'nterms' : 2,
             'ncycles' : 2,
             'use_rms' : True,
             'image_final': False,
             'iterate_threshold' : True,
             'n_per_node': 1},
'solve_phaseonly2' : {'incol': 'DATA',
                      'outcol': 'CORRECTED_DATA',
                      'chunksize': 200,
                      'uvrange': 80,
                      'flags': '-f'},
'avg2' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 1,
          'timestep': 12},
'imager2' : {'niter': 500,
             'imsize': 1024,
             'mscale': True,
             'cell': '1.5arcsec',
             'uvrange': '>80lambda',
             'minuv': '80',
             'maxuv': '1000000',
             'threshpix': 10.0,
             'threshisl': 10.0,
             'atrous_do': True,
             'rmsbox': '(60, 20)',
             'adaptive_rmsbox': False,
             'threshold': '0mJy',
             'nterms' : 2,
             'ncycles' : 2,
             'use_rms' : True,
             'image_final': False,
             'iterate_threshold' : True,
             'n_per_node': 1},
'solve_phaseamp1_phaseonly': {'incol': 'DATA',
                              'outcol': 'CORRECTED_DATA_PHASE',
                              'uvrange': 80,
                              'flags': '-f'},
'solve_phaseamp1_amponly': {'incol': 'CORRECTED_DATA_PHASE',
                            'uvrange': 80,
                            'flags': '-f'},
'smooth_amp1': {'solset': 'sol000',
                'soltab_amp': 'amplitude000',
                'soltab_phase': 'phase000',
                'smoothing_window': 10},
'apply_amp1' : {'incol': 'CORRECTED_DATA_PHASE',
                'outcol': 'CORRECTED_DATA'},
'avg3' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 1,
          'timestep': 12},
'imager3' : {'niter': 500,
             'imsize': 1024,
             'mscale': True,
             'cell': '1.5arcsec',
             'uvrange': '>80lambda',
             'minuv': '80',
             'maxuv': '1000000',
             'threshpix': 10.0,
             'threshisl': 10.0,
             'atrous_do': True,
             'rmsbox': '(60, 20)',
             'adaptive_rmsbox': False,
             'threshold': '0mJy',
             'nterms' : 2,
             'ncycles' : 2,
             'use_rms' : True,
             'image_final': False,
             'iterate_threshold' : True,
             'n_per_node': 1},
'reset_phases' : {'solset': 'sol000',
                  'soltab': 'phase000'},
'apply_amp2' : {'incol': 'DATA',
                'outcol': 'CORRECTED_DATA_AMP'},
'solve_phaseamp2_phaseonly': {'incol': 'CORRECTED_DATA_AMP',
                              'outcol': 'CORRECTED_DATA_PHASE',
                              'uvrange': 80,
                              'flags': '-f'},
'solve_phaseamp2_amponly': {'incol': 'CORRECTED_DATA_PHASE',
                            'uvrange': 80,
                            'flags': '-f'},
'smooth_amp2': {'solset': 'sol000',
                'soltab_amp': 'amplitude000',
                'soltab_phase': 'phase000',
                'smoothing_window': 10},
'apply_amp3' : {'incol': 'CORRECTED_DATA_PHASE',
                'outcol': 'CORRECTED_DATA'},
'avg4' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
          'freqstep': 1,
          'timestep': 12},
'imager4' : {'niter': 500,
             'imsize': 1024,
             'mscale': True,
             'cell': '1.5arcsec',
             'uvrange': '>80lambda',
             'minuv': '80',
             'maxuv': '1000000',
             'threshpix': 10.0,
             'threshisl': 10.0,
             'atrous_do': True,
             'adaptive_rmsbox': False,
             'rmsbox': '(60, 20)',
             'threshold': '0mJy',
             'nterms' : 2,
             'ncycles' : 2,
             'use_rms' : True,
             'image_final': False,
             'iterate_threshold' : True,
             'n_per_node': 1},
'smooth_amp3': {'solset': 'sol000',
                'soltab_amp': 'amplitude000',
                'soltab_phase': 'phase000',
                'smoothing_window': 1},
}

facet_add_all = {
'select' : {},
'add' : {'incol': 'SUBTRACTED_DATA_ALL',
         'outcol': 'FACET_DATA',
         'flags': '--replace-sourcedb'},
'shift' : {'columnname': 'FACET_DATA'} # outcol is DATA
}

facet_image= {
'apply_dirdep' : {'incol': 'DATA',
                  'outcol': 'CORRECTED_DATA'},
'avg' : {'columnname': 'CORRECTED_DATA', # outcol is DATA
         'freqstep': 5,
         'timestep': 3},
'concat' : {'columnname': 'DATA'}, # outcol is DATA
'imager' : {'niter': 5000,
            'imsize': 1024,
            'mscale': False,
            'cell': '1.5arcsec',
            'uvrange': '>80lambda',
            'minuv': '80',
            'maxuv': '1000000',
            'threshpix': 6.0,
            'threshisl': 3.0,
            'atrous_do': False,
            'rmsbox': 'None',
            'adaptive_rmsbox': True,
            'threshold': '0mJy',
            'nterms': 2,
            'ncycles': 3,
            'use_rms': True,
            'image_final': False,
            'iterate_threshold': True,
            'n_per_node': 1},
'select' : {}
}

facet_sub_all = {
'fft' : {'imsize': 1024,
         'cell': '1.5arcsec',
         'nterms': 2,
         'n_per_node': 1},
'subtract' : {'incol': 'FACET_DATA',
              'outcol': 'SUBTRACTED_DATA_ALL',
              'flags': '--replace-sourcedb'}
}

facet_add_all_final = {
'fft' : {'imsize': 1024,
         'cell': '1.5arcsec',
         'nterms': 2,
         'n_per_node': 1},
'add' : {'incol': 'SUBTRACTED_DATA_ALL',
         'outcol': 'FACET_DATA',
         'flags': '--replace-sourcedb'},
'shift' : {'columnname': 'FACET_DATA'} # outcol is DATA
}

facet_image_final = {
'add_dirdep' : {'incol': 'SUBTRACTED_DATA_ALL',
                'outcol': 'FACET_DATA',
                'flags': '--replace-sourcedb'},
'apply_dirdep' : {'incol': 'FACET_DATA',
                  'outcol': 'CORRECTED_DATA'},
'shift' : {'columnname': 'CORRECTED_DATA'}, # outcol is DATA
'avg' : {'columnname': 'DATA', # outcol is DATA
         'freqstep': 5,
         'timestep': 3},
'imager' : {'niter': 5000,
            'imsize': 1024,
            'mscale': False,
            'cell': '1.5arcsec',
            'uvrange': '>80lambda',
            'minuv': '80',
            'maxuv': '1000000',
            'threshpix': 6.0,
            'threshisl': 3.0,
            'atrous_do': False,
            'rmsbox': 'None',
            'adaptive_rmsbox': True,
            'threshold': '0mJy',
            'nterms': 2,
            'ncycles': 3,
            'use_rms': True,
            'image_final': False,
            'iterate_threshold': True,
            'n_per_node': 1},
}
