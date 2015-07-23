"""
Module that holds all facet operations

The facet calibration steps are divided into operations on the basis of whether
or not they can be run in parallel or in series.

Classes
-------
FacetAdd : Operation
    Adds facet sources to data. Must be run in series as writes are made to
    original datasets
FacetSelfcal : Operation
    Runs the selfcal and imaging of a facet. May be run in parallel
FacetSub : Operation
    Subtracts all facet sources from data. Must be run in series as writes are
    made to original datasets
FacetAddFinal : Operation
    Adds all facet sources from final model. Must be run in series as writes are
    made to original datasets
FacetImageFinal : Operation
    Images the entire facet. May be run in parallel

"""
import os
import ast
from factor.lib.operation import Operation
from lofarpipe.support.data_map import DataMap


class FacetAdd(Operation):
    """
    Operation to add calibrator source to data
    """
    def __init__(self, parset, bands, direction):
        super(FacetAdd, self).__init__(parset, bands, direction,
            name='FacetAdd')

        # Define extra parameters needed for this operation (beyond those
        # defined in the master Operation class and as attributes of the
        # direction object)
        skymodels = [band.skymodel_dirindep for band in self.bands]
        if self.direction.use_new_sub_data:
            add_all_parset = 'facet_dirindep_add_all_new.parset'
            add_cal_parset = 'facet_dirindep_add_cal_new.parset'
        else:
            add_all_parset = 'facet_dirindep_add_all.parset'
            add_cal_parset = 'facet_dirindep_add_cal.parset'
        self.parms_dict.update({'input_dir': parset['dir_ms'],
                                'add_all_parset': add_all_parset,
                                'add_cal_parset': add_cal_parset,
                                'dir_indep_parmdb_name': parset['parmdb_name'],
                                'skymodels': skymodels})


    def finalize(self):
        """
        Finalize this operation
        """
        # Add output datamaps to direction object
        self.direction.input_bands_datamap = os.path.join(self.mapfile_dir,
            'input_bands.datamap')
        self.direction.shifted_all_bands_datamap = os.path.join(self.mapfile_dir,
            'shifted_all_bands.datamap')
        self.direction.shifted_cal_bands_datamap = os.path.join(self.mapfile_dir,
            'shifted_cal_bands.datamap')
        self.direction.shifted_empty_bands_datamap = os.path.join(self.mapfile_dir,
            'shifted_empty_bands.datamap')
        self.direction.dir_indep_parmdbs_datamap = os.path.join(self.mapfile_dir,
            'dir_indep_instrument_parmdbs.datamap')
        self.direction.dir_indep_skymodels_datamap = os.path.join(self.mapfile_dir,
            'full_skymodels.datamap')
        self.direction.dir_indep_facet_skymodels_datamap = os.path.join(self.mapfile_dir,
            'facet_skymodels.datamap')
        self.direction.cleanup_mapfiles.extend([self.direction.shifted_all_bands_datamap,
            self.direction.shifted_cal_bands_datamap,
            self.direction.shifted_empty_bands_datamap])


class FacetSelfcal(Operation):
    """
    Operation to selfcal one or more directions
    """
    def __init__(self, parset, direction):
        super(FacetSelfcal, self).__init__(parset, None, direction,
            name='FacetSelfcal')

        # Set the pipeline parset to use
        if self.parset['facet_imager'].lower() == 'casa':
            # Set parset template to casa parset
            self.pipeline_parset_template = '{0}_casa_pipeline.parset'.format(self.name)
        else:
            # Set parset template to wsclean parset
            self.pipeline_parset_template = '{0}_pipeline.parset'.format(self.name)

        # Define extra parameters needed for this operation (beyond those
        # defined in the master Operation class and as attributes of the
        # direction object)
        if self.direction.nchannels > 1:
            nterms = 2
            casa_suffix = '.tt0'
            wsclean_suffix = '-MFS-image.fits'
        else:
            nterms = 1
            casa_suffix = None
            wsclean_suffix = '-image.fits'
        self.parms_dict.update({'casa_suffix': casa_suffix,
                                'wsclean_suffix': wsclean_suffix,
                                'nterms': nterms})


    def finalize(self):
        """
        Finalize this operation
        """
        # Add output datamap to direction object
        self.direction.dir_dep_parmdb_datamap = os.path.join(self.mapfile_dir,
            'dir_dep_parmdb.datamap')
        self.direction.facet_image_mapfile = os.path.join(self.mapfile_dir,
            'final_image.datamap')
        self.direction.facet_model_mapfile = os.path.join(self.mapfile_dir,
            'final_model_rootnames.datamap')
        self.verify_subtract_OK_mapfile = os.path.join(self.mapfile_dir,
            'verify_subtract_OK.datamap')
        self.direction.cleanup_mapfiles.extend([os.path.join(self.mapfile_dir,
            'chunk_files.datamap'), os.path.join(self.mapfile_dir,
            'concat1_input.datamap'), os.path.join(self.mapfile_dir,
            'concat2_input.datamap'), os.path.join(self.mapfile_dir,
            'concat3_input.datamap'), os.path.join(self.mapfile_dir,
            'concat4_input.datamap')])

        # Store results of verify_subtract check
        if os.path.exists(self.verify_subtract_OK_mapfile):
            ok_datamap = DataMap.load(self.verify_subtract_OK_mapfile)
            ok_flags = [ast.literal_eval(item.file) for item in ok_datamap]
            if all(ok_flags):
                self.direction.selfcal_ok = True
            else:
                self.direction.selfcal_ok = False


class FacetSub(Operation):
    """
    Operation to mosiac facet images
    """
    def __init__(self, parset, direction):
        super(FacetSub, self).__init__(parset, None, direction,
            name='FacetSub')

        # Set the pipeline parset to use
        if self.direction.skip_add_subtract:
            self.pipeline_parset_template = '{0}_single_pipeline.parset'.format(self.name)
        else:
            self.pipeline_parset_template = '{0}_pipeline.parset'.format(self.name)


    def finalize(self):
        """
        Finalize this operation
        """
        self.direction.facet_model_data_mapfile = os.path.join(self.mapfile_dir,
            'shifted_to_field_models.datamap')


class FacetAddFinal(Operation):
    """
    Operation to add all sources in the facet in preparation for final imaging
    """
    def __init__(self, parset, bands, direction):
        super(FacetAddFinal, self).__init__(parset, bands, direction,
            name='FacetAddFinal')

        # Set the pipeline parset to use
        if not self.direction.selfcal_ok:
            # Set parset template to sky-model parset
            self.pipeline_parset_template = '{0}_cc_skymodel_pipeline.parset'.format(self.name)
        else:
            # Set parset template to facet model-image parset
            self.pipeline_parset_template = '{0}_model_image_pipeline.parset'.format(self.name)

        # Define extra parameters needed for this operation (beyond those
        # defined in the master Operation class and as attributes of the
        # direction object)
        skymodels = [band.skymodel_dirindep for band in self.bands]
        self.parms_dict.update({'input_dir': parset['dir_ms'],
                                'dir_indep_parmdb_name': parset['parmdb_name'],
                                'skymodels': skymodels})


    def finalize(self):
        """
        Finalize this operation
        """
        # Add output datamaps to direction object
        self.direction.shifted_all_final_bands_datamap = os.path.join(self.mapfile_dir,
            'shifted_all_final_bands.datamap')
        self.direction.cleanup_mapfiles.extend([self.direction.shifted_all_final_bands_datamap])



class FacetImageFinal(Operation):
    """
    Operation to make final facet image
    """
    def __init__(self, parset, direction):
        super(FacetImageFinal, self).__init__(parset, None, direction,
            name='FacetImageFinal')

        # Set the pipeline parset to use
        if self.parset['facet_imager'].lower() == 'casa':
            # Set parset template to casa parset
            self.pipeline_parset_template = '{0}_casa_pipeline.parset'.format(self.name)
        else:
            # Set parset template to wsclean parset
            self.pipeline_parset_template = '{0}_pipeline.parset'.format(self.name)

        # Define extra parameters needed for this operation (beyond those
        # defined in the master Operation class and as attributes of the
        # direction object)
        if self.direction.nchannels > 1:
            nterms = 2
            casa_suffix = '.tt0'
            wsclean_suffix = '-MFS-image.fits'
        else:
            nterms = 1
            casa_suffix = None
            wsclean_suffix = '-image.fits'
        self.parms_dict.update({'casa_suffix': casa_suffix,
                                'wsclean_suffix': wsclean_suffix,
                                'nterms': nterms})


    def finalize(self):
        """
        Finalize this operation
        """
        # Add output datamaps to direction object
        self.direction.facet_image_mapfile = os.path.join(self.mapfile_dir,
            'final_image.datamap')
        self.direction.facet_model_mapfile = os.path.join(self.mapfile_dir,
            'final_model_rootnames.datamap')
