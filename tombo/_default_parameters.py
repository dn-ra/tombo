from __future__ import unicode_literals

###############################
##### Model Name Defaults #####
###############################

# default model names
STANDARD_MODELS = {
    'DNA':'tombo.DNA.model',
    'RNA':'tombo.RNA.180mV.model',
}
ALTERNATE_MODELS = {
    'DNA_5mC':'tombo.DNA.5mC.model',
    'DNA_6mA':'tombo.DNA.6mA.model',
    'RNA_5mC':'tombo.RNA.5mC.model',
}


################################
##### Re-squiggle Defaults #####
################################

# table containing default segmentation parameters for different sample types
#   1) running neighboring window width for segmentation scoring
#   2) minimum observations per genomic base
#   3) mean number of observations per event during segmentation
SEG_PARAMS_TABLE = {
    'RNA':(12, 6, 12),
    'DNA':(5, 3, 5),
}

# table containing default signal to sequence assignment parameters
# for different sample types
#   1) expected value for matching event to sequence
#   2) penalty for skipped sequence position
#   3) adaptive bandwidth
#   4) save adaptive bandwidth (if first bw fails)
#   5) z-score winsorizing threshold
ALGN_PARAMS_TABLE = {
    'RNA':(4, 8, 400, 1200, 5.0),
    'DNA':(4.2, 4.2, 250, 1200, 5.0),
}

# default thresholds for filtering out reads that don't match well to
# expected signal levels
SIG_MATCH_THRESH = {
    'RNA':1.3,
    'DNA':1.1,
}

# factor of extra raw signal above minimum to add around skipped bases for
# raw signal segment detection
EXTRA_SIG_FACTOR = 1.1

MASK_FILL_Z_SCORE = -10
MASK_BASES = 50

START_BANDWIDTH = 5000
START_SEQ_WINDOW = 250
BAND_BOUNDARY_THRESH = 5

DEL_FIX_WINDOW = 2
MAX_DEL_FIX_WINDOW = 8
MAX_RAW_CPTS = 200
MIN_EVENT_TO_SEQ_RATIO = 1.1


############################
##### Testing Defaults #####
############################

LLR_THRESH = {
    'DNA':(-1.5, 2.5),
    'RNA':(-2.5, 2.5),
}
SAMP_COMP_THRESH = {
    'DNA':(0.15, 0.5),
    'RNA':(0.05, 0.4),
}
DE_NOVO_THRESH = {
    'DNA':(0.15, 0.5),
    'RNA':(0.05, 0.4),
}

# outlier corrected likelihood ratio parameters
#     visualize with scripts test_scaled_log_likelihood.R
#    scale_factor - sets the spread of the value (2 makes peaks equal the normal
#        density centers, but this is very sharp near the boundary between the
#        reference and alternative densities
#    density_height_factor - globally scales the height of the scores. Set to
#        approximately match log likelihood scale.
#    density_height_power - scales the density height proportional to the
#        difference between the reference and alternate means. 0.5 makes all
#        densities peak at the same value. Recommend values between 0 and 0.5
#        so that more divergent reference and alternate densities contrbute more
#        to the score.
OCLLHR_SCALE = 4.0
OCLLHR_HEIGHT = 1.0
OCLLHR_POWER = 0.2


#####################################
##### Model Estimation Defaults #####
#####################################

ALT_EST_BATCH = 1000
MAX_KMER_OBS = 10000
MIN_KMER_OBS_TO_EST = 50
KERNEL_DENSITY_RANGE = (-5,5)
ALT_EST_PCTL = 5


##########################
##### Misc. Defaults #####
##########################

SMALLEST_PVAL = 1e-50

# got quantiles from analysis of stability after shift-only normalization
ROBUST_QUANTS = (46.5, 53.5)

# minimum standard deviation for a genomic position when estimating spread
# from a sample
MIN_POSITION_SD = 0.01

# number of points at which to estimate the k-mer siganl densities
NUM_DENS_POINTS = 500

# number of reads to estimate global scale parameter
NUM_READS_FOR_SCALE = 1000
# sequence-based scaling thresholds for iterative re-squiggle
SHIFT_CHANGE_THRESH = 0.1
SCALE_CHANGE_THRESH = 0.1
MAX_SCALING_ITERS=3

# number of reads to adjust model
NUM_READS_TO_ADJUST_MODEL = 5000

# TODO check the number of points where this stabilizes
# Note that all pairwise slopes for this number of points must be computed
MAX_POINTS_FOR_THEIL_SEN = 1000

# number of points to plot in the ROC curve plotting command
ROC_PLOT_POINTS = 1000

# for mean q-score computation
PHRED_BASE= 33

# central position from a nanopolish reference (not 100% sure this is correct)
NANOPOLISH_CENTRAL_POS = 2

# default values for dampened fraction computations
COV_DAMP_COUNTS = [2, 0.5]
