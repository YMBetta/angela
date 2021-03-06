#### Notes
- able to train in about 1 hour on laptop
- using a normal distribution (vs uniform) when adding randomness to the Ornstein-Uhlenbeck process helped immensely
- l2 weight_decay of the critic set to 0.0001 vs 0.01 in the paper helped
- batch size of 128 vs 64 helped
- updating gradients every 2 steps reduced wall time but increased episodes to solve
- elu instead of relu for activation functions did not help
- increasing buffer_size did not help


#### DDPG
```
Episode     1   Avg:     0.66   BestAvg:     -inf   σ:     0.00   |   ⍺: 0.5000  Buffer:  20000   Reward:     0.66   Steps:    999
Episode     2   Avg:     0.64   BestAvg:     -inf   σ:     0.02   |   ⍺: 0.5000  Buffer:  40000   Reward:     0.62   Steps:    999
Episode     3   Avg:     0.83   BestAvg:     -inf   σ:     0.27   |   ⍺: 0.5000  Buffer:  60000   Reward:     1.21   Steps:    999
Episode     4   Avg:     0.89   BestAvg:     -inf   σ:     0.26   |   ⍺: 0.5000  Buffer:  80000   Reward:     1.07   Steps:    999
Episode     5   Avg:     0.99   BestAvg:     -inf   σ:     0.30   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.37   Steps:    999
Episode     6   Avg:     1.11   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.74   Steps:    999
Episode     7   Avg:     1.18   BestAvg:     -inf   σ:     0.40   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.56   Steps:    999
Episode     8   Avg:     1.20   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.38   Steps:    999
Episode     9   Avg:     1.22   BestAvg:     -inf   σ:     0.36   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.39   Steps:    999
Episode    10   Avg:     1.28   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.80   Steps:    999
Episode    11   Avg:     1.31   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.60   Steps:    999
Episode    12   Avg:     1.34   BestAvg:     -inf   σ:     0.37   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.69   Steps:    999
Episode    13   Avg:     1.38   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.82   Steps:    999
Episode    14   Avg:     1.39   BestAvg:     -inf   σ:     0.37   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.55   Steps:    999
Episode    15   Avg:     1.43   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.03   Steps:    999
Episode    16   Avg:     1.44   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.62   Steps:    999
Episode    17   Avg:     1.47   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.93   Steps:    999
Episode    18   Avg:     1.50   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.92   Steps:    999
Episode    19   Avg:     1.50   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.55   Steps:    999
Episode    20   Avg:     1.50   BestAvg:     -inf   σ:     0.37   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.48   Steps:    999
Episode    21   Avg:     1.52   BestAvg:     -inf   σ:     0.37   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.83   Steps:    999
Episode    22   Avg:     1.49   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     0.85   Steps:    999
Episode    23   Avg:     1.49   BestAvg:     -inf   σ:     0.38   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.59   Steps:    999
Episode    24   Avg:     1.48   BestAvg:     -inf   σ:     0.37   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.25   Steps:    999
Episode    25   Avg:     1.51   BestAvg:     -inf   σ:     0.39   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.23   Steps:    999
Episode    26   Avg:     1.53   BestAvg:     -inf   σ:     0.40   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.09   Steps:    999
Episode    27   Avg:     1.50   BestAvg:     -inf   σ:     0.42   |   ⍺: 0.5000  Buffer: 100000   Reward:     0.75   Steps:    999
Episode    28   Avg:     1.51   BestAvg:     -inf   σ:     0.42   |   ⍺: 0.5000  Buffer: 100000   Reward:     1.81   Steps:    999
Episode    29   Avg:     1.54   BestAvg:     -inf   σ:     0.42   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.12   Steps:    999
Episode    30   Avg:     1.57   BestAvg:     -inf   σ:     0.45   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.45   Steps:    999
Episode    31   Avg:     1.60   BestAvg:     -inf   σ:     0.49   |   ⍺: 0.5000  Buffer: 100000   Reward:     2.77   Steps:    999
Episode    32   Avg:     1.66   BestAvg:     -inf   σ:     0.58   |   ⍺: 0.5000  Buffer: 100000   Reward:     3.50   Steps:    999
Episode    33   Avg:     1.73   BestAvg:     -inf   σ:     0.70   |   ⍺: 0.5000  Buffer: 100000   Reward:     3.95   Steps:    999
Episode    34   Avg:     1.80   BestAvg:     -inf   σ:     0.78   |   ⍺: 0.5000  Buffer: 100000   Reward:     3.89   Steps:    999
Episode    35   Avg:     1.86   BestAvg:     -inf   σ:     0.85   |   ⍺: 0.5000  Buffer: 100000   Reward:     4.00   Steps:    999
Episode    36   Avg:     1.95   BestAvg:     -inf   σ:     1.00   |   ⍺: 0.5000  Buffer: 100000   Reward:     5.16   Steps:    999
Episode    37   Avg:     2.02   BestAvg:     -inf   σ:     1.06   |   ⍺: 0.5000  Buffer: 100000   Reward:     4.30   Steps:    999
Episode    38   Avg:     2.12   BestAvg:     -inf   σ:     1.23   |   ⍺: 0.5000  Buffer: 100000   Reward:     6.06   Steps:    999
Episode    39   Avg:     2.20   BestAvg:     -inf   σ:     1.30   |   ⍺: 0.5000  Buffer: 100000   Reward:     5.05   Steps:    999
Episode    40   Avg:     2.30   BestAvg:     -inf   σ:     1.43   |   ⍺: 0.5000  Buffer: 100000   Reward:     6.32   Steps:    999
Episode    41   Avg:     2.39   BestAvg:     -inf   σ:     1.52   |   ⍺: 0.5000  Buffer: 100000   Reward:     5.87   Steps:    999
Episode    42   Avg:     2.50   BestAvg:     -inf   σ:     1.67   |   ⍺: 0.5000  Buffer: 100000   Reward:     7.15   Steps:    999
Episode    43   Avg:     2.68   BestAvg:     -inf   σ:     2.03   |   ⍺: 0.5000  Buffer: 100000   Reward:    10.33   Steps:    999
Episode    44   Avg:     2.85   BestAvg:     -inf   σ:     2.27   |   ⍺: 0.5000  Buffer: 100000   Reward:     9.84   Steps:    999
Episode    45   Avg:     3.10   BestAvg:     -inf   σ:     2.80   |   ⍺: 0.5000  Buffer: 100000   Reward:    14.23   Steps:    999
Episode    46   Avg:     3.29   BestAvg:     -inf   σ:     3.06   |   ⍺: 0.5000  Buffer: 100000   Reward:    11.97   Steps:    999
Episode    47   Avg:     3.54   BestAvg:     -inf   σ:     3.46   |   ⍺: 0.5000  Buffer: 100000   Reward:    14.98   Steps:    999
Episode    48   Avg:     3.78   BestAvg:     -inf   σ:     3.82   |   ⍺: 0.5000  Buffer: 100000   Reward:    15.26   Steps:    999
Episode    49   Avg:     4.00   BestAvg:     -inf   σ:     4.07   |   ⍺: 0.5000  Buffer: 100000   Reward:    14.48   Steps:    999
Episode    50   Avg:     4.22   BestAvg:     -inf   σ:     4.29   |   ⍺: 0.5000  Buffer: 100000   Reward:    14.64   Steps:    999
Episode    51   Avg:     4.47   BestAvg:     -inf   σ:     4.63   |   ⍺: 0.5000  Buffer: 100000   Reward:    17.47   Steps:    999
Episode    52   Avg:     4.69   BestAvg:     -inf   σ:     4.84   |   ⍺: 0.5000  Buffer: 100000   Reward:    15.67   Steps:    999
Episode    53   Avg:     4.93   BestAvg:     -inf   σ:     5.09   |   ⍺: 0.5000  Buffer: 100000   Reward:    17.28   Steps:    999
Episode    54   Avg:     5.18   BestAvg:     -inf   σ:     5.36   |   ⍺: 0.5000  Buffer: 100000   Reward:    18.54   Steps:    999
Episode    55   Avg:     5.49   BestAvg:     -inf   σ:     5.78   |   ⍺: 0.5000  Buffer: 100000   Reward:    22.22   Steps:    999
Episode    56   Avg:     5.81   BestAvg:     -inf   σ:     6.21   |   ⍺: 0.5000  Buffer: 100000   Reward:    23.59   Steps:    999
Episode    57   Avg:     6.14   BestAvg:     -inf   σ:     6.62   |   ⍺: 0.5000  Buffer: 100000   Reward:    24.40   Steps:    999
Episode    58   Avg:     6.49   BestAvg:     -inf   σ:     7.09   |   ⍺: 0.5000  Buffer: 100000   Reward:    26.76   Steps:    999
Episode    59   Avg:     6.82   BestAvg:     -inf   σ:     7.45   |   ⍺: 0.5000  Buffer: 100000   Reward:    25.44   Steps:    999
Episode    60   Avg:     7.18   BestAvg:     -inf   σ:     7.89   |   ⍺: 0.5000  Buffer: 100000   Reward:    28.46   Steps:    999
Episode    61   Avg:     7.56   BestAvg:     -inf   σ:     8.35   |   ⍺: 0.5000  Buffer: 100000   Reward:    30.30   Steps:    999
Episode    62   Avg:     7.99   BestAvg:     -inf   σ:     8.95   |   ⍺: 0.5000  Buffer: 100000   Reward:    34.35   Steps:    999
Episode    63   Avg:     8.41   BestAvg:     -inf   σ:     9.49   |   ⍺: 0.5000  Buffer: 100000   Reward:    34.87   Steps:    999
Episode    64   Avg:     8.83   BestAvg:     -inf   σ:     9.98   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.12   Steps:    999
Episode    65   Avg:     9.23   BestAvg:     -inf   σ:    10.41   |   ⍺: 0.5000  Buffer: 100000   Reward:    34.85   Steps:    999
Episode    66   Avg:     9.65   BestAvg:     -inf   σ:    10.86   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.75   Steps:    999
Episode    67   Avg:    10.05   BestAvg:     -inf   σ:    11.25   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.21   Steps:    999
Episode    68   Avg:    10.45   BestAvg:     -inf   σ:    11.65   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.63   Steps:    999
Episode    69   Avg:    10.84   BestAvg:     -inf   σ:    12.00   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.07   Steps:    999
Episode    70   Avg:    11.22   BestAvg:     -inf   σ:    12.32   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.37   Steps:    999
Episode    71   Avg:    11.59   BestAvg:     -inf   σ:    12.62   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.43   Steps:    999
Episode    72   Avg:    11.95   BestAvg:     -inf   σ:    12.90   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.64   Steps:    999
Episode    73   Avg:    12.30   BestAvg:     -inf   σ:    13.14   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.39   Steps:    999
Episode    74   Avg:    12.64   BestAvg:     -inf   σ:    13.39   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.89   Steps:    999
Episode    75   Avg:    12.97   BestAvg:     -inf   σ:    13.59   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.31   Steps:    999
Episode    76   Avg:    13.30   BestAvg:     -inf   σ:    13.80   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.90   Steps:    999
Episode    77   Avg:    13.62   BestAvg:     -inf   σ:    13.99   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.70   Steps:    999
Episode    78   Avg:    13.93   BestAvg:     -inf   σ:    14.16   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.93   Steps:    999
Episode    79   Avg:    14.22   BestAvg:     -inf   σ:    14.31   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.36   Steps:    999
Episode    80   Avg:    14.52   BestAvg:     -inf   σ:    14.47   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.94   Steps:    999
Episode    81   Avg:    14.81   BestAvg:     -inf   σ:    14.61   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.84   Steps:    999
Episode    82   Avg:    15.08   BestAvg:     -inf   σ:    14.72   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.78   Steps:    999
Episode    83   Avg:    15.34   BestAvg:     -inf   σ:    14.82   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.20   Steps:    999
Episode    84   Avg:    15.60   BestAvg:     -inf   σ:    14.92   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.70   Steps:    999
Episode    85   Avg:    15.85   BestAvg:     -inf   σ:    15.01   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.28   Steps:    999
Episode    86   Avg:    16.09   BestAvg:     -inf   σ:    15.09   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.74   Steps:    999
Episode    87   Avg:    16.33   BestAvg:     -inf   σ:    15.16   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.75   Steps:    999
Episode    88   Avg:    16.57   BestAvg:     -inf   σ:    15.25   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.70   Steps:    999
Episode    89   Avg:    16.81   BestAvg:     -inf   σ:    15.32   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.39   Steps:    999
Episode    90   Avg:    17.04   BestAvg:     -inf   σ:    15.39   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.50   Steps:    999
Episode    91   Avg:    17.26   BestAvg:     -inf   σ:    15.45   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.51   Steps:    999
Episode    92   Avg:    17.48   BestAvg:     -inf   σ:    15.50   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.16   Steps:    999
Episode    93   Avg:    17.65   BestAvg:     -inf   σ:    15.51   |   ⍺: 0.5000  Buffer: 100000   Reward:    33.26   Steps:    999
Episode    94   Avg:    17.83   BestAvg:     -inf   σ:    15.52   |   ⍺: 0.5000  Buffer: 100000   Reward:    34.18   Steps:    999
Episode    95   Avg:    18.01   BestAvg:     -inf   σ:    15.54   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.72   Steps:    999
Episode    96   Avg:    18.20   BestAvg:     -inf   σ:    15.56   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.59   Steps:    999
Episode    97   Avg:    18.39   BestAvg:     -inf   σ:    15.59   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.48   Steps:    999
Episode    98   Avg:    18.57   BestAvg:     -inf   σ:    15.63   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.93   Steps:    999
Episode    99   Avg:    18.76   BestAvg:     -inf   σ:    15.66   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.00   Steps:    999
Episode   100   Avg:    18.94   BestAvg:     -inf   σ:    15.68   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.60   Steps:    999
Episode   100   Avg:    18.94   BestAvg:     -inf   σ:    15.68   |   ⍺: 0.5000  Buffer: 100000   |   Steps:    99900  Secs:   2504
Episode   101   Avg:    19.30   BestAvg:    19.30   σ:    15.66   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.43   Steps:    999
Episode   102   Avg:    19.65   BestAvg:    19.65   σ:    15.64   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.35   Steps:    999
Episode   103   Avg:    20.00   BestAvg:    20.00   σ:    15.62   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.17   Steps:    999
Episode   104   Avg:    20.35   BestAvg:    20.35   σ:    15.57   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.51   Steps:    999
Episode   105   Avg:    20.69   BestAvg:    20.69   σ:    15.53   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.49   Steps:    999
Episode   106   Avg:    21.03   BestAvg:    21.03   σ:    15.48   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.52   Steps:    999
Episode   107   Avg:    21.36   BestAvg:    21.36   σ:    15.42   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.21   Steps:    999
Episode   108   Avg:    21.72   BestAvg:    21.72   σ:    15.36   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.74   Steps:    999
Episode   109   Avg:    22.06   BestAvg:    22.06   σ:    15.29   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.77   Steps:    999
Episode   110   Avg:    22.41   BestAvg:    22.41   σ:    15.22   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.86   Steps:    999
Episode   111   Avg:    22.76   BestAvg:    22.76   σ:    15.14   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.73   Steps:    999
Episode   112   Avg:    23.12   BestAvg:    23.12   σ:    15.06   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.04   Steps:    999
Episode   113   Avg:    23.46   BestAvg:    23.46   σ:    14.96   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.00   Steps:    999
Episode   114   Avg:    23.82   BestAvg:    23.82   σ:    14.86   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.35   Steps:    999
Episode   115   Avg:    24.17   BestAvg:    24.17   σ:    14.75   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.03   Steps:    999
Episode   116   Avg:    24.52   BestAvg:    24.52   σ:    14.63   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.24   Steps:    999
Episode   117   Avg:    24.87   BestAvg:    24.87   σ:    14.51   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.87   Steps:    999
Episode   118   Avg:    25.23   BestAvg:    25.23   σ:    14.37   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.44   Steps:    999
Episode   119   Avg:    25.57   BestAvg:    25.57   σ:    14.21   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.01   Steps:    999
Episode   120   Avg:    25.93   BestAvg:    25.93   σ:    14.05   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.03   Steps:    999
Episode   121   Avg:    26.28   BestAvg:    26.28   σ:    13.88   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.17   Steps:    999
Episode   122   Avg:    26.63   BestAvg:    26.63   σ:    13.68   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.57   Steps:    999
Episode   123   Avg:    26.98   BestAvg:    26.98   σ:    13.48   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.97   Steps:    999
Episode   124   Avg:    27.34   BestAvg:    27.34   σ:    13.27   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.48   Steps:    999
Episode   125   Avg:    27.68   BestAvg:    27.68   σ:    13.06   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.21   Steps:    999
Episode   126   Avg:    28.02   BestAvg:    28.02   σ:    12.82   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.28   Steps:    999
Episode   127   Avg:    28.37   BestAvg:    28.37   σ:    12.55   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.75   Steps:    999
Episode   128   Avg:    28.71   BestAvg:    28.71   σ:    12.28   |   ⍺: 0.5000  Buffer: 100000   Reward:    35.95   Steps:    999
Episode   129   Avg:    29.05   BestAvg:    29.05   σ:    12.01   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.41   Steps:    999
Episode   130   Avg:    29.40   BestAvg:    29.40   σ:    11.73   |   ⍺: 0.5000  Buffer: 100000   Reward:    37.26   Steps:    999
Episode   131   Avg:    29.73   BestAvg:    29.73   σ:    11.44   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.13   Steps:    999
Episode   132   Avg:    30.06   BestAvg:    30.06   σ:    11.15   |   ⍺: 0.5000  Buffer: 100000   Reward:    36.33   Steps:    999
Episode   132   Avg:    30.06   BestAvg:    30.06   σ:    11.15   |   ⍺: 0.5000  Buffer: 100000   |   Steps:   131868  Secs:   3235

Solved in 32 episodes!
```
