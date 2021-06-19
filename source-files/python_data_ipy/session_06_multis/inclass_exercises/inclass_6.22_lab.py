# 6.22:  Loop through and print the date and MktRF value from
# each "inner" dict.

import runreport

date_values = {
    '19260701':   { 'MktRF':  0.09,
                    'SMB':   -0.22,
                    'HML':   -0.30,
                    'RF':    0.009 },
    '19260702':   { 'MktRF':  0.44,
                    'SMB':   -0.35,
                    'HML':   -0.08,
                    'RF':    0.009 },
}

# Expected Output:

# 19260701:  0.09
# 19250702:  0.44

