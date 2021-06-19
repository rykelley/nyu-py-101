# 6.25:  Print the date value from each dict in 'data'.  Hint:
# determine the chained subscript that reaches the 'data'
# list, and assign to a variable.  Then loop through that
# variable as you would any list of dicts.

import runreport

json_struct = {

  'json_rpc': '1.1',

  'result': {

    'meta': {
      'last_refresh': '20201019',
      'size': 2395 },

    'data': [
      { 'date': '19260701', 'MktRF': 0.09, 'SMB': -0.22,
        'HML': -0.30, 'RF': 0.009 },

      { 'date': '19260702', 'MktRF': 0.44, 'SMB': -0.35,
        'HML': -0.08, 'RF': 0.009 },

      { 'date': '19260706', 'MktRF': 0.17, 'SMB': 0.26,
        'HML': -0.37, 'RF': 0.009 }
    ],

  },

}

# Expected Output:

# 19260701
# 19260702
# 19260706

