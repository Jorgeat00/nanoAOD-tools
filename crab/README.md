### Produce TnP n-tuples using crab

Execute the script SubmitDatasets.py with proper options. Try to execute it with no options to obtain info and examples. For example:

    python SubmitDatasets.py --datasets [DATASET] --outTier [T2_ES_IFCA] --prodName jul20 --options "2017"

You can create a txt file with samples and send jobs for all of them.

    python SubmitDatasets.py datasets/data2017_TnP.txt --test --pretend --verbose --options "TnP,2017"

### Produce skim for nano Run3
```bash
python SubmitDatasets.py datasets/mc2022PostEE_v12.txt --prodName mcRun3_PostEE_oct2023 -v --outTier T2_ES_IFCA
```
```bash
python SubmitDatasets.py datasets/mc2022_v12.txt --prodName mcRun3_2022_oct2023 -v --outTier T2_ES_IFCA
```
```bash
python SubmitDatasets.py datasets/data2022PostEE_v12.txt --prodName dataRun3_PostEE_oct2023 -v --outTier T2_ES_IFCA
```
```bash
python SubmitDatasets.py datasets/data2022_v12.txt --prodName dataRun3_2022_oct2023 -v --outTier T2_ES_IFCA
```