# FRAPS Frametime Analysis Grapher 

Simple script that does some statistical analysis of the frame time results from FRAPS and creates a graph summary.

## Installation

Download the script and place in directory of choice.

## Usage:

1. [Download fraps](https://fraps.com/download.php).
2. Run the benchmark tool and copy any number of frametime result files (in the form `* frametimes.csv`) to the same directory as the script.
3. Execute the script, it will load and analyse all relevent csv files in the same directory.

## Dependencies:
- matplotlib
- pandas
- scipy

## Examples

![Example](https://i.ibb.co/Tt4wQ5H/3.png)

```
Analysis of MCC-Win64-Shipping 2021-01-02 02-18-38-18 frametimes.csv
Frame Time Average 5.382341668561036
Frame Time Standard Deviation 5.900677549318819
Frames Per Second Average 220.48527275079527
Frames Per Second Standard Deviation 73.69543615204748
FPS Percentiles:
01: 79.23299856778335 10: 138.45813195990996
99: 426.27931886219443 90: 322.6847370119227
```

## License
[unlicense](https://choosealicense.com/licenses/unlicense/)
